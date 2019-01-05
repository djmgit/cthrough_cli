from api_handler import api_handler
import tabulate
from apis import find_sim_between_two_api

def find_sim_between_two(doc1, doc2, pretty):
	request_body = {
		"doc1": doc1,
		"doc2": doc2
	}

	response = api_handler(url, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
	else:
		print ("Similarity score: " + response.get("data").get("score"))
