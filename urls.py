from django.conf.urls import url
from rest_framework import routers
import views


urlpatterns = [
    url(r'^search/$', views.QuestionSearchAPIView.as_view(), name='search'),
    url(r'^test/$', views.QuestionTestAPIView.as_view(), name='test'),
    url(r'^challenge/$', views.QuestionChallengeAPIView.as_view(), name='challenge')
    url(r'^gym/$', views.QuestionGymAPIView.as_view(), name='gym')
		]   