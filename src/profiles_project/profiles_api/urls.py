from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'profiles_api'

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),

    # If django not found url, it start to find it in a router
    url(r'', include(router.urls))
]
