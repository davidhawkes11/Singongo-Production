from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'member_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='process_login'),
    path('signup', views.sign_up, name='signup'),
    path('process', views.process_signup, name='process_signup'),
    path('home', views.home, name='home'),
    path('search', views.search, name='search'),
    path(r'details/<name_display>', views.details, name='details'),
    path('logout', views.logout, name='logout'),
    path('signupsuccess', views.signup_success, name='signup_success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
