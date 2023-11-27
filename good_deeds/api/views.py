from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from ads.models import Category, Ad, AdRequest, ApplicantList

from .pagination import CustomPagination
from .permissions import IsAuthorOrAdminOrReadOnly
from .serializers import (
    CategorySerializer, AdSerializer,
    CreateAdSerializer, AdRequestSerializer,
    ApplicantListSerializer, ApplicantSelectionSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    pagination_class = None
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AdViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrAdminOrReadOnly]
    pagination_class = CustomPagination
    queryset = Ad.objects.all()
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AdSerializer
        return CreateAdSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context


class AdRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AdRequestSerializer

    def get_queryset(self):
        return AdRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ApplicantListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrAdminOrReadOnly]
    serializer_class = ApplicantListSerializer

    def get_queryset(self):
        return ApplicantList.objects.filter(ad=self.request.ad)

    def get_serializer_class(self):
        if self.action == 'update':
            return ApplicantSelectionSerializer
        return ApplicantListSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.is_selected = True
        instance.save()
