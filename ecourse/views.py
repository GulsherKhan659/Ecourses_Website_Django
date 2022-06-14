from copy import error
from django.http import HttpResponse
from django.shortcuts import render
from courses_card.models import AddCourseCategory, Courses
from teachers.models import Teacher



def practice(response,myid):
    data = {
        'id':myid
    }
    return render(response,"0practice.html",data)

def index_page(response):
    
    course_categories = AddCourseCategory.objects.all()[0:8]
    count_of_courses =[]
    try:
        for x in range(1,len(course_categories)+1):
            count_of_courses.append( (Courses.objects.filter(course_type="{}".format(x)).count())) 
        zipped_data = zip(count_of_courses,course_categories)
    except:
        pass
    data = {
        'zipped_data':zipped_data,
    }
    return render(response,"index.html",data)

def blog_page(response):
    return render(response,"blog.html")

def contact_page(response):
    return render(response,"contact.html")

def course_page(response):
    courses = Courses.objects.all()[0:6]
    course_categories = AddCourseCategory.objects.all()[0:8]
    count_of_courses =[]
    try:
        for x in range(1,len(course_categories)+1):
            count_of_courses.append( (Courses.objects.filter(course_type="{}".format(x)).count())) 
        zipped_data = zip(count_of_courses,course_categories)

    except:
        pass
    data = {
        'zipped_data':zipped_data,
        'num': [str(x) for x in range(1,9)],
        'courses': courses
    }
    return render(response,"course.html",data)

def teacher_page(response):
    try:
        teachers = Teacher.objects.all()
        data ={
            "teachers":teachers
        }
    except:
        print("Unexped Error ==> {}".format(error))

    return render(response,"teacher.html",data)

def about_page(response):
    return render(response,"about.html")


def course_details(response,id):
    data={}
    query_data = Courses.objects.get(id=id)
    try:
        data = {
        "course_detail":query_data
        }
    except:
       print("Error Found ===> {}".format(error))
    return render(response,"course_detail.html",data)


def courses_by_categories(response,id):
    data = {}
    try:
        if id==1:
            query_data = Courses.objects.filter(course_type="{}".format(id))
        else:
            query_data = Courses.objects.filter(course_type="{}".format(int(id)-1))
        data = {
        "courses" : query_data
                }
    except :
        print("Error Found ===> {}".format(error))
        pass
    return render(response,"course_by_categories.html",data)



def all_categories(response):
    course_categories = AddCourseCategory.objects.all()
    count_of_courses =[]
    try:
        for x in range(1,len(course_categories)+1):
            count_of_courses.append( (Courses.objects.filter(course_type="{}".format(x)).count())) 
        zipped_data = zip(count_of_courses,course_categories)
        data = {
            'zipped_data':zipped_data
             }
    except:
        print("Unexpected Error in views.allcategories")
        pass
    return render(response,"categories.html",data)

def all_courses(response):
    courses = Courses.objects.all()
    data= {
         'courses': courses,
         'num': [str(x) for x in range(1,9)],
    }
    return render(response,"courses.html",data)
