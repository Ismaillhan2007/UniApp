from django.urls import path
from . import views

urlpatterns = [
    path('universities/', views.university_list),
    path('universities/<int:pk>/', views.university_detail),
    path('universities/<int:uni_id>/faculties/', views.faculty_list),
    path('universities/<int:uni_id>/programs/', views.university_programs),
    path('programs/', views.program_list),
    path('search/', views.search),
    path('compare/', views.compare),
]