from django.db import models


# Model for directors
class Directors(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
		db_table = 'directors'


# Model for Genre
class Genres(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'genres'
		ordering = ('name',)


# Model for Movies
class Movies(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(Directors)
    genre = models.ManyToManyField(Genres)
    _99popularity = models.IntegerField()
    imdb_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
    	db_table = 'movies'
        ordering = ('name',)  # Default Ordering
