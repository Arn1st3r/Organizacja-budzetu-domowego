"""projekt URL Configuration

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
from django.conf import settings

from django.contrib import admin
from budzet_domowy.views import statistics_view;
from django.conf.urls.static import static
from budzet_domowy.views import wydatki_utworz_widok;


from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',statistics_view, name='home'),
    path('wydatki/', wydatki_utworz_widok, name='wydatki'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Admin panel"
admin.site.site_title = "Admin panel"