from django.urls import path
from . import views

urlpatterns = [
    
    path('operation_create/',views.Operations.as_view())
]
