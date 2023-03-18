from django.db import models


class Article(models.Model):
    Title = models.CharField('Название', max_length=100, null=True)
    Image = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)
    Image_two = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)
    Country = models.CharField('Страна', max_length=20, null=True)
    Metal = models.CharField('Металл', max_length=50, null=True)
    Year = models.IntegerField('Год выпуска монеты', null=True)
    Nominal = models.IntegerField('Номинал', null=True)
    Text = models.TextField('Описание', max_length=250, null=True)

    def __str__(self):
        return self.Title