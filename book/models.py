from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'countries'
        ordering = 'name',
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, models.DO_NOTHING, 'authors')

    class Meta:
        db_table = 'authors'
        ordering = 'first_name', 'last_name'
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'categories'
        ordering = 'name',
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, models.DO_NOTHING, 'books')
    categories = models.ManyToManyField(Category, related_name='books')

    class Meta:
        db_table = 'books'
        ordering = '-id',
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.title
