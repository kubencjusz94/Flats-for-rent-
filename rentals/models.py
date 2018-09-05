from django.db import models
import uuid

class Cities(models.Model):
    nazwa = models.CharField(max_length=30)
    wojewodztwo = models.CharField(max_length=20)
    def __str__(self):
        return self.nazwa

class Flats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikatowy klucz id')
    miasto = models.ForeignKey('Cities', on_delete=models.SET_NULL, null=True)
    adres = models.CharField(max_length=50)
    cena = models.IntegerField()
    kaucja = models.BooleanField()
    opis = models.TextField(max_length=500)

    FLAT_STATUS = (
        ('d', 'Dostępne'),
        ('n', 'Niedostępne')
    )
    status = models.CharField(
        max_length=1,
        choices=FLAT_STATUS,
        blank=True,
        default='m',
        help_text='Dostępność mieszkania',
    )

    def __str__(self):
        return f'{self.id} ({self.book.miasto}) ({self.book.adres})'
