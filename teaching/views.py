from django.http import HttpResponse
from django.shortcuts import render
from .models import Group
from .models import Student


def index(request):
  if request.method == "POST":
    name = request.POST.get("name")
    last_name = request.POST.get("last_name")
    phone_number = request.POST.get("phone_number")
    group_id = request.POST.get("group_id")
    student = Student.objects.create(name=name, last_name=last_name, phone_number=phone_number, group_id=group_id)
    
  edu_groups = Group.objects.all()
  edu_students = Student.objects.all()
  context = {"groups": edu_groups, "students": edu_students}

  return render(request, "index.html", context=context)



