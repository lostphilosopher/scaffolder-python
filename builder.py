# External Imports
import json # JSON parsing class

# Prepares associated sets of templates and file paths
# @param string fileName: Name of file being created
# @param string type: Type of file being created (examples: controller, model, view)
#
class Builder:
	'Builder -getTempate -getFilePath'
	def __init__(self, fileName, type):
		self.fileName = fileName
	        self.type = type
		self.templateDir = 'templates/' # Path to boiler plate content

	# Gets the boiler plate template text and makes necessary naming substitions
	# @param string type: Type of file being created (examples: controller, model, view)
	# @return string template: Text for file matching given type
	#
	def getTemplate(self, type):
		if (not self.fileName or not self.type or not self.templateDir):
			return 'Error'
	
		with open (self.templateDir + type + '.txt', "r") as contents:
			template = contents.read().replace('%%NAME%%', self.fileName)

		return template

	# Gets the path for a file of a given type
	# @return string result: File path
	#
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
