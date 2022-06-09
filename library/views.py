from django.shortcuts import render
from library.models import *

# Create your views here.
def book(request):
    return render(request,'book.html')

def addbook(request):
    if request.method == 'POST':
        bookdata = request.POST
        bid = bookdata.get('bid')
        book = None
        if bid:
            book = add_book.objects.filter(id=bid).first()
        if book:
            book.name = bookdata['name']
            book.auther = bookdata['auther']
            book.status = bookdata['status']
            message = 'Book Updated Successfully'
            book.save()
            return render(request, 'booklist.html', {"message": message , "book_list":add_book.objects.filter(is_available=True).all()})
        else:
            book = add_book(name=bookdata['name'],
                                auther=bookdata['auther'],
                                status=bookdata['status']
                                )
            message = 'Book Added Successfully'
            book.save()
            return render(request,'addbook.html',{"message":message})
    return render(request,'addbook.html')

def book_list(request):
    return render(request,'booklist.html',{"book_list":add_book.objects.filter(is_available=True).all()})

def update(request,bid):
    book = add_book.objects.filter(id=bid).first()
    if book:
        return render(request, 'update.html', {"book": book})

def delete(request,bid):
    book = add_book.objects.filter(id=bid).first()
    if book:
        book.is_available = False
        book.save()
        book = add_book.objects.filter(is_available=True).all()
        return render(request, 'booklist.html', {"book_list": book})

def studentview(request):
    return render(request,'studentview.html')

def studentview_booklist(request):
    return render(request,'studentbooklist.html',{"book_list":add_book.objects.filter(is_available=True).all()})