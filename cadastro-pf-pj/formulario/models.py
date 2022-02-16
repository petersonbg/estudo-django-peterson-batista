from django.db import models


class DadosPessoa(models.Model):
    SEXO_CHOICE = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
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

    nome = models.CharField(max_length=100, verbose_name='Nome')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICE, verbose_name='Sexo')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    rg = models.CharField(max_length=11, verbose_name='RG')
    dt_nasc = models.DateField(verbose_name='Data de Nascimento', null=True)
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ')
    insc_estadual = models.CharField(max_length=15, verbose_name='Inscrição Estadual')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    email = models.CharField(max_length=100, verbose_name='E-mail')
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.CharField(max_length=2, choices=UF_CHOICES, verbose_name='Estado')



    def __str__(self):
        return f'{self.nome}'
