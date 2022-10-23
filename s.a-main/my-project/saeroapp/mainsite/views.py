from django.http.response import HttpResponse
from pickle import TRUE
from unicodedata import category
from django.shortcuts import render
from .models import staff, Category, Sponsors,Carousel



data={
    "personel":[
        {
        "id":1,
        "name":"emre durak",
        "task":"project manager",
        "image":"10.jpg",
        "is_active":True,
         },
            {
        "id":2,
        "name":"murat sağın",
        "task":"machine engineer",
        "image":"10.jpg",
        "is_active":True,
         },
            {
        "id":3,
        "name":"fatih terim",
        "task":"software developer",
        "image":"10.jpg",
        "is_active":True,
         }



    ]
}
# Create your views here.
def index(request):
    sponsors=Sponsors.objects.all()
    obj=Carousel.objects.all()
    context={
        "sponsors":sponsors,
        "obj":obj

    }
    return render(request,"home.html",context)

def about(request):
    teams=Category.objects.all()
    context={
        "teams":teams
    }
    return render(request,"about.html",context)

def team(request):
    context={
        "persons":staff.objects.filter(is_active=True),
        "categories":Category.objects.all()
    }
    return render(request,"team.html",context)


def team_details(request,slug):
    team=staff.objects.get(slug=slug)
    return render(request,"team-detail.html",{
        "team":team,
        "person":staff.objects.get(slug=slug)
    })

def staff_by_category(request,slug):
    context={
        "persons":Category.objects.get(slug=slug).staff_set.filter(is_active=True),
        # "persons":staff.objects.filter(is_active=True,category__slug=slug),
        "categories":Category.objects.all(),
        "selected_category":slug
    }
    return render(request,"team.html",context)
        







        




def contact(request):
    return render(request,"contact.html")
# def team_detail(request,slug):
#     return render(request,"team-detail.html",{
#         "slug":slug
#     })   


# def team_detail(request, id):
#     return HttpResponse ("blog details: " + str(id))