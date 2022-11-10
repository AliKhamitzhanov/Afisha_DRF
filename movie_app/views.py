from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewsSerializers, \
    DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer
from .models import Director, Movie, Review


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class MoviesReviewListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewsSerializers


class DirectorModelViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination


class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination


@api_view(['GET'])
def movies_review_views(request):
    movie_ = Movie.objects.all()
    serializer = MovieReviewsSerializers(movie_, many=True)
    return Response(data=serializer.data)


# @api_view(['GET', "POST"])
# def director_views(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(data=serializer.data)
#     serializer = DirectorValidateSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                         data={"error": serializer.errors})
#     else:
#         director = Director.objects.create(
#             name=request.data.get('name', '')
#         )
#         director.save()
#         return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def director_details_views(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'error': '404'})
#     if request.method == 'GET':
#         serializer = DirectorSerializer(director)
#         return Response(data=serializer.data)
#     elif request.method == "PUT":
#         director.name = request.data.get('name', '')
#         director.save()
#         return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)
#     elif request.method == "DELETE":
#         director.delete()
#         return Response(data={'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def movie_views(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data)
#     serializer = MovieValidateSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                         data={"error": serializer.errors})
#     else:
#         movies = Movie.objects.create(
#             title=request.data.get('title', ''),
#             description=request.data.get('description', ''),
#             duration=request.data.get('duration'),
#             director_id=request.data.get('director')
#         )
#         movies.save()
#         return Response(data=MovieSerializer(movies).data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details_views(request, id):
#     try:
#         movies = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'error': '404'})
#     if request.method == 'GET':
#         serializer = MovieSerializer(movies)
#         return Response(data=serializer.data)
#     elif request.method == 'PUT':
#         movies.title = request.data.get('title', '')
#         movies.description = request.data.get('description', '')
#         movies.duration = request.data.get('duration')
#         movies.director_id = request.data.get('director_id')
#         movies.save()
#         return Response(data=MovieSerializer(movies).data, status=status.HTTP_201_CREATED)
#     elif request.method == "DELETE":
#         movies.delete()
#         return Response(data={'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def review(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(data=serializer.data)
#     serializer = DirectorValidateSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                         data={"error": serializer.errors})
#     else:
#         reviews = Review.objects.create(
#             text=request.data.get('text'),
#             stars=request.data.get('stars'),
#             movie_id=request.data.get('movie')
#         )
#         reviews.save()
#         return Response(ReviewSerializer(reviews).data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', "PUT", "DELETE"])
# def review_details_views(request, id):
#     try:
#         reviews = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'error': '404'})
#     if request.method == "GET":
#         serializer = ReviewSerializer(reviews)
#         return Response(data=serializer.data)
#     elif request.method == "PUT":
#         reviews.text = request.data.get('text', '')
#         reviews.stars = request.data.get('stars', '')
#         reviews.movie_id = request.data.get('movie_id', '')
#         reviews.save()
#         return Response(data=ReviewSerializer(reviews).data, status=status.HTTP_201_CREATED)
#     elif request.method == "DELETE":
#         reviews.delete()
#         return Response(data={'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)