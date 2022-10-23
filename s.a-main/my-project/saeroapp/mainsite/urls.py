from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="home"), #bunun olayı site adresi base ise ne olcağını söylüyoruz. Hiç bir şey olmamasının anlamı bu --http://127.0.0.1:8000/
    path("home",views.index,name="home"), #bunun olayı site adresi base ise ne olcağını söylüyoruz. Hiç bir şey olmamasının anlamı bu --http://127.0.0.1:8000/
    path("about",views.about,name="about"), #bunun olayı site adresi base ise ne olcağını söylüyoruz. Hiç bir şey olmamasının anlamı bu --http://127.0.0.1:8000/
    path("team",views.team,name="team"), #bunun olayı site adresi base ise ne olcağını söylüyoruz. Hiç bir şey olmamasının anlamı bu --http://127.0.0.1:8000/
    path("category/<slug:slug>", views.staff_by_category, name="staff_by_category"),
    path("team/<slug:slug>",views.team_details,name="team-detail"), #bunun olayı site adresi base ise ne olcağını söylüyoruz. Hiç bir şey olmamasının anlamı bu --http://127.0.0.1:8000/
    path("contact",views.contact,name="contact"), #bunun olayı site adresi base ise ne olcağını söylüyoruz. Hiç bir şey olmamasının anlamı bu --http://127.0.0.1:8000/






]
