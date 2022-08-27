from django.urls import path

from . import views

# app_name = 'quiz'
urlpatterns = [
    path('', views.QuizListView.as_view(), name='quiz_list'),
    path('<int:pk>/', views.QuizDetailView.as_view(), name='quiz_detail'),    
    path('<int:quiz_id>/submit/', views.submitView, name='submit'),
    path('<int:quiz_id>/<int:submission_id>/showresult/', views.show_quiz_result, name='show_quiz_result'),
 ] 
 