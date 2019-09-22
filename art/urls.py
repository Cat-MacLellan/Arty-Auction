from django.conf.urls import url, include
from .views import all_art

urlpatterns = [
    url(r'^$', all_art, name='art'),
]