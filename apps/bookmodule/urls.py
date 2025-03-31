from django.urls import path
from . import views
from .views import add_book, simple_query, complex_query

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),  # ✅ هذا هو الرابط الرئيسي
    path('add/', add_book, name='add'),
    path('simple/query/', simple_query, name='simple_query'),
    path('complex/query/', complex_query, name='complex_query'),
    path('list_books/', views.list_books, name='list_books'),
    path('<int:bookId>/', views.viewbook, name='view_one_book'),
    path('aboutus/', views.aboutus, name='aboutus'),

    # HTML5 related views
    path('html5/links/', views.html_links, name='html_links'),
    path('html5/textformat/', views.text_format, name='text_format'),
    path('html5/listing/', views.listing, name='listing'),
    path('html5/tables/', views.html5_tables, name='tables'),

    # Search
    path('search/', views.search_books, name='search'),
]
