from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from models import Movies, Directors, Genres


# Director Resource
# It is not exposed it is currently used only for relation
class DirectorsResource(ModelResource):
    class Meta:
        queryset = Directors.objects.all()
        excludes = ['id']
        include_resource_uri = False
        filtering = {"name": ALL}

    # Only return name
    def dehydrate(self, bundle):
        return bundle.data['name']


# Genre Resource
# It is not exposed it is currently used only for relation
class GenresResource(ModelResource):
    class Meta:
        queryset = Genres.objects.all()
        excludes = ['id']
        include_resource_uri = False
        filtering = {"name": ALL}

    # Only return name
    def dehydrate(self, bundle):
        return bundle.data['name']


# Movies Resource
# This resource is exposed via api endpoint 'movies'
class MoviesResource(ModelResource):
    director = fields.ForeignKey(DirectorsResource, 'director', full=True)  # One to one relationship for director
    genre = fields.ToManyField(GenresResource, 'genre', null=True, blank=True, full=True)  # One to Many relationship for genre

    class Meta:
        queryset = Movies.objects.all()
        resource_name = 'movies'  # Resource name/ API endpoint
        ordering = ['_99popularity', 'imdb_score']  # Order by _99popularity and imdb_score
        # Filtering by name, director, 99populatity and imdb_score
        filtering = {
        	"name": ALL,
        	"director": ALL_WITH_RELATIONS,
        	"genre": ALL_WITH_RELATIONS,
        	"_99popularity": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        	"imdb_score": ['exact', 'range', 'gt', 'gte', 'lt', 'lte']}
        excludes = ['updated_at', 'created_at']	 # Exclude dates from the response
        authentication = BasicAuthentication()  # Basic Authentication TODO: Custom Authentication
        authorization = DjangoAuthorization()  # Django Authorization TODO: Custom Roles based Authorization
