from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def html5_links(request):  # ✅ Corrected function name
    return render(request, 'bookmodule/html5_links.html')

def text_format(request):
    return render(request, 'bookmodule/text_format.html')

def listing(request):
    return render(request, "bookmodule/listing.html")

def html5_tables(request):  # ✅ Corrected function name (was 'html_tabels')
    return render(request, 'bookmodule/tables.html')
