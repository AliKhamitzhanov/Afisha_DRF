from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieReviewsSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=30)

    def velidate_director_id(self, director_id):
        if Director.objects.filter(id=director_id).count() == 0:
            raise ValidationError(f"Director with id={director_id} not found!")
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=3, max_length=30)
    movie = serializers.IntegerField(min_value=1, max_value=24, allow_null=True)
    stars = serializers.IntegerField()

    def validate_reviews_id(self, reviews_id):
        if Review.objects.filter(id=reviews_id).count() == 0:
            raise ValidationError(f"Reviews with id={reviews_id} not found!")
        return


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField(allow_null=True)

    def validate_movie_id(self, movie_id):
        if Movie.objects.filter(id=movie_id).count() == 0:
            raise ValidationError(f"Movie with id={movie_id} not found!")
        return movie_id