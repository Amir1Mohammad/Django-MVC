from django.conf.urls import url
from django.conf.urls import include

from . import views


urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
]
