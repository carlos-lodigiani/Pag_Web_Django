from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book
# Create your views here.



@login_required(login_url = '/login/')
def list_all_books(request):
    book = Book.objects.filter(active=True)
    return render(request, 'list.html', {'book': book})


def logout_user(request):
    logout(request)
    return redirect('/login/')

def list_user_book(request):
    book = Book.objects.filter(active=True, user= request.user)
    return render(request, 'list.html', {'book': book})

@login_required(login_url='/login/')
def register_book(request):
    book_id = request.GET.get('id')
    if book_id:
        book = Book.objects.get(id=book_id)
        return render(request, 'register-book.html', {'book': book})
    return render(request, 'register-book.html')

@login_required(login_url='/login/')
def set_book(request):
    name_of_user = request.POST.get('name_of_user')
    city = request.POST.get('city')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    photo = request.FILES.get('file')
    name_of_books = request.POST.get('name_of_books')
    book_id = request.POST.get('book-id')
    user = request.user
    if book_id:
        book = Book.objects.get(id=book_id)
        if user == book.user:
            book.name_of_user= name_of_user
            book.name_of_books= name_of_books
            book.email= email
            book.phone= phone
            book.city= city
            book.description= description
            if photo:
                book.photo=photo
            book.save()
        else:
            book = Book.objects.create(email=email, city=city, phone=phone, description=description,
                              photo=photo,
                              name_of_books=name_of_books, user=user)
        url = '/book/detail/{}/'.format(book.id)
        return redirect(url)

@login_required(login_url='/login/')
def delete_book(request, id):
    book = Book.objects.get(id=id)
    if book.user == request.user:
        book.delete()
    return redirect('/')


def book_detail(request, id):
    book = Book.objects.get(active=True, id=id)
    return render(request, 'book.html', {'book': book})

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, ' Usuário não encontrado. Favor verificar usuario ou senha ')
    return redirect('/login/')
