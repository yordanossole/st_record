from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PersonSerializer
from .models import Person



# @api_view()
# def get_all_Students(request):
#     queryset = Student.objects.all()
#     serializer = studentSerializer(queryset, many=True, context={'request': request})

#     return HttpResponse()

class PersonList(APIView):
    def get(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PersonDetail(APIView):
    def get(self, request, id):
        person = get_object_or_404(Person, pk=id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    
    def put(self, request, id):
        person = get_object_or_404(Person, pk=id)
        serializer = PersonSerializer(person, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        person = get_object_or_404(Person, pk=id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
