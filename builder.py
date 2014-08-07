import json

class Builder:
	'Optional class documentation string'
	def __init__(self, fileName, type):
		self.fileName = fileName
	        self.type = type
		self.templateDir = 'templates/'

	def getTemplate(self, type):
		if (not self.fileName or not self.type or not self.templateDir):
			return 'Error'
	
		with open (self.templateDir + type + '.txt', "r") as contents:
			template = contents.read().replace('%%NAME%%', self.fileName)

		return template

	def getFilePath(self):
		if (not self.fileName or not self.type):
			return 'Error'
		
		with open('paths.json', 'r') as content:
			pathsJson = content.read()
		
		pathsArray = json.loads(pathsJson)

		result = {}
		for types,paths in pathsArray.iteritems():
			if (types == self.type):
				for type,path in paths.iteritems():
					result[type] = path + self.fileName
		
				return result

		return 'Error'
