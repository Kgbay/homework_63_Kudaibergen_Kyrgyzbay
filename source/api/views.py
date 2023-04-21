from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from instagram_app.models import Post

from .serializers import PostSerializer


class PostView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Post.objects.all()
        serializer = PostSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailView(APIView):

    def get(self, request, pk=None):
        if pk:
            task = Post.objects.get(id=pk)
            serializer = PostSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        tasks = Post.objects.all()
        serializer = PostSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateView(APIView):

    def put(self, request, pk=None):
        task = Post.objects.get(id=pk)
        serializer = PostSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(APIView):

    def delete(self, request, pk=None):
        task = get_object_or_404(Post, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
