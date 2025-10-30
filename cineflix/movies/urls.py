from django.urls import path

from . import views


#urlpattern not urls 
urlpatterns = [
    
    path('',views.HomeView.as_view(),name='home'),


]
         