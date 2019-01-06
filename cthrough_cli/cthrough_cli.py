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

def get_image(file):
	if not os.path.exists(file) or not os.path.isfile(file):
		return None

	file_name = os.path.split(file)[1]

	if os.path.splitext(file_name)[1][1:] not in ['png', 'jpg']:
		return None

	content = ""
	with open(file, 'rb') as f:
		content = base64.b64encode(f.read()).decode()

	if content == "":
		return None

	return {
		"name": file_name,
		"content": content
	}

def get_file(file):
	if not os.path.exists(file) or not os.path.isfile(file):
		return None

	file_name = os.path.split(file)[1]

	if os.path.splitext(file_name)[1][1:] != "txt":
		return None

	content = ""
	with open(file) as f:
		content = f.read()

	if content == "":
		return None

	return {
		"name": file_name,
		"content": content
	}

def get_files(files, is_image=False):
	list_files = [f.strip() for f in files.split(",")]
	res = []

	for file in list_files:
		if is_image:
			file_obj = get_image(file)
		else:
			file_obj = get_file(file)
		if not file_obj:
			return None
		res.append(file_obj)

	return res

def get_dir(directory, is_image=False):
	if not os.path.exists(directory) or not os.path.isdir(directory):
		return None

	res = []

	for file in os.listdir(directory):
		if is_image:
			file_obj = get_image(os.path.join(directory, file))
		else:
			file_obj = get_file(os.path.join(directory, file))
		if not file_obj:
			return None

		res.append(file_obj)

	return res

def process_find_sim_between_two():
	pretty = True

	parser = optparse.OptionParser()
	parser.add_option('--doc1', dest='doc1',
				  help='Enter path for doc1')
	parser.add_option('--doc2', dest='doc2',
				  help='Enter path for doc2')
	parser.add_option('-p', '--pretty', dest='pretty',
				  help='Pretty or not, default true')

	(options, args) = parser.parse_args()

	doc1 = options.doc1
	doc2 = options.doc2

	if options.pretty:
		pretty = options.pretty
		if pretty == "True":
			pretty = True
		else:
			pretty = False

	if not doc1 or not doc2:
		print ("Please provide a valid document path")
		return 1

	doc1_name = os.path.split(doc1)[1]
	doc2_name = os.path.split(doc2)[1]

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

	status = find_sim_between_two(doc1_text, doc2_text, pretty)

	return status

def process_find_similar_docs():
	pretty = True

	parser = optparse.OptionParser()
	parser.add_option('--primary_doc', dest='primary_doc',
				  help='Enter path for primary_doc')
	parser.add_option('--files', dest='files',
				  help='Enter list of file paths')
	parser.add_option('--directory', dest='directory',
				  help='Enter directory path. This option and files  option cannot be used together')
	parser.add_option('-t', '--threshold', dest='threshold',
				  help='Enter threshold')
	parser.add_option('-p', '--pretty', dest='pretty',
				  help='Pretty or not, default true')

	(options, args) = parser.parse_args()

	primary_doc = options.primary_doc
	files = options.files
	directory = options.directory
	threshold = options.threshold

	if not primary_doc:
		print ("Please provide a valid path to primary document.")
		return 1

	if not threshold:
		print ("Please provide a valid threshold")
		return 1

	if not files and not directory:
		print ("Please provide either list of files or a directry path")
		return 1

	if files and directory:
		print ("Both files and list of directories provided. List of files will be used")

	if options.pretty:
		pretty = options.pretty
		if pretty == "True":
			pretty = True
		else:
			pretty = False

	primary_doc = get_file(primary_doc)
	if files:
		list_of_docs = get_files(files)
	else:
		list_of_docs = get_dir(directory)

	if primary_doc and list_of_docs:
		status = find_similar_docs(primary_doc, list_of_docs, threshold, pretty)
		return status
	
	print ("Please provide valid paths")
	return 1

