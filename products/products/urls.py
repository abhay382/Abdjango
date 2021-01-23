"""products URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from kalpanapaper import views

urlpatterns = [
path("",views.index,name='shop'),
    path('admin/', admin.site.urls),
    path('kalpanapaper/',include('kalpanapaper.urls')),
    path('shop/', include('shop.urls')),
    path('bag/', include('bag.urls')),
    path('box/', include('box.urls')),
    path('cards/', include('cards.urls')),
    path('gift/', include('gift.urls')),
    path('journal/', include('journal.urls')),
    path('papers/', include('papers.urls')),
    path('star/', include('star.urls')),
    path('stationary/', include('stationary.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
