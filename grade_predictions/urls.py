from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.StudentSignupView.as_view(), name='signup'),
    path('login/', views.StudentLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/subject/<int:pk>', views.SubjectDetailView.as_view(), name='subject_detail')
]


