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
    
    #Lab 8 Tasks
    path('lab8/task1', views.task1, name='task1'),
    path('lab8/task2', views.task2, name='task2'),
    path('lab8/task3', views.task3, name='task3'),
    path('lab8/task4', views.task4, name='task4'),
    path('lab8/task5', views.task5, name='task5'),
    path('lab8/task7', views.city_count, name='task7'),
    
    path('students/', views.students_with_cards, name='students_with_cards'),
    #lab9
    path('lab9/task1', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='lab9_task4'),
    
    #lab10
    path('lab9_part1/listbooks', views.list_books_lab9_part1, name='list_books_lab9_part1'),
    path('lab9_part1/addbook', views.add_book_lab9_part1, name='add_book_lab9_part1'),
    path('lab9_part1/editbook/<int:book_id>/', views.edit_book_lab9_part1, name='edit_book_lab9_part1'),
    path('lab9_part1/deletebook/<int:book_id>/', views.delete_book_lab9_part1, name='delete_book_lab9_part1'),
    
    # Lab 10 Part 2
    path('lab9_part2/listbooks', views.list_books_lab9_part2, name='list_books_lab9_part2'),
    path('lab9_part2/addbook', views.add_book_lab9_part2, name='add_book_lab9_part2'),
    path('lab9_part2/editbook/<int:book_id>/', views.edit_book_lab9_part2, name='edit_book_lab9_part2'),
    path('lab9_part2/deletebook/<int:book_id>/', views.delete_book_lab9_part2, name='delete_book_lab9_part2'),

    #lab11
    path('lab11_part1/liststudents', views.list_students_lab11_part1, name='list_students_lab11_part1'),
    path('lab11_part1/addstudent/', views.add_student_lab11_part1, name='add_student_lab11_part1'),
    path('lab11_part1/editstudent/<int:student_id>/', views.edit_student_lab11_part1, name='edit_student_lab11_part1'),
    path('lab11_part1/deletestudent/<int:student_id>/', views.delete_student_lab11_part1, name='delete_student_lab11_part1'),
    
    # lab11 part2
    path('lab11_part2/listaddresses', views.list_addresses_lab11_part2, name='list_addresses_lab11_part2'),
    path('lab11_part2/addaddress/', views.add_address_lab11_part2, name='add_address_lab11_part2'),
    path('lab11_part2/editaddress/<int:address_id>/', views.edit_address_lab11_part2, name='edit_address_lab11_part2'),
    path('lab11_part2/deleteaddress/<int:address_id>/', views.delete_address_lab11_part2, name='delete_address_lab11_part2'),

]

 



    

