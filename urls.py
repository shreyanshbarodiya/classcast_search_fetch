from django.conf.urls import url
from rest_framework import routers
import views


urlpatterns = [
    url(r'^search/$', views.QuestionSearchAPIView.as_view(), name='search'),
    url(r'^search_function/$', views.search_function, name='search_function'),
    url(r'^search_without_data/$', views.QuestionSearchWithoutDataAPIView.as_view(), name='search_without_data'),
    url(r'^test/$', views.QuestionTestAPIView.as_view(), name='test'),
    # url(r'^challenge/$', views.QuestionChallengeAPIView.as_view(), name='challenge'),
    url(r'^gym/$', views.QuestionGymAPIView.as_view(), name='gym'),
		]   