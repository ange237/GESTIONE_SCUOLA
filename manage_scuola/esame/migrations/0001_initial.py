# Generated by Django 5.2.1 on 2025-05-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Esame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_corso', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
