from django.urls import path

from . import views

#html-----view----url

#urlpattern not urls 
urlpatterns = [
    
    path('',views.HomeView.as_view(),name='home'),

    path('movie-list/',views.MoviesListView.as_view(),name='movie-list'),

    path('movie-create/',views.MovieCreateView.as_view(),name='movie-create'),

    # path('movie-details/<int:id>',views.MovieDetailsView.as_view(),name='movie-details'),
    # int id... vere reetiyill id kodukkunne reeti annu

    path('movie-details/<str:uuid>',views.MovieDetailsView.as_view(),name='movie-details'),

    path('movie-edit/<str:uuid>',views.MovieEditView.as_view(),name='movie-edit'),
    
    path('movie-delete/<str:uuid>',views.MovieDeleteView.as_view(),name='movie-delete'),

]
         