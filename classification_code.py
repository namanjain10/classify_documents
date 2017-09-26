import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

from create_dic import create_dic

s = stopwords.words('english')

s.append('results')
s.append('also')
s.append('ued')
s.append('oed')

s = s + [chr(ord('a')+i) for i in range (26)]

refer = create_dic()

hf = pd.read_csv('/home/shubham/Documents/datasets/Untitled Folder/Hackathon_Packet/2.document_set/document_set.csv')
tf = pd.read_csv('/home/shubham/Documents/datasets/Untitled Folder/Hackathon_Packet/4.test_data/Test_Data.csv')

val = list(tf['document_id'])
test = len(val)

for i in range(test):
    c, n = val[i].split('_')
    n = int(n)

    val[i] = n

for l in range (len(val)) :

    dic_test = {i: {'value': 0, 'count': 0} for i in range(43)}
    result = []

    a = wordpunct_tokenize(re.sub('[^A-Za-z]', ' ', hf['Text'][val[l]].lower()))
    d = [word for word in a if word not in s]

    for j in d:
        try:
            q = refer[j]
            # print (q)
        except:
            q = {0: 0}

        for k in q:
            dic_test[k]['value'] += q[k]
            dic_test[k]['count'] += 1

    for k in range(43):

        try:
            t = dic_test[k]['value'] / dic_test[k]['count']

        except:
            t = 0
        result.append(t)

    val[l] = ['Document_'+str(val[l]),result.index(max(result))]

ds = pd.DataFrame(val, columns=['document_id', 'category'])

ds.to_csv('../evaluation_file/predicted_cat.csv',index = False)
