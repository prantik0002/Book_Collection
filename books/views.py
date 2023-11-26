from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
#from .models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
#from helpers.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading


from rest_framework.generics import CreateAPIView, ListAPIView,  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters

from books.serializers import BookSerializer

from .filters import BookFilter

from rest_framework import viewsets, permissions

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import book_user
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import random




@api_view(['GET', 'POST'])
def book_list(request, format=None):

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def book_detail(request, id, format=None):

    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        serializer = BookSerializer(book, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


def greeting(request):
    return render(request,"greeting.html")
def signup(request):
    return render(request,"signup.html")
def savedata(request):
    if request.method=='POST':
        formData=request.POST
        cre1=User()
        cre1.username=formData['username']
        cre1.set_password(formData['password']) 
        cre1.email=formData['email']
        cre1.save()
        request.session['email']=formData['email']
        request.session['username']=formData['username']
        request.session['password']=formData['password']
        return  HttpResponseRedirect('http://localhost:8000/books/')
def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email = request.POST['email']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['email']=email
            request.session['username']=username
            request.session['password']=password
            return  HttpResponseRedirect('http://localhost:8000/books/')
        else:
            data['error']="Username or Password is incorrect"
            return render(request,'user_login.html',data)
    else:
        return render(request,'user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/login/')

def about(request):
    s="""<h1>About</h1>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Debitis autem non unde provident, sed, laboriosam vitae quibusdam veniam ullam molestias iusto eveniet, recusandae est placeat incidunt. Dicta consequatur facere inventore cupiditate culpa saepe. Sapiente nostrum consequuntur nesciunt, ratione tenetur quidem saepe mollitia tempore quasi suscipit, facere doloribus animi voluptatibus dignissimos!
    </p>"""
    return HttpResponse(s)
def showContact(request):
    s="""<table>
            <tr>
                <td>Address</td>
                <td>73,Arjun Complex,Shivaji Nagar,Mumbai</td>
            </tr>
            <tr>
                <td>Email</td>
                <td>contact@xyz.com</td>
            </tr>
            <tr>
                <td>Phone</td>
                <td>022-6387912</td>
            </tr>
        </table>"""
    return HttpResponse(s)
