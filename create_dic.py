import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

s = stopwords.words('english')

s.append('results')
s.append('also')
s.append('ued')
s.append('oed')

s = s + [chr(ord('a')+i) for i in range (26)]

def create_dic () :

    df = pd.read_csv('/home/shubham/Documents/datasets/Untitled Folder/Hackathon_Packet/3.training_data/Training_Data.csv')

    hf = pd.read_csv('/home/shubham/Documents/datasets/Untitled Folder/Hackathon_Packet/2.document_set/document_set.csv')

    split = df.shape[0]

    bigy = []

    for j in range(0, 43):

        dic = {}

        for i in range(0, split):

            if df['category'][i] == j:

                c, n = df['document_id'][i].split('_')
                n = int(n)
                a = wordpunct_tokenize(re.sub('[^A-Za-z]', ' ', hf['Text'][n].lower()))
                d = [word for word in a if word not in s]

                for k in d:
                    try:
                        dic[k] += 1

                    except:
                        dic[k] = 1

        bigy.append(dic)

    refer = {}

    for j in range(0, 43):
        for i in bigy[j]:
            try:
                refer[i][j] = bigy[j][i]

            except:
                refer[i] = {j: bigy[j][i]}

    for i in refer:
        sum1 = 0

        for j in refer[i]:
            sum1 += refer[i][j]

        for k in refer[i]:
            refer[i][k] = refer[i][k] / sum1

    return refer