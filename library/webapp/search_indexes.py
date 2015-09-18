from haystack import indexes
from webapp import models


class TitleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    author = indexes.IntegerField(model_attr='author')
    isbn = indexes.CharField(model_attr='isbn')
    dewey = indexes.CharField(model_attr='dewey')

    def get_model(self):
        return models.Readerware

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
