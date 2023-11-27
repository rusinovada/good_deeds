from django.db import transaction
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from drf_extra_fields.fields import Base64ImageField

from ads.models import Category, Ad, AdRequest, ApplicantList
from users.models import User


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        ]


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug'
        ]


class AdSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = [
            'id',
            'category',
            'author',
            'title',
            'description',
            'image'
        ]


class CreateAdSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    image = Base64ImageField()

    class Meta:
        model = Ad
        fields = [
            'id',
            'author',
            'category',
            'image',
            'title',
            'description'
        ]

    @transaction.atomic
    def create(self, validated_data):
        author = self.context.get('request').user
        ad = Ad.objects.create(author=author, **validated_data)
        return ad

    @transaction.atomic
    def update(self, instance, validated_data):
        ad = validated_data.pop('ad')
        self.create(ad, instance)
        instance.title = validated_data.pop('name')
        instance.text = validated_data.pop('text')
        if validated_data.get('image'):
            instance.image = validated_data.pop('image')
        instance.save()
        return instance

    @transaction.atomic
    def delete(self, instance):
        return super().delete(instance)

    def to_representation(self, instance):
        return AdSerializer(instance, context={
            'request': self.context.get('request')
        }).data


class AdRequestSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    ad = AdSerializer()

    class Meta:
        model = AdRequest
        fields = [
            'id',
            'user',
            'ad',
            'comment'
        ]

    @transaction.atomic
    def create(self, validated_data):
        author = self.context.get('request').user
        ad_request = AdRequest.objects.create(author=author, **validated_data)
        return ad_request


class ApplicantListSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    ad = AdSerializer()

    class Meta:
        model = ApplicantList
        fields = [
            'id',
            'ad',
            'user',
            'is_selected'
        ]


class ApplicantSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantList
        fields = [
            'id',
            'is_selected'
        ]

    def update(self, instance, validated_data):
        instance.is_selected = validated_data.get(
            'is_selected', instance.is_selected
        )
        instance.save()
        return instance
