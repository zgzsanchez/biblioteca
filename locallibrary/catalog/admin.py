from django.contrib import admin
from .models import Author, Genre, Book, Language, BookInstance

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(Language)
# admin.site.register(BookInstance)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')

#Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_display = ('book', 'status', 'due_back')
  list_filter = ('status', 'due_back')

#Register the Admin classes for Author using the decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth')

#Register the Admin classes for lenguage using the decorator
@admin.register(Language)
class LanguageInstanceAdmin(admin.ModelAdmin):
  pass

