from .api_handler import api_handler
import tabulate
from .apis import find_similar_pairs_api

def find_similar_pairs(list_of_docs, pretty=True):
	request_body = {
		"list_of_docs": list_of_docs
	}

	response = api_handler(find_similar_pairs_api, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
		return 1

	if not pretty:
		print ("Similarity scores for each pair of documents: ")
		print ("\n")
		for pair in response.get("data"):
			print (pair.get("docs")[0], pair.get("docs")[1], pair.get("score"))
		print ("\n")
		return 0

	table_header = ["Document Name", "Document Name", "Similarity score"]
	table = []

	for pair in response.get("data"):
		table.append([pair.get("docs")[0], pair.get("docs")[1], pair.get("score")])

	print ("Similarity scores for each pair of documents: ")
	print ("\n")
	print (tabulate(table_body, table_header, tablefmt="orgtbl"))
	print ("\n")

	return 0
