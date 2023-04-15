import re

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title, User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role')


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User
        read_only_fields = ('role',)


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    title = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == 'POST'
            and Review.objects.filter(title=title, author=author).exists()
        ):
            raise ValidationError('Может существовать только один отзыв!')
        return data

    def validate_score(self, value):
        if 0 > value > 11:
            raise serializers.ValidationError('Оценка по 10-бальной шкале!')
        return value

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('author', 'pub_date', 'id')


class TitlesSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )

    class Meta:
        model = Title
        fields = '__all__'


class ReadOnlyTitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(
        source='reviews__score__avg', read_only=True
    )
    genre = GenresSerializer(many=True)
    category = CategoriesSerializer()

    class Meta:
        model = Title
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField(
        required=True,
    )
    username = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = (
            'username',
            'confirmation_code'
        )


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
    )
    email = serializers.EmailField(
        max_length=200,
    )

    def validate_username(self, value):
        if value.lower() == "me":
            raise serializers.ValidationError("Username 'me' is not valid")
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                "Неверный формат имени."
            )
        return value

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        if User.objects.filter(email=email, username=username).exists():
            return data
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Пользоваиель с таким email уже существует"
            )
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                "Пользователь с таким username уже существует"
            )
        return data

    class Meta:
        fields = ("username", "email")
        model = User
