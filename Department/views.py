from django.shortcuts import render,redirect
from Department.models import Department
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

def updateDepartment(request, did):
    if request.method == "GET":
        d = Department.objects.filter(dept_id=did) 
        context = {}
        context['department'] = d #in case if we use get
        return render(request,'updatedeparment.html',context)
    else:
        dep = Department.objects.filter(dept_id = did)
        # d is the queryset, on Queryset, we can call update and delete
        n = request.POST['dept_name']
        d = request.POST['description']
        dep.update(dept_name=n, description =d)
        return redirect('/')