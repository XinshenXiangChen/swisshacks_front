from django.urls import path
from . import views

app_name = 'ui'

urlpatterns = [
    path('', views.home, name='home'),
    path('document/1/', views.passport, name='passport'),
    path('document/2/', views.client_profile, name='client_profile'),
    path('document/<int:doc_id>/', views.document, name='document'),
] 