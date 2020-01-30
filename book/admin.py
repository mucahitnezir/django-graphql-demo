from django.contrib import admin

from .models import Country, Author, Category, Book


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
