# Generated by Django 3.0.5 on 2020-04-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200423_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produit'},
        ),
        migrations.AddField(
            model_name='product',
            name='lipids_for_100g',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Lipides'),
        ),
        migrations.AddField(
            model_name='product',
            name='salt_for_100g',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Lipides'),
        ),
        migrations.AddField(
            model_name='product',
            name='saturated_fats_for_100g',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Lipides'),
        ),
        migrations.AddField(
            model_name='product',
            name='sugars_for_100g',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Lipides'),
        ),
    ]