from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.StudentSignupView.as_view(), name='signup'),
    path('login/', views.StudentLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/subject/<int:pk>', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('dashboard/subjects', views.SubjectListView.as_view(), name='subject_list'),
    path('dashboard/subjects/subscribe', views.subscribe_to_subject, name='subject_subscribe'),
    path('dashboard/subjects/unsubscribe/all', views.unsubscribe_from_all, name='subject_unsubscribe_all'),
    path('dashboard/subjects/unsubscribe/<int:subject_id>', views.unsubscribe_from_subject, name='subject_unsubscribe')
]


