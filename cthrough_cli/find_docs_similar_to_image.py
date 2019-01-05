from api_handler import api_handler
import tabulate
from apis import find_docs_similar_to_image_api

def find_docs_similar_to_image(primary_image, list_of_docs, threshold=None, pretty=True):
	request_body = {
		"primary_image": primary_image
		"list_of_docs": list_of_docs,
		"threshold": threshold
	}

	response = api_handler(url, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
		return 1

	if len(response.get("data")) == 0:
		print ("No documnets similar to {} found".format(primary_image.get("name")))
		return 0

	if not pretty:
		print ("Documents similar to {}:".format(primary_image.get("name")))
		print ("\n")
		for doc in response.get("data"):
			print (doc.get("name"), doc.get("score"))
		return 0

	table_header = ["Document Name", "Similarity score"]
	table_body = []

	for doc in response.get("data"):
		table_body.append([doc.get("name"), doc.get("score")])

	print ("Documents similar to {}:".format(primary_image.get("name")))
	print ("\n")
	print (tabulate(table_body, table_header, tablefmt="orgtbl"))
	print ("\n")

	return 0

