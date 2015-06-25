from django.conf.urls import patterns, include, url
from movies.api import MoviesResource

# Load MoviesResource Object
movies_resource = MoviesResource()

urlpatterns = patterns('',
		url(r'^api/', include(movies_resource.urls)),  # Api Endpoint /api/movies
)
