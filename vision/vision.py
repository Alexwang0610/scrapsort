import io

import base64
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import json
import argparse

def get_image_labels(file_path):
	credentials = GoogleCredentials.get_application_default()
	service = discovery.build('vision', 'v1', credentials=credentials)

	with open(file_path, 'rb') as image:
		image_content = base64.b64encode(image.read())
		service_request = service.images().annotate(body={
			'requests': [{
				'image': {
					'content': image_content.decode('UTF-8')
				},
				'features': [{
					'type': 'LABEL_DETECTION',
					'maxResults': 10
				}]
			}]
		})
		response = service_request.execute()
		print json.dumps(response, indent=4, sort_keys=True)


print get_image_labels("bottle.jpg")
