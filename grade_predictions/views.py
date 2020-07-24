from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.views.generic import CreateView, FormView, DetailView
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.views import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

from . import forms
from .models import GrUser, Student, Subject


class StudentSignupView(CreateView):
    model = Student
    form_class = forms.StudentSignupForm
    template_name = 'grade_predictions/students/auth/signup.html'
    success_url = '/student/login'

    def form_valid(self, form):

        if not form.is_valid():
            return super(StudentSignupView, self).form_valid(form)
        self.object = form.save()

        self.object.user.username = self.object.student_code
        self.object.user.is_student = True

        self.object.user.save()

        return HttpResponseRedirect(self.get_success_url())


class StudentLoginView(FormView):
    template_name = 'grade_predictions/students/auth/login.html'
    form_class = forms.StudentLoginForm
    success_url = '/student/dashboard'

    def form_valid(self, form):
        try:
            student = Student.objects.get(pk=form.cleaned_data.get('student_code'))
            if student is not None:
                user = authenticate(username=form.cleaned_data.get('student_code'),
                                    password=form.cleaned_data.get('password'))

                if user is not None:
                    login(self.request, user)

                    return HttpResponseRedirect(self.success_url)

            form.add_error('password', 'La contraseña es inválida')
            return self.form_invalid(form)

        except ObjectDoesNotExist:
            form.add_error('student_code', 'No se encontró un estudiante con éste código')
            return self.form_invalid(form)


@login_required()
def dashboard(request):

    return render(request, 'grade_predictions/students/dashboard/index.html', {
        'materias': True
    })



class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'grade_predictions/subjects/detail.html'


@login_required()
def logout(request):
    user_logout(request)
    return redirect('/student/login')