def process_cluster_docs():
	pretty = True

	parser = optparse.OptionParser()
	parser.add_option('--files', dest='files',
				  help='Enter list of file paths')
	parser.add_option('--directory', dest='directory',
				  help='Enter directory path. This option and files  option cannot be used together')
	parser.add_option('-t', '--threshold', dest='threshold',
				  help='Enter threshold')
	parser.add_option('-p', '--pretty', dest='pretty',
				  help='Pretty or not, default true')

	(options, args) = parser.parse_args()

	files = options.files
	directory = options.directory
	threshold = options.threshold

	if not threshold:
		print ("Please provide a valid threshold")
		return 1

	if not files and not directory:
		print ("Please provide either list of files or a directry path")
		return 1

	if files and directory:
		print ("Both files and list of directories provided. List of files will be used")

	if options.pretty:
		pretty = options.pretty
		if pretty == "True":
			pretty = True
		else:
			pretty = False

	if files:
		list_of_docs = get_files(files)
	else:
		list_of_docs = get_dir(directory)

	if list_of_docs:
		status = cluster_docs(list_of_docs, threshold, pretty)
		return status
	
	print ("Please provide valid paths")
	return 1

def process_find_sim_between_two_images():
	pretty = True

	parser = optparse.OptionParser()
	parser.add_option('--img1', dest='img1',
				  help='Enter path for image1')
	parser.add_option('--img2', dest='img2',
				  help='Enter path for image2')
	parser.add_option('-p', '--pretty', dest='pretty',
				  help='Pretty or not, default true')

	(options, args) = parser.parse_args()

	img1 = options.img1
	img2 = options.img2

	if options.pretty:
		pretty = options.pretty
		if pretty == "True":
			pretty = True
		else:
			pretty = False

	if not img1 or not img2:
		print ("Please provide a valid image path")
		return 1

	img1_name = os.path.split(img1)[1]
	img2_name = os.path.split(img2)[1]

	print (img1_name, img2_name)
	#print (os.path.splitext(img1_name)[1][1:], os.path.splitext(img2_name)[1][1:])

	if os.path.splitext(img1_name)[1][1:] not in ['jpg', 'png']:
		print ("Please provide jpg or png files only")
		return 1

	if os.path.splitext(img2_name)[1][1:] not in ['jpg', 'png']:
		print ("Please provide jpg or png files only")
		return 1

	with open(img1, 'rb') as f:
		img1_content = base64.b64encode(f.read()).decode()

	with open(img2, 'rb') as f:
		img2_content = base64.b64encode(f.read()).decode()

	status = find_sim_between_two_images(img1_content, img2_content, pretty)

	return status

def process_find_sim_between_image_text():
	pretty = True

	parser = optparse.OptionParser()
	parser.add_option('--img', dest='img',
				  help='Enter path for image')
	parser.add_option('--doc', dest='doc',
				  help='Enter path for document')
	parser.add_option('-p', '--pretty', dest='pretty',
				  help='Pretty or not, default true')

	(options, args) = parser.parse_args()

	img = options.img
	doc = options.doc

	if options.pretty:
		pretty = options.pretty
		if pretty == "True":
			pretty = True
		else:
			pretty = False

	if not img or not doc:
		print ("Please provide a valid document and image path")
		return 1

	img_name = os.path.split(img)[1]
	doc_name = os.path.split(doc)[1]

	if os.path.splitext(img_name)[1][1:] not in ['jpg', 'png']:
		print ("Please provide jpg and png files only for image")
		return 1

	if os.path.splitext(doc_name)[1][1:] != "txt":
		print ("Please provide text files only")
		return 1

	with open(doc) as f:
		doc_text = f.read()

	with open(img, 'rb') as f:
		img_content = base64.b64encode(f.read()).decode()

	status = find_sim_between_image_text(img_content, doc_text, pretty)

	return status

