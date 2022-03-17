from django.urls import path

from tracking.views import dashboard

urlpatterns = [
    path('', dashboard, name='tracking-dashboard'),
]
