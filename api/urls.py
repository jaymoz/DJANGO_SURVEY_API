from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.urlview),
    path('create-survey', views.CreateSurvey),
    path('active-survey', views.ActiveSurveys),
    path('survey-list', views.SurveyList),
    path('survey-detail/<str:pk>/', views.SurveyDetail),
    path('update-survey/<str:pk>/', views.UpdateSurvey),
    path('delete-survey/<str:pk>/', views.DeleteSurvey),
    path('create-question',views.CreateQuestion),
    path('question-list',views.QuestionList),
    path('update-question/<str:pk/', views.UpdateQuestion),
    path('delete-question/<str:pk/', views.DeleteQuestion),
    path('response',views.CreateResponse),
    path('response-detail/<str:pk>/', views.ResponseDetail),
    path('user-response/<str:id_user>/',views.GetUserResponse),
    path('update-response/<str:pk>/', views.UpdateResponse),
    path('delete-response/<str:pk>/', views.DeleteResponse),
    path('question-detail/<str:pk>/',views.QuestionDetail),
    path('create-choices',views.CreateChoice),
    path('choice-detail/<str:pk>/',views.ChoiceDetail),
    path('update-choice/<str:pk>/', views.UpdateChoice),
    path('delete-choice/<str:pk>/', views.DeleteChoice),

]