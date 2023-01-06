from django.urls import path
from .views import StoreList, StoreDetail

urlpatterns = [
    path('stores/', StoreList.as_view()),
    path('stores/<int:pk>/', StoreDetail.as_view()),
]
