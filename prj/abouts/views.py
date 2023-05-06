from .models import Post
from .serializers import PostSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from rest_framework import viewsets


# class PostList(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True) # 여러 개 객체 serialization 위해 many=true
#         pagination = PostPaigination
#         return Response(serializer.data)
    
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.data) # 사용자의 입력 데이터
#         if serializer.is_valid(): # 유효성 검사
#             serializer.save() #저장
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostPagination(PageNumberPagination):
    page_size=6

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination