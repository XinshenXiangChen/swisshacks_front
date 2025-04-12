from django.urls import path
from . import views

app_name = 'ui'

urlpatterns = [
    path('', views.home, name='home'),
    path('document/<int:doc_id>/', views.document_view, name='document'),
] 