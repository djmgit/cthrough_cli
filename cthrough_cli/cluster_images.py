from .api_handler import api_handler
import tabulate
from .apis import cluster_images_api

def cluster_docs(list_of_images, threshold=None, pretty=True):
	request_body = {
		"list_of_images": list_of_images,
		"threshold": threshold
	}

	response = api_handler(cluster_images_api, request_body)
	if not response:
		print ("Operation could not be completed successfully.")
		return 1

	if not pretty:
		print ("Clusters: ")
		print ("\n")
		for cluster in response.get("data"):
			print (" ".join(cluster))
		print ("\n")

		return 0

	table_header = ['Cluster ID', "Image Names"]
	table = []

	for index, cluster in enumerate(response.get("data")):
		table.append([index] + cluster)

	print ("Clusters: ")
	print ("\n")
	print (tabulate(table_body, table_header, tablefmt="orgtbl"))
	print ("\n")

	return 0
