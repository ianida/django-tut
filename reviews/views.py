from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, ReviewForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'reviews/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'reviews/add_book.html', {'form': form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'reviews/book_detail.html', {'book': book})

def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form, 'book': book})
