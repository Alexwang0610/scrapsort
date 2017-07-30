from firebase import firebase
import base64
import time

class Database:
	firebase = None
	version = 0.2
	databaseName = "recyclingData"

	def __init__(self):
		self.firebase = firebase.FirebaseApplication("https://smart-garbage-4ba99.firebaseio.com/", None)

	def write_result(self, imageFilePath, labels, isTrash, pickedRecyclingLabel):
		timestamp = int(time.time()) # Seconds since UNIX epoch
		image = open(imageFilePath, "rb")
		imagebase64 = base64.b64encode(image.read())
		data = {'image': imagebase64, 'labels': labels, 'isTrash' : isTrash, 'timestamp': timestamp, 'recyclingLabel': pickedRecyclingLabel, 'version': self.version}
		self.firebase.post(self.databaseName, data)
