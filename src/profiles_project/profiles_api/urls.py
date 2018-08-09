from django.conf.urls import url
from . import views

app_name = 'profiles_api'

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view())
]
