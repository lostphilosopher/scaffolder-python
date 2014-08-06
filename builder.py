import json

class Builder:
	'Optional class documentation string'
	def __init__(self, fileName, type):
		self.fileName = fileName
	        self.type = type
		self.templateDir = 'templates/'

	def getTemplate(self, type):
		if (not self.fileName or not self.type or not self.templateDir):
			return false
	
		with open (self.templateDir, "r") as contents:
			template=content.read().replace('%%NAME%%', self.fileName)

		return template

	def getFilePath(self):
		if (not self.fileName or not self.type):
			return false

		with open('paths.json', 'r') as content:
			pathsJson = content.read()
		
		pathsArray = json.loads(pathsJson)

		for types,paths in pathsArray.iteritems():
			if (types == self.type):
				for type,path in paths:
					print path
		return 'EXIT'
