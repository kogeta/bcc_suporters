from django.urls import path

from . import views


app_name = 'donate'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('omikuji/', views.OmikujiView.as_view(), name="omikuji"),
    path('result', views.result_view, name='result'),
]