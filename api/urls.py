from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'users',views.UserInfoApi,basename='users')


""""
Here is we're using ViewSet classes rather than View classes, we actually don't need to design the URL configuration
so need put custome url becaese of  default  router concept
"""

urlpatterns = [
	url(r'',include(router.urls)),

]

