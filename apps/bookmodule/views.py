from django.shortcuts import render
from django.http import HttpResponse
from .models import Book  # ✅ Import the Book model

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    mybooks = Book.objects.all()
    books = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': mybooks}) 

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

def add_book(request):
   mybook = Book(title='Continuous Delivery', author='J. Humble and D. Farley', edition=1)
   mybook.save() 
   return HttpResponse("Book added successfully!")

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')  # ✅ Query to filter books with "and" in title
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})  # ✅ Pass books to the template

# ✅ Add missing complex query function
def complex_query(request):
    # ✅ Ensure your Book model has a `price` field before filtering by it
    mybooks = Book.objects.filter(
        author__isnull=False  # ✅ Author must not be NULL
    ).filter(
        title__icontains='and'  # ✅ Title must contain 'and' (case-insensitive)
    ).filter(
        edition__gte=2  # ✅ Edition must be greater than or equal to 2
    ).exclude(
        price__lte=100  # ✅ Exclude books with price <= 100
    )[:10]  # ✅ Limit results to 10 books

    # ✅ If books exist, render bookList.html, otherwise render index.html
    if mybooks.exists():
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')  # Redirect to index page if no books match
