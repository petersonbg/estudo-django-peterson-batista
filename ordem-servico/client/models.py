from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from localflavor.br.models import BRCPFField, BRCNPJField, BRPostalCodeField, BRStateField


class CustomerData(models.Model):
    cpf = BRCPFField("CPF", max_length=14, blank=True)
    cnpj = BRCNPJField("CNPJ", max_length=18, blank=True)
    name = models.CharField("Nome Completo", max_length=250)
    slug = AutoSlugField(unique=True, always_update=False, populate_from='name')
    email = models.EmailField("E-mail")
    cell = models.CharField("Celular", max_length=14)
    postal_code = BRPostalCodeField("CEP")
    address = models.CharField("Endereço", max_length=250)
    number = models.CharField("Número", max_length=250)
    complement = models.CharField("Complemento", max_length=250, blank=True)
    district = models.CharField("Bairro", max_length=250)
    state = BRStateField("Estado")
    city = models.CharField("Cidade", max_length=250)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("client:client-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

