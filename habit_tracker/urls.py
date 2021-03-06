"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from habit import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('accounts/', include('registration.backends.simple.urls'), name ='login'),
    path("accounts/logout/",views.log_out, name ='log_out'),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include("api.urls")),

    path("",views.list_habits, name ='list_habits' ),
    path('habit/<int:pk>',views.habit_detail, name='habit_detail'),
    path('habit/new',views.add_habit, name='add_habit'),
    path('habit/<int:pk>/delete',views.delete_habit, name='delete_habit'),
    path('habit/<int:pk>/edit',views.edit_habit, name='edit_habit'),
    
    
    #right now i am able to log out by clicking the logout button but it doesn't go to the login
]
