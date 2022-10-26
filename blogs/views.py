from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    response = "Placeholder to later display all the list of blogs."
    return HttpResponse(response)


def new(request):
    response = "Placeholder to display a new form to create a new blog %s. "
    return HttpResponse(response)


def create(request):
    return redirect(index)


def show(request, blog_number):
    return HttpResponse("Placeholder to display blog %s." % blog_number)


def edit(request, blog_number):
    return HttpResponse("Placeholder to edit blog %s." % blog_number)


def destroy(request, blog_number):
    return redirect(index)
