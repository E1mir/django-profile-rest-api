from django.conf.urls import url
from profiles_api import views

app_name = 'profiles_api'

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view())
]
