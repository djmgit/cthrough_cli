from api_handler import api_handler
import tabulate
from apis import find_images_similar_to_doc_api

def find_similar_docs(primary_doc, list_of_images, threshold=None, pretty=True):
	request_body = {
		"primary_doc": primary_doc
		"list_of_images": list_of_images,
		"threshold": threshold
	}

	response = api_handler(find_images_similar_to_doc_api, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
		return 1

	if len(response.get("data")) == 0:
		print ("No documnets similar to {} found".format(primary_doc.get("name")))
		return 0

	if not pretty:
		print ("Images similar to {}:".format(primary_doc.get("name")))
		print ("\n")
		for img in response.get("data"):
			print (img.get("name"), img.get("score"))
		return 0

	table_header = ["Image Name", "Similarity score"]
	table_body = []

	for img in response.get("data"):
		table_body.append([img.get("name"), img.get("score")])

	print ("Documents similar to {}:".format(primary_doc.get("name")))
	print ("\n")
	print (tabulate(table_body, table_header, tablefmt="orgtbl"))
	print ("\n")

	return 0

