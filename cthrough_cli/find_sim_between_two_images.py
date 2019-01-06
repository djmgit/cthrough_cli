from .api_handler import api_handler
from tabulate import tabulate
from .apis import find_sim_between_two_images_api

def find_sim_between_two_images(img1, img2, pretty=True):
	request_body = {
		"img1": img1,
		"img2": img2
	}

	response = api_handler(find_sim_between_two_images_api, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
		return 1

	print ("Similarity score: {}".format(response.get("data").get("score")))
	return 0
	