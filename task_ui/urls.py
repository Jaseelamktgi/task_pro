from django.urls import path, include
from task_ui import views

urlpatterns = [
    path('', views.home, name='home'),

]
