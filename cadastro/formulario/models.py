from django.db import models


# Create your models here.

class DadosCad(models.Model):
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )
    nome = models.CharField(max_length=255, null=False)
    sobrenome = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=14, null=False)
    email = models.EmailField( null=False)
    telefone = models.CharField(max_length=14, null=False)
    endereco = models.CharField(max_length=255, null=False)
    cidade = models.CharField(max_length=255, null=False)
    estado = models.CharField(max_length=2, choices=UF_CHOICES, null=False)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
