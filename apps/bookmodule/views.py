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

# ✅ Keep only one function for HTML links
def html_links(request):  
    return render(request, 'bookmodule/html5_links.html')

def text_format(request):
    return render(request, 'bookmodule/text_format.html')

def listing(request):
    return render(request, "bookmodule/listing.html")

# ✅ Fix function name (previously was 'html_tabels')
def html5_tables(request):
    return render(request, 'bookmodule/tables.html')

def search_books(request):
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]
def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # Get the list of books
        books = __getBooksList()
        newBooks = []

        # Filtering books based on search criteria
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            
            if contained:
                newBooks.append(item)

        # Render the results page
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    # Default rendering if form is not submitted
    return render(request, 'bookmodule/search.html')