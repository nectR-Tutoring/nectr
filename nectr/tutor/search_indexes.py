from haystack import indexes
from nectr.tutor.models import Tutor


class TutorIndex(indexes.SearchIndex, indexes.Indexable):
    pass
