from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .serializers import ManagePostSerializer
from blogapps.models import UserPost

@api_view(['GET'])
def api_routes(request):
    
    routes = [
        { 'GET': '/api/posts'},
        { 'GET': '/api/posts/id'},
    ]

    return Response(routes)

@api_view(['GET', 'POST'])
def get_posts(request):
    if request.method == 'GET':
        posts = UserPost.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({'all_post':serializer.data}, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = ManagePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':status.HTTP_201_CREATED, "created" : serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def get_post(request, pk):
    try:
       post = UserPost.objects.get(id=pk)
    except UserPost.DoesNotExist:
        return Response({'status':status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post, many=False)
        if(status.HTTP_200_OK == 200):
            return Response({'selected_post':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = ManagePostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':status.HTTP_200_OK, "updated" : serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'status':status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    