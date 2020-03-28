from django.conf.urls import url
from rest_framework import routers

from .views import(
    UserActivityView
)

router = routers.DefaultRouter()

router.register(
    'activity',
    UserActivityView,
    base_name='activity'
)

urlpatterns = []
urlpatterns += router.urls
