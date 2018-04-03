from django.urls import path

from . import views

urlpatterns = [
    path('generate', views.generateQuestionBank, name='generateQuestionBank'),
]