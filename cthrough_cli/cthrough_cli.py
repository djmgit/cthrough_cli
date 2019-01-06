import optparse
from .find_sim_between_two import find_sim_between_two
from .find_similar_docs import find_similar_docs
from .find_similar_pairs import find_similar_pairs
from .cluster_docs import cluster_docs
from .find_sim_between_two_images import find_sim_between_two_images
from .find_sim_between_image_text import find_sim_between_image_text
from .find_images_similar_to_doc import find_images_similar_to_doc
from .find_docs_similar_to_image import find_docs_similar_to_image
from .cluster_images import cluster_images
import base64
import os
import sys

def process_find_sim_between_two():
	parser = optparse.OptionParser()
	parser.add_option('--doc1', dest='doc1',
				  help='Enter path for doc1')
	parser.add_option('--doc2', dest='doc2',
				  help='Enter path for doc2')

	(options, args) = parser.parse_args()

	doc1 = options.doc1
	doc2 = options.doc2

	if not doc1 or not doc2:
		print ("Please provide a valid document path")
		return 1

	doc1_name = os.path.split(doc1)
	doc2_name = os.path.split(doc2)

	if os.path.splitext(doc1_name)[1][1:] != "txt":
		print ("Please provide text files only")
		return 1

	if os.path.splitext(doc2_name)[1][1:] != "txt":
		print ("Please provide text files only")
		return 1

	with open(doc1) as f:
		doc1_text = f.read()

	with open(doc2) as f:
		doc2_text = f.read()

	status = find_sim_between_two(doc1_text, doc2_text,pretty)

	return status

def main():
	if len(sys.argv) == 1:
		print ("No action specified")
		exit()

	action = sys.argv[1]

	if action == "find_sim_between_two":
		process_find_sim_between_two()

if __name__ == "__main__":
	main()
	 
