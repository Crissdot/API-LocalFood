"""APILocalFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.user.views import Login, Logout, TokenInfoAbout

API_PREFIX = 'api/v1/'

schema_view = get_schema_view(
    openapi.Info(
        title="LocalFood API",
        default_version='v0.5',
        description="Documentación de la aplicación LocalFood",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="crissdotcontact@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(rf'^{API_PREFIX}swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(rf'^{API_PREFIX}swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(rf'^{API_PREFIX}redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(API_PREFIX + 'admin/', admin.site.urls),
    path(API_PREFIX + 'localfood/', include('apps.localfood.api.urls')),
    path(API_PREFIX + 'user/', include('apps.user.api.urls')),
    path(API_PREFIX + 'login/', Login.as_view()),
    path(API_PREFIX + 'logout/', Logout.as_view()),
    path(API_PREFIX + 'token/about/', TokenInfoAbout.as_view()),
    path(API_PREFIX + 'product/', include('apps.products.api.urls')),
] + static(API_PREFIX[0: len(API_PREFIX)-1] + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
