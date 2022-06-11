from django.http import HttpResponse
from django.shortcuts import render


def index_page(response):
    return render(response,"index.html")

def blog_page(response):
    return render(response,"blog.html")

def contact_page(response):
    return render(response,"contact.html")

def course_page(response):
    return render(response,"course.html")

def teacher_page(response):
    return render(response,"teacher.html")

def about_page(response):
    return render(response,"about.html")
