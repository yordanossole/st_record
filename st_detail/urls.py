from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonList.as_view()),
    path('<int:id>', views.PersonDetail.as_view()),
]