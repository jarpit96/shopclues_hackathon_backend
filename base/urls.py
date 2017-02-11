from django.conf.urls import url
import base.views
urlpatterns = [
    url(r'^getBasic/', base.views.getBasic, name="getBasic"),
    url(r'^getDetail/', base.views.getDetail, name="getDetail"),
]
