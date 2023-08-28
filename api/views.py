from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from blogapps.models import UserPost

@api_view(['GET'])
def api_routes(request):
    
    routes = [
        { 'GET': '/api/posts'},
        { 'GET': '/api/posts/id'},
    ]

    return Response(routes)

@api_view(['GET'])
def get_posts(request):
    posts = UserPost.objects.all()
    serializer = PostSerializer(posts, many=True)
    if(status.HTTP_200_OK == 200):
        return Response({'all_post':serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'status':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_post(request, pk):
    post = UserPost.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    if(status.HTTP_200_OK == 200):
        return Response({'selected_post':serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'status':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
    