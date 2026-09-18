from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название населенного пункта')
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Названия населенных пунктов'


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Язык программирования')
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
