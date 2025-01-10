 
from django.urls import path
from Department import views

urlpatterns = [
    path('home/',views.showHome),
    path('',views.home),
    path('createdepartment',views.createDepartment),
    path('delete/<int:did>',views.Deletedepartment),
    path('edit/<int:did>',views.updateDepartment),
    #Roles:
    path('viewrole',views.viewRole),
    path('addrole',views.addRole),
    path('deleterole/<int:roleid>',views.Deleterole),
    path('updaterole/<int:roleid>',views.Updaterole),

    # Employees:
    path('viewemployees/', views.view_employees, name='viewemployees'),
    path('addemployee/', views.add_employee, name='addemployee'),
    path('updateemployee/<int:employee_id>/', views.update_employee, name='updateemployee'),
    path('deleteemployee/<int:employee_id>/', views.delete_employee, name='deleteemployee'),

        # User Login:
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('resetpasswordrequest/', views.reset_password_request, name='resetpasswordrequest'),
    path('validateotp/', views.validate_otp, name='validateotp'),
    path('resetpassword/', views.reset_password, name='resetpassword'),
]

