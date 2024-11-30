 
from django.urls import path
from Department import views

urlpatterns = [
    path('',views.home),
    path('createdepartment',views.createDepartment),
    path('delete/<int:did>',views.Deletedepartment),
    path('edit/<int:did>',views.updateDepartment),
]

