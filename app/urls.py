from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('operation',views.operation,name='operation')
]
