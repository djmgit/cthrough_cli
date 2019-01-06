## Cthrough CLI
Cthrough CLI allows us to use almost all the features that Cthrough API offers us.
As of now it does not come as a pip package so we have to use to from source. 

To know more about the API, please read here : https://github.com/djmgit/cthrough/blob/master/README.md
### How to use this tool
- First of all, clone or download this repository
- Next open terminal and enter into the repo
- Run ```pip3 install -r requirements``` to install all the requirements. optionally you may use a virtual environment.
- Run the tool as ``` python3 . [operation_name] [params]

### Functionalities provided by the tool
The following operations are provided by the tool
Npte, the below examples uses data present in the /examples directory. You may look in to that folder.

### find_sim_between_two

```
USAGE: 
python3 . find_sim_between_two -h
Usage: . [options]

Options:
  -h, --help            show this help message and exit
  --doc1=DOC1           Enter path for doc1
  --doc2=DOC2           Enter path for doc2
  -p PRETTY, --pretty=PRETTY
                        Pretty or not, default true
                        

python3 . find_sim_between_two --doc1 examples/docs/test1.txt  --doc2 examples/docs/test2.txt 

Similarity score: 0.6674238124719146

```

### find_similar_docs
```
python3 . find_similar_docs -h
Usage: . [options]

Options:
  -h, --help            show this help message and exit
  --primary_doc=PRIMARY_DOC
                        Enter path for primary_doc
  --files=FILES         Enter list of file paths
  --directory=DIRECTORY
                        Enter directory path. This option and files  option
                        cannot be used together
  -t THRESHOLD, --threshold=THRESHOLD
                        Enter threshold
  -p PRETTY, --pretty=PRETTY
                        Pretty or not, default true
                        
python3 . find_similar_docs --primary_doc examples/docs/test1.txt --directory examples/docs/ -t 0.4
Documents similar to test1.txt:


| Document Name   |   Similarity score |
|-----------------+--------------------|
| test2.txt       |           0.667424 |
| test1.txt       |           1        |

                        
```
### cluster_docs
```
python3 . cluster_docs -h
Usage: . [options]

Options:
  -h, --help            show this help message and exit
  --files=FILES         Enter list of file paths
  --directory=DIRECTORY
                        Enter directory path. This option and files  option
                        cannot be used together
  -t THRESHOLD, --threshold=THRESHOLD
                        Enter threshold
  -p PRETTY, --pretty=PRETTY
                        Pretty or not, default true

python3 . cluster_docs --directory examples/docs/ -t 0.4
Clusters: 


|   Cluster ID | Document Names       |
|--------------+----------------------|
|            0 | test2.txt, test1.txt |
|            1 | test4.txt, test3.txt |
|            2 | test6.txt            |
|            3 | test5.txt            |

```
### find_sim_between_two_images
```
python3 . find_sim_between_two_images -h
Usage: . [options]

Options:
  -h, --help            show this help message and exit
  --img1=IMG1           Enter path for image1
  --img2=IMG2           Enter path for image2
  -p PRETTY, --pretty=PRETTY
                        Pretty or not, default true
                    
python3 . find_sim_between_two_images --img1 examples/images/skate1.jpg --img2 examples/images/skate2.png 
skate1.jpg skate2.png
Similarity score: 0.6
```
### find_sim_between_image_text
```
python3 . find_sim_between_image_text -h
Usage: . [options]

Options:
  -h, --help            show this help message and exit
  --img=IMG             Enter path for image
  --doc=DOC             Enter path for document
  -p PRETTY, --pretty=PRETTY
                        Pretty or not, default true
          
python3 . find_sim_between_image_text --img examples/images/skate1.jpg --doc examples/docs/test6.txt 
Similarity score: 0.48989794855663565
```
### find_docs_similar_to_image
```
python3 . find_docs_similar_to_image -h
Usage: . [options]

Options:
  -h, --help            show this help message and exit
  --primary_image=PRIMARY_IMAGE
                        Enter path for primary_image
  --files=FILES         Enter list of file paths
  --directory=DIRECTORY
                        Enter directory path. This option and files  option
                        cannot be used together
  -t THRESHOLD, --threshold=THRESHOLD
                        Enter threshold
  -p PRETTY, --pretty=PRETTY
                        Pretty or not, default true
python3 . find_docs_similar_to_image --primary_image examples/images/skate1.jpg --directory examples/docs/ -t 0.4
Documents similar to skate1.jpg:


| Document Name   |   Similarity score |
|-----------------+--------------------|
| test6.txt       |           0.489898 |

```
### find_images_similar_to_doc
```
 python3 . find_images_similar_to_doc -h
Usage: . [options]

Options:
  -h, --help            show this help message and exit
  --primary_doc=PRIMARY_DOC
                        Enter path for primary_doc
  --files=FILES         Enter list of file paths
  --directory=DIRECTORY
                        Enter directory path. This option and files  option
                        cannot be used together
  -t THRESHOLD, --threshold=THRESHOLD
                        Enter threshold
  -p PRETTY, --pretty=PRETTY
                        Pretty or not, default true

python3 . find_images_similar_to_doc --primary_doc examples/docs/test6.txt --directory examples/images -t 0.4
Documents similar to test6.txt:


| Image Name   |   Similarity score |
|--------------+--------------------|
| skate1.jpg   |           0.489898 |
| skatec.jpg   |           0.489898 |

```
### cluster_images
```
python3 . cluster_images -h
Usage: . [options]

Options:
  -h, --help            show this help message and exit
  --files=FILES         Enter list of file paths
  --directory=DIRECTORY
                        Enter directory path. This option and files  option
                        cannot be used together
  -t THRESHOLD, --threshold=THRESHOLD
                        Enter threshold
  -p PRETTY, --pretty=PRETTY
                        Pretty or not, default true
                      
python3 . cluster_images --directory examples/images/ -t 0.2
Clusters: 


|   Cluster ID | Image Names                        |
|--------------+------------------------------------|
|            0 | skate1.jpg, basket.jpg, skatec.jpg |

```



