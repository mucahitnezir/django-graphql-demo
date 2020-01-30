from graphene_django import DjangoObjectType
import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation

from book.forms import CountryForm
from book.models import Author, Country, Category, Book


class CountryType(DjangoObjectType):
    class Meta:
        model = Country


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(graphene.ObjectType):
    author = graphene.Field(AuthorType, id=graphene.Int())
    authors = graphene.List(AuthorType)

    book = graphene.Field(BookType, id=graphene.Int())
    books = graphene.List(BookType)

    category = graphene.Field(CategoryType, id=graphene.Int())
    categories = graphene.List(CategoryType)

    country = graphene.Field(CountryType, id=graphene.Int())
    countries = graphene.List(CountryType)

    def resolve_author(self, info, **kwargs):
        pk = kwargs.get('id')
        return Author.objects.get(pk=pk)

    def resolve_authors(self, info):
        return Author.objects.select_related('country').all()

    def resolve_book(self, info, **kwargs):
        pk = kwargs.get('id')
        return Book.objects.get(pk=pk)

    def resolve_books(self, info):
        return Book.objects.select_related('author').all()

    def resolve_category(self, info, **kwargs):
        pk = kwargs.get('id')
        return Category.objects.get(pk=pk)

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_country(self, info, **kwargs):
        pk = kwargs.get('id')
        return Country.objects.get(pk=pk)

    def resolve_countries(self, info):
        return Country.objects.all()


class CountryMutation(DjangoModelFormMutation):
    country = graphene.Field(CountryType)

    class Meta:
        form_class = CountryForm


class Mutation(graphene.ObjectType):
    create_country = CountryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
