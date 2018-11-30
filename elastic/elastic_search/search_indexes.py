import datetime
from haystack import indexes
from elastic_search import models


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    customer_name = indexes.CharField(model_attr='customer_name')
    order_date = indexes.DateTimeField(model_attr='order_date')

    def get_model(self):
        return models.SalesDetails

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(order_date__lte=datetime.datetime.now())