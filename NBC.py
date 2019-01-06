import math
import nltk
import random
import os
import json
import subprocess
import string
import shutil
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

# 20news-18828 seperate to Trainset and Testset

def create_set():
#	shutil.rmtree('M2018218')
	subprocess.call( ['mkdir', '-p', 'M2018218'])
	subprocess.call( ['mkdir', '-p', 'M2018218/Testset'])
	subprocess.call( ['mkdir', '-p', 'M2018218/Trainset'])
	copydirTs='M2018218/Testset'
	copydirTr='M2018218/Trainset'
	for root, subfolders, files in os.walk('20news-18828', topdown=False):
		if root != '20news-18828':		
			ffffff=root.split('/')
# all folder & files copy from '20news-18828' to 'M2018218/Trainset'
			P_path=os.path.join(copydirTr, ffffff[len(ffffff)-1])
			subprocess.call(['mkdir', '-p', P_path])
			for copyfile in files:
				C_path = os.path.join(root, copyfile)
				shutil.copy(C_path, P_path)
# from 'M2018218/Trainset' 20% move to 'M2018218/Testset'
			i=1
			for movefile in files:
				if i<=len(files)*0.2:
					M_path=os.path.join(P_path, movefile)
					MP_path=os.path.join(copydirTs, ffffff[len(ffffff)-1])				
					subprocess.call(['mkdir', '-p', MP_path])
					shutil.move(M_path, MP_path)
					i=i+1
	return ('Create Training set and Testset is Finish')


#Returen words from read testset file 
def file_read(root, read_file):
	r_path = os.path.join(root, read_file)
	with open(r_path, 'rb') as f:
		rList = list(f.read())
# filter stopwoeds, letters convert to lower case and word tokenize
	wordList_Read_testset = list(filter(lambda x: x not in stopwords.words('english'), map(wnl.lemmatize, word_tokenize(''.join(chr(item).lower() if chr(item) in string.ascii_letters else ' ' for item in rList)))))
	i=-1
# Dont need one charectors, one chirector is not word		
	for word in wordList_Read_testset:
		i+=1        
		if len(word) == 1 : 
	            del wordList_Read_testset[i]
	return set(wordList_Read_testset)


#Return category all word number end write dictionary with count numbers in the category to wordDic.json file
def cat_diction(root, files):
	wordDic = {}
	bat={}
	all_words_C=[]
	wnl = WordNetLemmatizer()
	for read_file in files:
		r_path = os.path.join(root, read_file)
		with open(r_path, 'rb') as f:
			rList = list(f.read())
		wordList = list(filter(lambda x: x not in stopwords.words('english'), map(wnl.lemmatize, word_tokenize(''.join(chr(item).lower() if chr(item) in string.ascii_letters else ' ' for item in rList)))))
	
		i=-1
		for word in wordList:
			i+=1        
			if len(word) == 1 : 
		            del wordList[i]

		all_words_C+=set(wordList)
		wordList=set(wordList)

	all_words_C=nltk.FreqDist(all_words_C)
	dic_most=all_words_C.most_common(len(all_words_C))
#len(all_words_C
	for i, j in dic_most:
		wordDic[i] = j
	print(root, 'finish',len(all_words_C))
	bat[root]=wordDic
	with open('wordDic.json', 'a') as f:
	        f.writelines(json.dumps(bat) + '\n')

	return len(wordDic)



#start **************************

'''
print(create_set())

all_words_N=[]

#create Dictionary for every category, write dictionary to wordDic.json file

for root, subfolders, files in os.walk('M2018218/Trainset', topdown=True):
	if root != 'M2018218/Trainset':		
		fffff=root.split('/')
		category=fffff[len(fffff)-1]
		all_words_N.append(cat_diction(root, files))
print(all_words_N)
'''

#Totall words in training set

all_words_N=[12517, 15969, 10717, 10717, 13929, 9637, 15252, 11652, 11670, 26392, 13479, 10893, 14777, 13871, 10608, 13389, 12295, 9885, 9822, 10197]

#all file number from trainset and file number in category

all_file_N=0

#Dictionary for folders name and file numbers in folder
all_C_and_File_N={}
for root, subfolders, files in os.walk('M2018218/Trainset', topdown=True):
	if root != 'M2018218/Trainset':
		all_file_N+=len(files)
		all_C_and_File_N[root]=len(files)

# Read Files from Testset 
wnl = WordNetLemmatizer()
for root, subfolders, files in os.walk('M2018218/Testset', topdown=True):
	if root != 'M2018218/Testset':		
		fffff=root.split('/')
		category=fffff[len(fffff)-1]
	for read_file in files:
		wordList_Read_testset = file_read(root, read_file )
		print('File Name:',read_file)
		result='File Name: '+read_file
		with open('result.txt', 'a') as f:
		        f.write(result + '\n')
#dictionary probbility in Categorys
		dic_prob={}
#Read from Dic file
		i=-1
		magadlal=[]
		with open('wordDic.json') as f:
			for line in f:
				data=json.loads(line)
				i+=1			
				for b in data.keys():
					k=b		#k->category name
				l=data[k]		#l-> dictionary for K category
				c_probility=math.log(all_C_and_File_N[k]/all_file_N)
				f=k.split('/')
				k=f[len(f)-1]				
				for word in wordList_Read_testset:
#					print(l.get(word))				
					if type(l.get(word)) is int : 
						j=l.get(word)
						c_probility+=math.log((j+2)/(all_words_N[i]+sum(all_words_N)))
						magadlal.append(math.log((j+2)/(all_words_N[i]+sum(all_words_N))))
					else :
						c_probility+=math.log(1/(all_words_N[i]+sum(all_words_N)))
						magadlal.append(math.log(1/(all_words_N[i]+sum(all_words_N))))
#			print(wordList_Read_testset)
#				print(magadlal)
				result=('probility= '+str(c_probility)+'         '+k)
				with open('result.txt', 'a') as f:
				        f.write(result + '\n')
				print('probility=',c_probility,'	', k)
				dic_prob[k]=c_probility
		print('\n','File Name:',read_file,'Testset Category is:' , category)
		result=('File Name: '+read_file+'    Testset Category is: '+category)
		with open('result.txt', 'a') as f:
		        f.write(result + '\n')	
		print('My category is :', max(zip(dic_prob.values(), dic_prob.keys())), '\n')
		result='My category is : '+json.dumps(max(zip(dic_prob.values(),dic_prob.keys())))
		with open('result.txt', 'a') as f:
		        f.write(result + '\n \n')	

