from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path('signup', views.signup, name='signup'),
    path('signinstudent', views.signinstudent, name = 'signinstudent'),
    path('signinmentor', views.signinmentor, name = 'signinmentor'),
    path('signupstudent', views.signupstudent, name= 'signupstudent'),
    path('signupmentor', views.signupmentor, name= 'signupmentor'),
    path('studenthomepage', views.studenthomepage, name = 'studenthomepage'),
    path('mentorhomepage', views.mentorhomepage, name = 'mentorhomepage'),

]