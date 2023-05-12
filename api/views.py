from rest_framework import generics

from .models import Student, Building, Room, Key
from .serializers import StudentSerializer, BuildingSerializer, RoomSerializer, KeySerializer

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer 
    queryset = Student.objects.all()


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer 
    queryset = Student.objects.all()


class BuildingList(generics.ListCreateAPIView):
    serializer_class = BuildingSerializer 
    queryset = Building.objects.all()


class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildingSerializer 
    queryset = Building.objects.all()


class RoomList(generics.ListCreateAPIView):
    serializer_class = RoomSerializer 

    def get_queryset(self):
        queryset = Room.objects.all()
        building = self.request.query_params.get('building')
        if building is not None:
            queryset = queryset.filter(roomBuilding=building)
        return queryset


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer 
    queryset = Room.objects.all()


class KeyList(generics.ListCreateAPIView):
    serializer_class = KeySerializer 
    queryset = Key.objects.all()


class KeyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KeySerializer 
    queryset = Key.objects.all()