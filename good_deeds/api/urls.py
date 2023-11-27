from django.urls import include, path
from djoser import views
from rest_framework.routers import DefaultRouter

from .views import AdViewSet, CategoryViewSet, AdRequestViewSet, ApplicantListViewSet

app_name = 'api'

router = DefaultRouter()

router.register('ads', AdViewSet, basename='ads')
router.register('category', CategoryViewSet, basename='category')
router.register('ad_request', AdRequestViewSet, basename='ad_request')
router.register('applicant_list', ApplicantListViewSet, basename='applicant_list')

urlpatterns = [
    path('auth/token/login/', views.TokenCreateView.as_view(),
         name='login'),
    path('auth/token/logout/', views.TokenDestroyView.as_view(),
         name='logout'),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('', include(router.urls))
]
