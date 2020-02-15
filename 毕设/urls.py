"""databasetest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from movie.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('banner.html/', banner),
    path('layer.html/', layer),
    path('films/', films),
    path('layer.html/', layer),
    path('login.html/', login),
    path('register.html/', register),
    path('tab_desc.html/', tab_desc),
    path('tab_celebrity.html/', tab_celebrity),
    path('tab_img.html/', tab_img),
    path('buy_ticket/', buy_ticket),
    path('select_seat/', select_seat),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

