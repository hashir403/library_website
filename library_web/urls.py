from django.contrib import admin
from django.urls import path
from library_web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    # path('about/contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('book_details/<int:id>/', views.book_details, name='book_details'),
    path('signup/' , views.signup, name= 'signup'),
    path('search/', views.search, name='search'),
     path('download_file/<int:id>/', views.download_file, name='download_file'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
