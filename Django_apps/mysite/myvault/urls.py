from django.urls import path

from . import views

app_name = 'myvault'
urlpatterns = [
    path('', views.home, name='home'),
    path('new_cred/', views.new_cred, name='new_cred'),
    path('add_credential/', views.add_credential, name='add_credential'),
    path('<str:app_id>/', views.reveal, name='reveal'),
    path('<str:app_id>/delete_cred/', views.delete_cred, name='delete_credential'),

    
    


]