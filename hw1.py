#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 12:56:59 2018

@author: mirandayuan
"""

class NGram():  
  
    def __init__(self):  
        self.unigram = {}  
        self.bigram = {}
        
        
    def ngrams(self,content,str):
        #generate the list of bigrams and trigrams; 'b'represent bigram and 't' represent trigram
        ngram_list = []
        if str == 'b':
            for i in range(len(content)):
                if i < len(content)-1:
                    ngram_list.append([content[i], content[i+1]])
            #print(bigram_list)
        elif str == 't':
            for i in range(len(content)):
                if i < len(content)-2:
                    ngram_list.append([content[i], content[i+1], content[i+2]])
            #print(trigram_list)
        return ngram_list


    def frequency(self, list ):
        #compute the frequencies of every unique element in bigram and trigram and sort them in the order of their frequencies separately
        ngram = {}
        for stri in list:
            str_c = ','.join(stri)
            if str_c not in ngram:  
                ngram[str_c] = 1  
            else:  
                ngram[str_c] = ngram[str_c] + 1  
        return ngram;

    def Prob_Tri(self):
        #compute the probability of third word using trigram language model
        Test = input("please input three words splited by comma:")
        if Test in trigram:
            count_unt = trigram[Test]
        else:
            count_unt = 0
    
        TestL = Test.split(',')
        Test2 = TestL[1] + ',' + TestL[2]
    
        if Test2 in bigram:
            count_unb = bigram[Test2]
        else:
            return 0
    
        prob = count_unt / count_unb
        return prob
    
    

if __name__=="__main__":  
    
    import glob
    import re

    #combine the files
    path =('./data/*.txt')
    files = glob.glob(path)
    with open("./result.txt", "wb") as outfile:
        for f in files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

    #import dataset & replace all non-alphabet with space
    path =('./result.txt')
    f = open(path, 'r')
    content = f.read()
    
    #exception
    content = content.replace("<br />", "")
    content = content.replace("n't", " not")
    content = content.replace("'ll", " will")
    content = content.replace("'m", " am")
    content = content.replace("'d", " would")
    content = content.replace("'ve", " have")
    content = content.replace("'re", " are")
    #exception about "s"
    content = content.replace("who's", "who is")
    content = content.replace("what's", "what is")
    content = content.replace("that's", "that is")
    content = content.replace("it's", "it is")
    content = content.replace("he's", "he is")
    content = content.replace("she's", "she is")
    content = content.replace("there's", "there is")
    content = content.replace("here's", "here is")
    content = content.replace("let's", "let us")
    content = content.replace("'s", "s")


    content = re.sub('[^0-9a-zA-Z]+', ' ', content).split()
    print(content)
    f.close

    print(len(content))  #number of tokens:26565
    
    print(len(set(content)))  #size of vocabulary:5043
    
    exe = NGram()
    bigram_list = exe.ngrams(content,'b')
    trigram_list = exe.ngrams(content,'t')
    
    bigram = exe.frequency(bigram_list)
    sorted(bigram.items(), key = lambda item:item[1])

    trigram = exe.frequency(trigram_list)
    sorted(trigram.items(), key = lambda item:item[1])
    
    prob = exe.Prob_Tri()
    print(prob)