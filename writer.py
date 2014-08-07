from builder import Builder

class Writer:
	'Optional class documentation string'
	def __init__(self, fileName, type):
		self.fileName = fileName
		self.type = type
	
	def make(self):
		builder = Builder(self.fileName, self.type)

		for type,path in builder.getFilePath().iteritems():
			file = open(path, 'w')
			file.write(builder.getTemplate(type))
			file.close()

		return 'SUCCESS!'


