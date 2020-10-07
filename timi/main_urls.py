"""timi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
# from filebrowser.sites import site

from core import views
from timi import main_settings

urlpatterns = [
    # path('admin/filebrowser/', site.urls),
    # path('grappelli/', include('grappelli.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^upload/', views.upload),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^portfolio(?:/(?P<slug>[-\w]+))?/$', views.portfolio, name='portfolio'),
    url(r'^projects/$', views.projects, name='projects'),
    # url(r'^blog/$', views.index, name='blog'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]

urlpatterns += static(main_settings.MEDIA_URL, document_root=main_settings.MEDIA_ROOT)
