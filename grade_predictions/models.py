from django.db import models
from django.contrib.auth.models import AbstractUser
from treenode.models import TreeNodeModel


# Create your models here.

class GrUser(AbstractUser):
    is_student = models.BooleanField(default=False)


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name()


class Career(models.Model):
    snies = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Subject(TreeNodeModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    careers = models.ManyToManyField(Career, related_name='careers')
    teachers = models.ManyToManyField(Teacher)

    treenode_display_field = 'name'

    def __str__(self):
        return self.name


class Student(GrUser):
    student_code = models.CharField(max_length=15, primary_key=True)
    enrolment_year = models.IntegerField()
    user = models.OneToOneField(
        GrUser, on_delete=models.CASCADE, primary_key=False,
        related_name='related_user')

    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='students')
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.student_code

    class Meta:
        verbose_name = 'Student'


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=50, default='Sin estado')
    status = models.IntegerField(default=0)




