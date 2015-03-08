#

class Entry:
	def __init__(self):
		self.code = """var f = 10;
var i;
for (i = 1; i <= f; i++) {
	console.log(i);
}"""

	#Return the user script
	def userScript (self):
		#return self.other
		return self.code
