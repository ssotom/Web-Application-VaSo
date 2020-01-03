"""telematica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.urls import include, re_path
from rest_framework import routers
from telematica.my_app import views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.views.generic import TemplateView

router = routers.SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('customers', views.CustomerViewSet)
router.register('comments', views.CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    url(r'^.*$', TemplateView.as_view(template_name='index.html'))
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
