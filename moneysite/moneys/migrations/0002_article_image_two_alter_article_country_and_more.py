# Generated by Django 4.1.7 on 2023-03-14 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Image_two',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='Country',
            field=models.CharField(max_length=20, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='article',
            name='Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='Metal',
            field=models.CharField(max_length=50, null=True, verbose_name='Металл'),
        ),
        migrations.AlterField(
            model_name='article',
            name='Text',
            field=models.TextField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='Title',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='article',
            name='Year',
            field=models.IntegerField(null=True, verbose_name='Номинал'),
        ),
    ]