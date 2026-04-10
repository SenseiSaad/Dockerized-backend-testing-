from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('archives/', views.ArchiveEntryListView.as_view(), name='entry-list'),
    path('archives/new/', views.ArchiveEntryCreateView.as_view(), name='entry-create'),
    path('register/', views.register, name='register'),
]
