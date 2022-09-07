from rest_framework import viewsets, permissions, status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

from .models import *
from .serializers import *



############################################################################
####################################FBV#####################################
############################################################################


@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        # 쿼리셋으로 가져올때는 many=True 옵션 넣기
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = BookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            # 모델 시리얼라이저의 기본 create 함수가 동작
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        

@api_view(['GET'])
def bookAPI(request, bid):
    book = get_object_or_404(Book, bid = bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status = status.HTTP_200_OK)


############################################################################
####################################CBV#####################################
############################################################################


class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        # 쿼리셋으로 가져올때는 many=True 옵션 넣기
        return Response(serializer.data, status = status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            # 모델 시리얼라이저의 기본 create 함수가 동작
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid = bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status = status.HTTP_200_OK)


############################################################################
####################################Mixins##################################
############################################################################

class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs): 
        return self.update(request, *args, **kwargs) 
    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs) 



############################################################################
###################################Generics#################################
############################################################################


class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'



############################################################################
###################################ViewSet##################################
############################################################################

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer