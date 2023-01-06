from django.urls import path
from .views import CountryView, StateView, CityView, CountryDetailView, StateDetailView, CityDetailView

urlpatterns = [
    path('countries/', CountryView.as_view()),
    path('states/', StateView.as_view()),
    path('cities/', CityView.as_view()),
    path('countries/<int:pk>/', CountryDetailView.as_view()),
    path('states/<int:pk>/', StateDetailView.as_view()),
    path('cities/<int:pk>/', CityDetailView.as_view()),

]