def process_find_docs_similar_to_image():
	pretty = True

	parser = optparse.OptionParser()
	parser.add_option('--primary_image', dest='primary_image',
				  help='Enter path for primary_image')
	parser.add_option('--files', dest='files',
				  help='Enter list of file paths')
	parser.add_option('--directory', dest='directory',
				  help='Enter directory path. This option and files  option cannot be used together')
	parser.add_option('-t', '--threshold', dest='threshold',
				  help='Enter threshold')
	parser.add_option('-p', '--pretty', dest='pretty',
				  help='Pretty or not, default true')

	(options, args) = parser.parse_args()

	primary_image = options.primary_image
	files = options.files
	directory = options.directory
	threshold = options.threshold

	if not primary_image:
		print ("Please provide a valid path to primary image.")
		return 1

	if not threshold:
		print ("Please provide a valid threshold")
		return 1

	if not files and not directory:
		print ("Please provide either list of files or a directry path")
		return 1

	if files and directory:
		print ("Both files and list of directories provided. List of files will be used")

	if options.pretty:
		pretty = options.pretty
		if pretty == "True":
			pretty = True
		else:
			pretty = False

	primary_image = get_image(primary_image)
	if files:
		list_of_docs = get_files(files)
	else:
		list_of_docs = get_dir(directory)

	if primary_image and list_of_docs:
		status = find_docs_similar_to_image(primary_image, list_of_docs, threshold, pretty)
		return status
	
	print ("Please provide valid paths")
	return 1

def process_find_images_similar_to_doc():
	pretty = True

	parser = optparse.OptionParser()
	parser.add_option('--primary_doc', dest='primary_doc',
				  help='Enter path for primary_doc')
	parser.add_option('--files', dest='files',
				  help='Enter list of file paths')
	parser.add_option('--directory', dest='directory',
				  help='Enter directory path. This option and files  option cannot be used together')
	parser.add_option('-t', '--threshold', dest='threshold',
				  help='Enter threshold')
	parser.add_option('-p', '--pretty', dest='pretty',
				  help='Pretty or not, default true')

	(options, args) = parser.parse_args()

	primary_doc = options.primary_doc
	files = options.files
	directory = options.directory
	threshold = options.threshold

	if not primary_doc:
		print ("Please provide a valid path to primary document.")
		return 1

	if not threshold:
		print ("Please provide a valid threshold")
		return 1

	if not files and not directory:
		print ("Please provide either list of files or a directry path")
		return 1

	if files and directory:
		print ("Both files and list of directories provided. List of files will be used")

	if options.pretty:
		pretty = options.pretty
		if pretty == "True":
			pretty = True
		else:
			pretty = False

	primary_doc = get_file(primary_doc)
	if files:
		list_of_images = get_files(files, is_image=True)
	else:
		list_of_images = get_dir(directory, is_image=True)

	if primary_doc and list_of_images:
		status = find_images_similar_to_doc(primary_doc, list_of_images, threshold, pretty)
		return status
	
	print ("Please provide valid paths")
	return 1

def process_cluster_images():
	pretty = True

	parser = optparse.OptionParser()
	parser.add_option('--files', dest='files',
				  help='Enter list of file paths')
	parser.add_option('--directory', dest='directory',
				  help='Enter directory path. This option and files  option cannot be used together')
	parser.add_option('-t', '--threshold', dest='threshold',
				  help='Enter threshold')
	parser.add_option('-p', '--pretty', dest='pretty',
				  help='Pretty or not, default true')

	(options, args) = parser.parse_args()

	files = options.files
	directory = options.directory
	threshold = options.threshold

	if not threshold:
		print ("Please provide a valid threshold")
		return 1

	if not files and not directory:
		print ("Please provide either list of files or a directry path")
		return 1

	if files and directory:
		print ("Both files and list of directories provided. List of files will be used")

	if options.pretty:
		pretty = options.pretty
		if pretty == "True":
			pretty = True
		else:
			pretty = False

	if files:
		list_of_images = get_files(files, is_image=True)
	else:
		list_of_images = get_dir(directory, is_image=True)

	if list_of_images:
		status = cluster_images(list_of_images, threshold, pretty)
		return status
	
	print ("Please provide valid paths")
	return 1

def main():
	if len(sys.argv) == 1:
		print ("No action specified")
		exit()

	action = sys.argv[1]

	if action == "find_sim_between_two":
		process_find_sim_between_two()

	if action == "find_similar_docs":
		process_find_similar_docs()

	if action == "cluster_docs":
		process_cluster_docs()

	if action == "find_sim_between_two_images":
		process_find_sim_between_two_images()

	if action == "find_sim_between_image_text":
		process_find_sim_between_image_text()

	if action == "find_docs_similar_to_image":
		process_find_docs_similar_to_image()

	if action == "find_images_similar_to_doc":
		process_find_images_similar_to_doc()

	if action == "cluster_images":
		process_cluster_images()

if __name__ == "__main__":
	main()
	 
