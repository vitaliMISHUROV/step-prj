# Generated by Django 4.2.2 on 2023-06-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_page_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
