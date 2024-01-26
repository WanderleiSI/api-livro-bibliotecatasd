from rest_framework import viewsets
from livro.api import serializers
from livro import models

class LivroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivroSerializer
    queryset = models.Livro.objects.all()
