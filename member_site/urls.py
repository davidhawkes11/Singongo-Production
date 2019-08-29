from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'member_site'
urlpatterns = [
    path('home', views.home, name='home'),
    path('search', views.search, name='search'),
    path(r'details/<name_display>', views.details, name='details'),
    path('not_found', views.file_not_found, name='file_not_found'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
