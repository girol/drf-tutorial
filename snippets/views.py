from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

###############################
# Tutorial Parte 3.3 - Using generic class-based views
###############################


class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
