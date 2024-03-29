"""
URL configuration for DRF_REST_TASK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
# below import for token authentication
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
# Creating Router Object
router = DefaultRouter()

# Register Product and categories with Router 
router.register('categories',views.CategoriesViewSet,basename='Categories')
# router.register('Products',views.ProductsViewSet,basename='Products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include('api.urls')),
    path('viewset/',include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # for session Authentication endpoint for browser login logout
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # for Token Authentication Endpoint to generate token
    # path('gettoken/',obtain_auth_token)
    # enpoint for simple jwt
    # path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    # path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),

] 

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
