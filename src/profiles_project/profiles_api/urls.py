from django.conf.urls import url
from django.conf.urls import include #for viewset

from rest_framework.routers import DefaultRouter #for viewset
from . import views

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
urlpatterns=[
url(r'^hello-view/',views.HelloApiView.as_view()),
url(r'',include(router.urls)) # empty string here so that url directs to this if initially specified not present
]
