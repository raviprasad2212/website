from django.shortcuts import render
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import GeeksSerializer
from .models import GeeksModel


# Create your views here.

from django.http import HttpResponse

def Course(request):
    return HttpResponse('Ravi Prasad')

# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = GeeksModel.objects.all()
	
	# specify serializer to be used
	serializer_class = GeeksSerializer
