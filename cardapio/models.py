from django.db import models
from db_file_storage.model_utils import delete_file, delete_file_if_needed


# --- MODELO 1: CATEGORIA (Chave para agrupar Cardápio e Jogos) ---
class Categoria(models.Model):
    """
    Define a categoria de um item (Comidas, Bebidas, Sobremesas, Tabuleiro, Máquinas).
    """
    nome = models.CharField(max_length=100, unique=True)
    # Slug é útil para URLs amigáveis, embora não seja estritamente necessário para este trabalho
    slug = models.SlugField(max_length=100, unique=True) 
    # Campo opcional para guardar o emoji/ícone (🍽️, 🎲, etc.)
    icone = models.CharField(max_length=10, blank=True, null=True) 

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

# --- FILE MODEL: Imagem de Item de Cardápio (armazenada no banco) ---
class ItemCardapioImage(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)

# --- MODELO 2: ITEM CARDÁPIO (Comidas, Bebidas, Sobremesas) ---
class ItemCardapio(models.Model):
    """
    Representa um item do cardápio (comida, bebida ou sobremesa).
    """
    nome = models.CharField(max_length=200, unique=True)
    descricao = models.TextField()
    # Usa ImageField com armazenamento no banco via django-db-file-storage
    imagem = models.ImageField(
        upload_to='cardapio.ItemCardapioImage/bytes/filename/mimetype',
        blank=True,
        null=True,
    ) 
    
    # RELACIONAMENTO (Um-para-Muitos): Um item pertence a uma Categoria
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE, # Se a categoria for apagada, os itens dela também são.
        related_name='itens_cardapio'
    )

    class Meta:
        verbose_name = "Item de Cardápio"
        verbose_name_plural = "Itens do Cardápio"
        # Garante que as comidas/bebidas sejam listadas por nome
        ordering = ['nome'] 

    def __str__(self):
        return f"{self.nome} ({self.categoria.nome})"

    def save(self, *args, **kwargs):
        # Remove arquivo antigo (se alterado) antes de salvar
        delete_file_if_needed(self, 'imagem')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Apaga o registro e depois remove o arquivo associado
        super().delete(*args, **kwargs)
        delete_file(self, 'imagem')

# --- MODELO 3: JOGO (Item base para rastreamento) ---
class Jogo(models.Model):
    """
    Representa um tipo de jogo disponível no bar (ex: Dungeons & Dragons).
    """
    nome = models.CharField(max_length=200, unique=True)
    tipo = models.CharField(max_length=100) # Ex: RPG de fantasia, Luta clássica arcade
    descricao = models.TextField()
    # --- FILE MODEL: Imagem de Jogo (armazenada no banco) ---
    # Declarado abaixo para manter ordem do arquivo legível
    imagem = models.ImageField(
        upload_to='cardapio.JogoImage/bytes/filename/mimetype',
        blank=True,
        null=True,
    )

    # RELACIONAMENTO (Um-para-Muitos): Um jogo pertence a uma Categoria
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='jogos'
    )

    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    # Método de conveniência para ser usado nas views
    def copias_disponiveis(self):
        return self.copias.filter(disponivel=True).count()

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'imagem')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        delete_file(self, 'imagem')

# --- FILE MODEL: Imagem de Jogo (armazenada no banco) ---
class JogoImage(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)

# --- MODELO 4: COPIA JOGO (Inventário e Rastreamento de Disponibilidade) ---
class CopiaJogo(models.Model):
    """
    Representa uma cópia física específica de um Jogo.
    Isto permite rastrear a disponibilidade (requisito do trabalho).
    """
    # RELACIONAMENTO (Um-para-Muitos): Uma cópia pertence a um Jogo
    jogo = models.ForeignKey(
        Jogo,
        on_delete=models.CASCADE,
        related_name='copias' # Usado para o método copias_disponiveis acima
    )
    # Identificador único para a cópia física (ex: Tag RFID, Número de Série)
    identificador = models.CharField(max_length=50, unique=True)
    # Campo crucial para o requisito de inventário
    disponivel = models.BooleanField(default=True)
    # Opcional: Rastrear onde está em uso (ex: Mesa 5)
    uso_atual = models.CharField(max_length=50, blank=True, null=True) 

    class Meta:
        verbose_name = "Cópia de Jogo"
        verbose_name_plural = "Cópias de Jogos"
        # Garante que não haja dois identificadores iguais para o mesmo jogo
        unique_together = ('jogo', 'identificador')

    def __str__(self):
        status = "Disponível" if self.disponivel else f"Em Uso ({self.uso_atual or 'Não Especificado'})"
        return f"{self.jogo.nome} - {self.identificador} ({status})"