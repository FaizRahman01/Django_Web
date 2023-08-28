from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    return Response(serializer.data)

@api_view(['GET'])
def get_post(request, pk):
    post = UserPost.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)