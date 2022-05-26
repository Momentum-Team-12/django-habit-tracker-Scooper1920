from django.urls import path
from api import views as api_views
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    
    path('api/', views.api_root),
    path('habits', api_views.HabitListView.as_view(), name='habit-list-api'),
    path('habits/<int:pk>/', api_views.HabitDetailView.as_view(), name='habit-detail-api'),
    path('users/', api_views.CustomUserListView.as_view(), name = 'user-list'),
    path('users/<int:pk>/', api_views.CustomUserDetailView.as_view(), name ='user-detail'),
    path('daterecords/', api_views.DateRecordView.as_view(), name = 'date-record-list'),
    path('daterecords/<int:pk>/',api_views.DateRecordDetailView.as_view(), name = 'date-record-detail'),
    
]



urlpatterns = format_suffix_patterns(urlpatterns)