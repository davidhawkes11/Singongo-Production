from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from haystack.views import SearchView, search_view_factory
from haystack.forms import SearchForm

from . import views

app_name = 'member_site'
urlpatterns = [
    url(r'^home/', search_view_factory(view_class=SearchView, template='search/search.html', form_class=SearchForm), name='haystack_search'),
    path(r'details/<name_display>', views.details, name='details'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
