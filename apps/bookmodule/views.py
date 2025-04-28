from django.shortcuts import render
from django.http import HttpResponse
from .models import Book  # Import the Book model
from django.db.models import Q, Count, Sum, Avg, Max, Min
from django.db.models.functions import Lower
from .models import Book, Student, Address,Course, Department, Card  # Make sure Student and Address exist
from django.db.models import OuterRef, Subquery
from django.shortcuts import redirect
from .forms import BookForm 

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

#  Keep only one function for HTML links
def html_links(request):  
    return render(request, 'bookmodule/html5_links.html')

def text_format(request):
    return render(request, 'bookmodule/text_format.html')

def listing(request):
    return render(request, "bookmodule/listing.html")

# Fix function name (previously was 'html_tabels')
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
    mybooks = Book.objects.filter(title__icontains='and')  # Query to filter books with "and" in title
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})  # ✅ Pass books to the template

# Add missing complex query function
def complex_query(request):
    # Ensure your Book model has a `price` field before filtering by it
    mybooks = Book.objects.filter(
        author__isnull=False  # Author must not be NULL
    ).filter(
        title__icontains='and'  # Title must contain 'and' (case-insensitive)
    ).filter(
        edition__gte=2  # Edition must be greater than or equal to 2
    ).exclude(
        price__lte=100  # Exclude books with price <= 100
    )[:10]  # Limit results to 10 books

    # If books exist, render bookList.html, otherwise render index.html
    if mybooks.exists():
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')  # Redirect to index page if no books match
    

def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'lab8/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
       # Q(price__gte=2) & (Q(title__icontains='co') | Q(author__icontains='co'))
        Q(edition__lte=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
      
    print(books)
    return render(request, 'lab8/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & ~ (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'lab8/task3.html', {'books': books})
def task4(request):
    books = Book.objects.all().order_by(Lower('title'))
    return render(request, 'lab8/task4.html', {'books': books})
def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'lab8/task5.html', {'stats': stats})
def city_count(request):
    city_data = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'lab8/task7.html', {'city_data': city_data})

def student_list(request):
    students = Student.objects.select_related('card').all()
    return render(request, 'bookmodule/student_list.html', {'students': students})


def students_with_cards(request):
    students = Student.objects.select_related('card').all()
    return render(request, 'bookmodule/students_with_cards.html', {'students': students})
    print("students_with_cards loaded")
    
def lab9_task1(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab9_task1.html', {'departments': departments})

def lab9_task2(request):
    courses = Course.objects.annotate(num_students=Count('students'))
    return render(request, 'bookmodule/lab9_task2.html', {'courses': courses})

def lab9_task3(request):
    oldest_student_subquery = Student.objects.filter(department=OuterRef('pk')).order_by('id').values('name')[:1]
    departments = Department.objects.annotate(oldest_student_name=Subquery(oldest_student_subquery))

    return render(request, 'bookmodule/lab9_task3.html', {'departments': departments})


def lab9_task4(request):
    departments = Department.objects.annotate(num_students=Count('student')).filter(num_students__gt=2).order_by('-num_students')

    return render(request, 'bookmodule/lab9_task4.html', {'departments':departments})

#lab10

def list_books_lab9_part1(request):
    books = Book.objects.all()
    return render(request, 'lab9_part1/listbooks.html', {'books': books})


def add_book_lab9_part1(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        edition = request.POST.get('edition')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            author=author,
            edition=edition,
            price=price
        )
        return redirect('books:list_books_lab9_part1')
    
    return render(request, 'lab9_part1/addbook.html')


def edit_book_lab9_part1(request, book_id):
    book = Book.objects.get(id=book_id)
    
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.edition = request.POST.get('edition')
        book.price = request.POST.get('price')
        book.save()
        return redirect('books:list_books_lab9_part1')

    return render(request, 'lab9_part1/editbook.html', {'book': book})

def delete_book_lab9_part1(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('books:list_books_lab9_part1')


#lab10 part2
def list_books_lab9_part2(request):
    books = Book.objects.all()
    return render(request, 'lab9_part2/listbooks.html', {'books': books})



def add_book_lab9_part2(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:list_books_lab9_part2')
    else:
        form = BookForm()

    return render(request, 'lab9_part2/addbook.html', {'form': form})

def edit_book_lab9_part2(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:list_books_lab9_part2')
    else:
        form = BookForm(instance=book)

    return render(request, 'lab9_part2/editbook.html', {'form': form, 'book': book})

def delete_book_lab9_part2(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('books:list_books_lab9_part2')
