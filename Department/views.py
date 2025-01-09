from django.shortcuts import render,redirect, get_object_or_404
from Department.models import Department,Roles
from django.contrib import messages

# Create your views here.
def home(request):
    data=Department.objects.filter(status=True)
    context={}
    context['department']= data
    return render(request,'index.html',context)

def createDepartment(request):
    if request.method == 'GET':
        return render(request,'createdepartment.html')
    else:
        n = request.POST['dept_name']
        d = request.POST['description']
        dept = Department.objects.create(dept_name=n, description =d)
        dept.save()
        return redirect('/')
    
def Deletedepartment(request, did):
    dept = Department.objects.get(dept_id = did)
    dept.status=False
    print(dept)
    print(dept.status)
    dept.save()
    return redirect('/')

# def updateDepartment(request, did):
#     if request.method == "GET":
#         d = Department.objects.filter(dept_id=did) 
#         context = {}
#         context['dept'] = d #in case if we use get
#         return render(request,'updatedeparment.html',context)
#     else:
#         dep = Department.objects.filter(dept_id = did)
#         # d is the queryset, on Queryset, we can call update and delete
#         n = request.POST['dept_name']
#         d = request.POST['description']
#         dep.update(dept_name=n, description =d)
#         return redirect('/')

def updateDepartment(request, did):
    if request.method == "GET":
        # Get a single department object
        d = get_object_or_404(Department, dept_id=did)
        context = {"dept": d}
        return render(request, 'updatedeparment.html', context)

    elif request.method == "POST":
        # Retrieve the object to update
        dep = Department.objects.filter(dept_id=did)

        # Fetch form data
        n = request.POST['dept_name']
        d = request.POST['description']

        # Update the department fields
        dep.update(dept_name=n, description=d)

        # Redirect to homepage or department list
        return redirect('/')
    

# View roles (only active)
def viewRole(request):
    data = Roles.objects.filter(status=True)
    context = {'roles': data}
    return render(request, 'viewrole.html', context)

# Add a role (only for admins)
def addRole(request):
    # user = Users.objects.get(username=request.user.username) if request.user.is_authenticated else None
    # if not user or not is_admin(user):
    #     messages.error(request, 'You do not have permission to perform this action.')
    #     return redirect('/')
    
    if request.method == 'GET':
        return render(request, 'addrole.html')
    else:
        n = request.POST['role_name']
        d = request.POST['description']
        Roles.objects.create(role_name=n, description=d)
        return redirect('/viewrole')

# Delete role (only for admins)
def Deleterole(request, roleid):
    # user = Users.objects.get(username=request.user.username) if request.user.is_authenticated else None
    # if not user or not is_admin(user):
    #     messages.error(request, 'You do not have permission to perform this action.')
    #     return redirect('/')
    
    role = Roles.objects.get(role_id=roleid)
    role.status = False
    role.save()
    return redirect('/viewrole')

# Update role (only for admins)
def Updaterole(request, roleid):
    # user = Users.objects.get(username=request.user.username) if request.user.is_authenticated else None
    # if not user or not is_admin(user):
    #     messages.error(request, 'You do not have permission to perform this action.')
    #     return redirect('/')
    
    r = Roles.objects.get(role_id=roleid)
    if request.method == 'GET':
        context = {'role': r}
        return render(request, 'updaterole.html', context)
    else:
        n = request.POST['role_name']
        r.description = request.POST['description']
        r.role_name = n
        r.save()
        return redirect('/viewrole')
