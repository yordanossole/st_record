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
        try:
            queryset = Person.objects.all()
            serializer = PersonSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            return Response({'error': 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = PersonSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response({'error': 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class PersonDetail(APIView):
    def get(self, request, id):
        try:
            person = get_object_or_404(Person, pk=id)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except Exception:
            return Response({'error': 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, id):
        try:
            person = get_object_or_404(Person, pk=id)
            serializer = PersonSerializer(person, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception:
            return Response({'error': 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, id):
        try:
            person = get_object_or_404(Person, pk=id)
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({'error': 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NotFound(APIView):
    def get(self, request):
        return Response({'error': "Page not found."}, status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        return Response({'error': "Page not found."}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request):
        return Response({'error': "Page not found."}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request):
        return Response({'error': "Page not found."}, status=status.HTTP_404_NOT_FOUND)    