from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Topic
from .serializers import TopicSerializer
from base.api import serializers
from rest_framework import status


@api_view(['GET', 'POST'])
def getTopics(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getTopic(request, pk):
    topic = Topic.objects.get(id=pk)
    if request.method == 'GET':
        serializer = TopicSerializer(topic, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
