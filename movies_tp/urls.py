from django.conf.urls import patterns, include, url
from tastypie.api import Api
from movies.api import MoviesResource, DirectorsResource, GenresResource

v1_api = Api(api_name='v1')
v1_api.register(MoviesResource())
v1_api.register(DirectorsResource())
v1_api.register(GenresResource())

urlpatterns = patterns('',
		url(r'^api/', include(v1_api.urls)),  # Api Endpoint for movies
)
