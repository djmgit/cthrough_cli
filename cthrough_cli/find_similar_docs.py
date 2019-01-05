from .api_handler import api_handler
import tabulate
from .apis import find_similar_docs_api

def find_similar_docs(primary_doc, list_of_docs, threshold=None, pretty=True):
	request_body = {
		"primary_doc": primary_doc
		"list_of_docs": list_of_docs,
		"threshold": threshold
	}

	response = api_handler(find_similar_docs_api, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
		return 1

	if len(response.get("data")) == 0:
		print ("No documnets similar to {} found".format(primary_doc.get("name")))
		return 0

	if not pretty:
		print ("Documents similar to {}:".format(primary_doc.get("name")))
		print ("\n")
		for doc in response.get("data"):
			print (doc.get("name"), doc.get("score"))
		return 0

	table_header = ["Document Name", "Similarity score"]
	table_body = []

	for doc in response.get("data"):
		table_body.append([doc.get("name"), doc.get("score")])

	print ("Documents similar to {}:".format(primary_doc.get("name")))
	print ("\n")
	print (tabulate(table_body, table_header, tablefmt="orgtbl"))
	print ("\n")

	return 0

