"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from library_web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    # path('about/contact/', views.contact, name='contact'),
    path('login/', views.login , name='login'),
    path('signup/' , views.signup, name='signup'),
    path('book_details/<int:id>/', views.book_details, name='book_details'),
    path('search/', views.search, name='search'),
    path('download/', views.download_file, name='download_file'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
