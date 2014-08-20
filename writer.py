# Internal Imports
from builder import Builder

class Writer:
	'Optional class documentation string'
	def __init__(self, fileName, type):
		self.fileName = fileName
		self.type = type
	
	def make(self):
		builder = Builder(self.fileName, self.type)

		filePath = builder.getFilePath()

		if ('Error' in filePath):
			return filePath

		for type,path in builder.getFilePath().iteritems():
			file = open(path, 'w')
			file.write(builder.getTemplate(type))
			file.close()

		return 'SUCCESS!'


