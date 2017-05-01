from haystack import indexes
from nectr.tutor.models import Tutor


class TutorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    tutor = indexes.CharField(model_attr='user')

    def get_model(self):
        return Tutor
