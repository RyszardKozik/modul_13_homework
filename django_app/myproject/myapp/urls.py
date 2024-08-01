from django.urls import path
from . import views

# Maps the root URL of the app to the index view
urlpatterns = [
    path('', views.index, name='index'),  
    # Add more paths here as you create more views
]
