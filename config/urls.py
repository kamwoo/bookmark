"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
    path('test/',template_test),
    path('kakao/', kakao_template),
    path('bookmark/', include('bookmark.urls')),
    # 1차 -> 2차 -> 3차
    # http://127.0.0.1/bookmark/?
    # http://127.0.0.1/중앙창구/외과
    # 1차 url을 설정해준것
    path('', index), # ''은 가장 상위
    # path(주소, 뷰, 주소의 별명)
]
