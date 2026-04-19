from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    # Agregamos .order_by('id') aquí abajo:
    queryset = Movie.objects.all().order_by('id') 
    serializer_class = MovieSerializer