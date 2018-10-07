# Generated by Django 2.1.1 on 2018-10-03 15:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0006_remove_cities_wojewodztwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unikatowy klucz id', primary_key=True, serialize=False)),
                ('mieszkanie', models.CharField(max_length=30)),
                ('data_wynajecia', models.DateField(blank=True, null=True)),
                ('data_oddania', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='flats',
            name='zdjecie',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='flats',
            name='rezerwacje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rentals.Reservations'),
        ),
    ]