from django.shortcuts import render,redirect
from crudapp.models import Student
from crudapp.forms import StudentForm
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
import csv

def read(request):
    # Retrieve the search query
    q = request.GET.get('q', '')  # Default to an empty string

    # Filter the queryset based on the search query
    student_list = Student.objects.filter(
        Q(name__icontains=q) |
        Q(city__icontains=q) |
        Q(course__icontains=q)
    )

    # Paginate the results (10 students per page)
    paginator = Paginator(student_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the page object and query to the template
    return render(request, 'apps/result.html', {'s': page_obj, 'q': q})
# def read(request,):
#     q=request.GET.get('q') if request.GET.get('q')!=None else ''
#     student=Student.objects.filter(
#         Q(name__icontains=q) |
#         Q(city__icontains=q) |
#         Q(course__icontains=q)
#         )
#     return render(request,'apps/result.html',{'s':student})
def insert(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/success')
    return render(request,'apps/insert.html',{'form':form})
def success(request):
    return render(request,'apps/success.html')
def delete(request,id):
    s=Student.objects.get(id=id)
    if request.method=='POST':
        s.delete()
        return redirect('read')
    context={'student':s}
    return render(request,'apps/delete.html',context)
def update(request,id):
    stud=Student.objects.get(id=id)
    form=StudentForm(instance=stud)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=stud)
        if form.is_valid():
            form.save()
            return redirect('read')
    context={'s':stud,'form':form}
    return render(request,'apps/update.html',context)
def contact(request):
    return render(request,'apps/contact.html')
def download(request):
    response=HttpResponse(content_type='text/csv')
    response['content-Disposition']='attachment;filename=students_record.csv'
    student=Student.objects.all()
    writer=csv.writer(response)
    writer.writerow(['NO','NAME','MOBILE','CITY','COURSE'])
    for i in student:
        writer.writerow([i.no,i.name,i.mobile,i.city,i.course])
    return response





# Create your views here.
