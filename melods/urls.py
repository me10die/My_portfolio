from django.urls import path
from .views import Home, Skills, Contact, About, Cv

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('/about',About.as_view(), name='about'),
    path('/skills',Skills.as_view(), name='skills'),
    path('/contact',Contact.as_view(), name='contact'),
    path('/cv',Cv.as_view(), name='cv'),

]
