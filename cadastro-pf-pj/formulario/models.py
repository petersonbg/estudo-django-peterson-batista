from django.db import models


class DadosPessoa(models.Model):
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

    class Meta:
        abstract = True

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, choices=UF_CHOICES)


class DadosPessoaFisica(DadosPessoa):
    SEXO_CHOICE = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=11)
    dt_nasc = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICE)

    def __str__(self):
        return f'{self.nome}'


class DadosPessoaJuridica(DadosPessoa):
    cnpj = models.CharField(max_length=20)
    insc_estadual = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome}'
