# Generated by Django 4.2.3 on 2023-07-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texnoshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]