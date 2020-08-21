from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.views.generic import CreateView, FormView, DetailView, ListView
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.views import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.conf import settings

# Create your views here.

from . import forms
from .models import GrUser, Student, Subject, Career


def index(request):
    return render(request, 'grade_predictions/index.html')


class StudentSignupView(CreateView):
    model = Student
    form_class = forms.StudentSignupForm
    template_name = 'grade_predictions/students/auth/signup.html'
    success_url = '/login'

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
    success_url = '/dashboard'

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


@login_required(login_url=settings.STUDENT_LOGIN_URL)
def dashboard(request):

    return render(request, 'grade_predictions/students/dashboard/index.html', {
        'materias': True
    })


class SubjectDetailView(LoginRequiredMixin, DetailView):
    login_url = settings.STUDENT_LOGIN_URL
    model = Subject
    template_name = 'grade_predictions/subjects/detail.html'


class SubjectListView(LoginRequiredMixin, ListView):
    login_url = settings.STUDENT_LOGIN_URL
    model = Subject
    template_name = 'grade_predictions/subjects/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {'careers': Career.objects.all()}

        return super(SubjectListView, self).get_context_data(**context)

    def get_queryset(self):
        filters = self.request.GET
        subjects = Subject.objects

        if 'query' in filters and filters['query'] is not None:
            subjects = subjects.filter(name__contains=filters['query'])

        if 'career[]' in filters and len(filters['career[]']):
            subjects = subjects.filter(careers__careers__id__in=filters['career[]'])

        print(subjects.all(), filters)

        return subjects.all()


@login_required(login_url=settings.STUDENT_LOGIN_URL)
def subscribe_to_subject(request):
    if request.method == 'POST':
        data = request.POST
        st = Student.objects.get(user_id=request.user.id)
        subject = Subject.objects.get(id=data['subject_id'])
        st.subjects.add(subject)
        st.save()

        return redirect(reverse('dashboard'))
    else:
        return HttpResponse('', status=404)


@login_required(login_url=settings.STUDENT_LOGIN_URL)
def unsubscribe_from_all(request):
    st = Student.objects.get(user_id=request.user.id)
    st.subjects.clear()
    st.save()

    return redirect(reverse('dashboard'))


@login_required(login_url=settings.STUDENT_LOGIN_URL)
def unsubscribe_from_subject(request, subject_id):
    st = Student.objects.get(user_id=request.user.id)
    st.subjects.set(st.subjects.exclude(id=subject_id))
    st.save()

    return redirect(reverse('dashboard'))


@login_required(login_url=settings.STUDENT_LOGIN_URL)
def view_grades(request, subject_id=''):

    subjects = Student.objects.get(user=request.user).subjects.all()
    context = {'grades': True}
    if subject_id:
        context['subject'] = Subject.objects.get(id=subject_id)

    context['subjects'] = subjects

    if request.method == 'POST':
        grade = request.POST['grade']

        if subject_id:
            context['subject'].grade_set.create(subject=context['subject'],
                                                student=request.user.related_user,
                                                value=grade)

    return render(request, 'grade_predictions/students/dashboard/grades.html', context)


@login_required(login_url=settings.STUDENT_LOGIN_URL)
def logout(request):
    user_logout(request)
    return redirect('/login')



