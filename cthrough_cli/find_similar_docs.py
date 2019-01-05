from api_handler import api_handler
import tabulate
from apis import find_similar_docs_api

def find_similar_docs(primary_doc, list_of_docs, threshold=None, pretty=True):
	request_body = {
		"primary_doc": primary_doc
		"list_of_docs": list_of_docs
	}

	response = api_handler(url, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
		return 1
	