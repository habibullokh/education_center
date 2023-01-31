from django.db import models

# Create your models here.

class EducationCenter(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateField(auto_now_add=True)
  
  def __str__(self):
      return self.name
  

class Course(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  center = models.ForeignKey(EducationCenter, on_delete=models.CASCADE)
  
class Group(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  center = models.ForeignKey(Course(), on_delete=models.CASCADE)
  def __str__(self):
      return self.name
  

class Teacher(models.Model):
  def __str__(self):
      return self.name
  name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=20)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
class Student(models.Model):
  def __str__(self):
      return f"{self.last_name} - {self.name} and his phone number {self.phone_number}, group is {self.group}"
        
  name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=20)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)