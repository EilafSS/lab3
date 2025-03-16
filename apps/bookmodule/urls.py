from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),

    # ✅ Ensure function names match `views.py`
    path('html5/links/', views.html_links, name="books.html_links"),  
    path('html5/textformat/', views.text_format, name="books.text_format"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.html5_tables, name='books.tables'),  # ✅ Fixed reference

    # Search Page
    path('search/', views.search_books, name="books.search"),
]
