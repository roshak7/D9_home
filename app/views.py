from rest_framework import generics

from app.serializers import AuthorSerializer
from app.models import Author


class AuthorList(generics):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class RetrievenAuthorView(generics.RetrievenUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_feilds = ['id']