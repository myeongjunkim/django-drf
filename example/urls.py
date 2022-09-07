from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),
    path("generic/books/", BooksAPIGenerics.as_view()),
    path("generic/book/<int:bid>/", BookAPIGenerics.as_view()),

    # 최종
    path("book/", include(router.urls)),

]



