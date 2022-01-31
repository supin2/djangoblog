"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


# 기본 url : http://localhost:8000/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # /blog 주소가 들어오면 blog 앱으로 처리를 넘김
    path("", RedirectView.as_view(url='/blog/', permanent=True)), # 기본 url로 들어올 시에 처리
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # JavaScript, CSS, image파일(Static 파일들)을 처리할 수 있도록 하는 세팅
