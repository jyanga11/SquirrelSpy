"""
URL configuration for SquirrelSpy project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import SquirrelViewSet, UserViewSet, SightingViewSet, UserRegistrationView, UserLoginView

router = DefaultRouter()
router.register(r'squirrels', SquirrelViewSet, 'Squirrels')
router.register(r'sightings', SightingViewSet, 'Sightings')
router.register(r'users', UserViewSet, 'Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='Register'),
    path('login/', UserLoginView.as_view(), name='Login'),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
