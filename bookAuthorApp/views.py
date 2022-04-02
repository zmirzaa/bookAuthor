from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request): 
    context = {
        "books": Book.objects.all()
    }
    return render(request,'index.html', context)

def addBook(request): 
    Book.objects.create(
        title = request.POST['title'], 
        desc = request.POST['desc']
    )
    return redirect('/')

def viewBook(request, id): 
    context = {
        "book": Book.objects.get(id=id),
        "authors": Author.objects.all()
    }
    return render(request, "book.html", context)


def addAuthorBook(request): 
    book_id= request.POST['book_id']
    book =  Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=request.POST['author_id'])
    book.save()
    author.save()
    book.authors.add(author)
    return redirect(f'/view/{book_id}')
    

def authors(request): 
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "authors.html", context)


def addAuthor(request): 
    Author.objects.create(
        firstName = request.POST['firstName'], 
        lastName = request.POST['lastName'], 
        notes = request.POST['notes']
    )
    return redirect('/authors')

def viewAuthor(request, id): 
    context = {
        "author": Author.objects.get(id=id),
        "books": Book.objects.all()
    }
    return render(request, "author.html", context)

def addBookAuthor(request): 
    author_id = request.POST['author_id']
    author = Author.objects.get(id=request.POST['author_id'])
    book =  Book.objects.get(id=request.POST['book_id'])
    author.save()
    book.save()
    author.books.add(book)
    return redirect(f'/view/author/{author_id}')
