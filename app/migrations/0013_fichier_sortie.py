# Generated by Django 3.1.7 on 2021-04-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_fichier_sortie'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichier',
            name='sortie',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]