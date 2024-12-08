from django.shortcuts import render  


# Create your views here.
def index2(request):
    return render(request, "index2.html", {"book":"cs"})
def links(request):
    return render(request, 'links.html')

def formatting(request):
    return render(request, 'formatting.html')

def listing(request):
    return render(request, 'listing.html')

def tables(request):
    return render(request, 'tables.html')

from django.shortcuts import render

# Function to simulate a list of books
def __getBooksList():
    return [
        {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'},
        {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'},
        {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    ]

# View to handle search form and results
def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        filtered_books = [book for book in books if
                          (isTitle and string in book['title'].lower()) or
                          (isAuthor and string in book['author'].lower())]

        return render(request, 'book/bookList.html', {'books': filtered_books})
    return render(request, 'book/search.html')

from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Address, Student

def lab8_tasks(request):
    task = request.GET.get('task')  # استخراج رقم المهمة من المعلمات
    context = {}

    if task == '1':
        context['books'] = Book.objects.filter(Q(price__lte=50))
        context['title'] = "Books with price ≤ 50"

    elif task == '2':
        context['books'] = Book.objects.filter(
            Q(edition__gt=2) &
            (Q(title__icontains='qu') | Q(author__icontains='qu'))
        )
        context['title'] = "Books with edition > 2 and title/author containing 'qu'"

    elif task == '3':
        context['books'] = Book.objects.filter(
            ~Q(edition__gt=2) &
            ~Q(title__icontains='qu') & ~Q(author__icontains='qu')
        )
        context['title'] = "Books with no edition > 2 and no 'qu' in title/author"

    elif task == '4':
        context['books'] = Book.objects.order_by('title')
        context['title'] = "Books ordered by title"

    elif task == '5':
        stats = Book.objects.aggregate(
            total_books=Count('id'),
            total_price=Sum('price'),
            avg_price=Avg('price'),
            max_price=Max('price'),
            min_price=Min('price')
        )
        context['stats'] = stats
        context['title'] = "Books Statistics"

    elif task == '6':
        context['students'] = Student.objects.all()
        context['title'] = "Student List"

    elif task == '7':
        context['cities'] = Address.objects.annotate(num_students=Count('student'))
        context['title'] = "Number of Students in Each City"

    return render(request, 'lab8.html', context)

# Create your views here.
def add_sample_books():
    Book.objects.create(title="Test Book 1", author="Author 1", price=10, edition=1)
    Book.objects.create(title="Test Book 2", author="Author 2", price=15, edition=2)
    Book.objects.create(title="Test Book 3", author="Author 3", price=20, edition=3)

    #10 
    from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# عرض قائمة الكتب
def list_books(request):
    books = Book.objects.all()
    return render(request, 'book/list_books.html', {'books': books})

# إضافة كتاب جديد
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form, 'action': 'Add Book'})

# تعديل كتاب
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)  # جلب الكائن
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # إعادة التوجيه إلى صفحة قائمة الكتب
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form, 'action': 'Edit Book'})


# حذف كتاب
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'book/delete_book.html', {'book': book})
