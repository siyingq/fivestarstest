from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), #1
    path('sections/', views.ParliamentRecordListView.as_view(), name='sections'),

]

'''
using #1 allows us to link our home page from any other page by
creating the following link in the template:
<a href="{% url 'index' %}">Home</a>

'''