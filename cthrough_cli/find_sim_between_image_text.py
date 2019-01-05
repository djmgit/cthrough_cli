from .api_handler import api_handler
import tabulate
from .apis import find_sim_between_image_text_api

def find_sim_between_image_text(img, doc, pretty=True):
	request_body = {
		"img": img,
		"doc": doc
	}

	response = api_handler(find_sim_between_image_text_api, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
		return 1

	print ("Similarity score: " + response.get("data").get("score"))
	return 0
	