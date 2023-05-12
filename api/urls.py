from django.urls import path 
from .views import StudentList, StudentDetail, BuildingList, BuildingDetail, RoomList, RoomDetail, KeyList, KeyDetail

urlpatterns = [
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('building/', BuildingList.as_view()),
    path('building/<int:pk>/', BuildingDetail.as_view()),
    path('room/', RoomList.as_view()),
    path('room/<int:pk>/', RoomDetail.as_view()),
    path('key/', KeyList.as_view()),
    path('key/<int:pk>/', KeyDetail.as_view()),
]
