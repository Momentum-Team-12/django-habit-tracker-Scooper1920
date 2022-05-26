from django.contrib import admin
from django.urls import path
from api import views as api_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('habits', api_views.HabitListView.as_view(), name='habit-list-api'),
    path('habits/<int:pk>/', api_views.HabitDetailView.as_view(), name='habit-detail-api')
]

urlpatterns = format_suffix_patterns(urlpatterns)