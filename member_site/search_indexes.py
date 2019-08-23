import datetime
from haystack import indexes
from member_site.models import FileRec

class FileRecIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	name = indexes.CharField(model_attr='name')
	location = indexes.CharField(model_attr='location')
	file_type = indexes.CharField(model_attr='file_type')
	
	def get_model(self):
		return FileRec
