## Cthrough CLI
Cthrough CLI allows us to use almost all the features that Cthrough API offers us.
As of now it does not come as a pip package so we have to use to from source. 

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


