from django.contrib import admin
from django.urls import path
from shift_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.generate_schedule, name='generate_schedule'),
    path('result/', views.schedule_result, name='schedule_result'),
]
