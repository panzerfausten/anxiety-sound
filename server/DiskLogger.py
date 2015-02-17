class DiskLogger:
	def __init__(self):
		self.route = "data.txt"
	def write(self,vals):
		_lineToWrite = ",".join(vals)
		with open(self.route, "a") as _FILE:
			_FILE.write("%s\n" %(_lineToWrite ))
			_FILE.close()
