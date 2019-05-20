import codecs
from nltk import bigrams, word_tokenize
from nltk.util import ngrams
from nltk import ConditionalFreqDist
from nltk.probability import ConditionalProbDist, MLEProbDist
from wordcloud import WordCloud
from matplotlib import pyplot
import matplotlib.pyplot as plt
import os
import random
from collections import OrderedDict

%matplotlib inline

def open_for_bi_tri():
  
  with codecs.open("/gdrive/My Drive/Colab Notebooks/KCCq28_Q01_Q02.txt", encoding='utf-8') as f:
    file = []
    output = [line.split('.') for line in f.read().splitlines()]
    
    for i in output:
      for j in i:
        file.append(j.strip())

  file = list(filter(lambda x: x!= '',file))
  return file
    

def bi_output():
  bigram_output = []
  file = open_for_bi_tri()
  
  for i in file:
    tokens = word_tokenize(i)
    bigram = ngrams(tokens, 2, pad_left=True, pad_right=True, \
                     left_pad_symbol="SS", right_pad_symbol="SE")
    bigram_output += [t for t in bigram]
  
  return bigram_output
  
    
def tri_output(): 
  trigram_output = []
  file = open_for_bi_tri()
  for j in file:
    tokens = word_tokenize(j)
    trigram = ngrams(tokens, 3, pad_left=True, pad_right=True, \
                     left_pad_symbol="SS", right_pad_symbol="SE")
    trigram_output += [t for t in trigram]
  
  return trigram_output

def bigram_dic():
  bigram_output = bi_output()
  bigram_count = ConditionalFreqDist(bigram_output)
  global BI_SEED
  BI_SEED = bigram_count['SS'].most_common(3)
  return bigram_count
    
def trigram_dic():
  trigram_output = tri_output()
  change_tri_to_count = (((a,a1),a2) for a,a1,a2 in trigram_output)
  trigram_count = ConditionalFreqDist(change_tri_to_count)
  global TRI_SEED
  TRI_SEED = trigram_count['SS','SS'].most_common(3)
  return trigram_count


global bigram_count
bigram_count = bigram_dic()
global bigram_pro
bigram_pro = ConditionalProbDist(bigram_count,MLEProbDist)

global trigram_count
trigram_count = trigram_dic()
global trigram_pro
trigram_pro = ConditionalProbDist(trigram_count,MLEProbDist)

#문장을 생성합니다.
def korean_bi_generate_sentence(M,seed=None, debug=False):
   
    
    c = M
    p = bigram_pro['SS'].prob(c)
   
    sentence = [c]
   
    while True:
      next_word = random.choice(bigram_count[c].most_common(10))[0]
      p *= bigram_pro[c].prob(next_word)
      c  = next_word
       
        
      if c == "SE":
        
        return " ".join(sentence),p
        
      else:
        
        sentence.append(c)

#생성된 문장과 그 문장의 생성확률을 저장해서 출력합니다.
def store_sort_bi_sentence():
     
   
   
    K = []
    for i in range(0,10):
      K.append(korean_bi_generate_sentence(BI_SEED[0][0],i))
    B1 = OrderedDict(sorted(dict(K).items(),key = lambda t: t[1],reverse = True))
    print(B1)
    K = []
    for i in range(0,10):
      K.append(korean_bi_generate_sentence(BI_SEED[1][0],i))
    B2 = OrderedDict(sorted(dict(K).items(),key = lambda t: t[1],reverse = True))
    print(B2)
    K = []
    for i in range(0,10):
      K.append(korean_bi_generate_sentence(BI_SEED[2][0],i))
    B3 = OrderedDict(sorted(dict(K).items(),key = lambda t: t[1],reverse = True))
    print(B3)  


def korean_tri_generate_sentence(M,seed=None, debug=False):
  
    
    c = M
    p = trigram_pro['SS','SS'].prob(c)
    
    sentence = [c]
    prev = "SS"
    while True:
       next_word = random.choice(trigram_count[prev,c].most_common(10))[0]
       p*= trigram_pro[prev,c].prob(next_word)
    
       prev, c  = c, next_word
       
       if c == "SE":
          p *= trigram_pro[prev,c].prob('SE')
          return " ".join(sentence),p

       else:
          sentence.append(c)

def store_sort_tri_sentence():
    
    
    K = []
    for i in range(0,10):
      K.append(korean_tri_generate_sentence(TRI_SEED[0][0],i))
    B1 = OrderedDict(sorted(dict(K).items(),key = lambda t: t[1],reverse = True))
    print(B1)
    K = []
    for i in range(0,10):
      K.append(korean_tri_generate_sentence(TRI_SEED[1][0],i))
    B2 = OrderedDict(sorted(dict(K).items(),key = lambda t: t[1],reverse = True))
    print(B2)
    K = []
    for i in range(0,10):
      K.append(korean_tri_generate_sentence(TRI_SEED[2][0],i))
    B3 = OrderedDict(sorted(dict(K).items(),key = lambda t: t[1],reverse = True))
    print(B3)  
