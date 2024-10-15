from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newmentor", views.newmentor, name = "newmentor"),
    path("newstudent", views.newstudent, name = "newstudent"),
    path("updatementor/<str:mentorid>",views.updatementor, name="updatementor"),
    path("updatementor/updatedata/<str:mentorid>", views.updatedata, name = "updatedata"),
    path("updatestudent/<str:studentid>", views.updatestudent, name="updatestudent"),
    path("updatestudent/updatedatastudent/<str:studentid>", views.updatedatastudent, name="updatedatastudent"),
    path("deletementor/<str:mentorid>",views.deletementor, name = "deletementor"),
    path("deletementor/delete/<str:mentorid>",views.delete, name = "delete"),
    path("searchmentor", views.searchmentor, name="searchmentor")

    ]
