Student ID : M2018218
Name: Davaanyam Battumur

NBC

def create_set(): 

	all files separate to two folder, 80% for trainset, 20% for testset

def file_read(root, read_file):
	
	read file from testset and return words

def cat_diction(root, files):
	
	read files from trainset and create Dictionary for every category, word and word count. after write to wordDic.json file


********Start code******
	
1. create_set():  Create M2018218/Trainset, M2018218/Trainset folders and separate all files from 20news-18828

2. read files from trainset and create Dictionary for every category, word and word count. after write to wordDic.json file

	I turned off the 1 and 2 steps on the code, because take 5 minute.

3. create Dictionary for folders name and file numbers in folder, this is for calculation

4. Read every Files from Testset and calculate probability using NBC, write results to result.txt file
	multiplying many probabilities together we could end up with really small numbers, and our computer might round down to zero. To prevent this, going to look at the log probability by taking the log of each side. Using some properties of logarithms, we can manipulate our Naive Bayes formulation.
