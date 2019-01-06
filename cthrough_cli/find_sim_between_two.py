from .api_handler import api_handler
from tabulate import tabulate
from .apis import find_sim_between_two_api

def find_sim_between_two(doc1, doc2, pretty=True):
	request_body = {
		"doc1": doc1,
		"doc2": doc2
	}

	response = api_handler(find_sim_between_two_api, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
		return 1

	print ("Similarity score: {}".format(response.get("data").get("score")))
	return 0
