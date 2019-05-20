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

#모든 구현을 수행할 text파일을 열어 한줄씩 읽습니다.한줄씩 읽을때 마침표를 기준으로 자릅니다.

def open_for_bi_tri():
  
  with codecs.open("/gdrive/My Drive/Colab Notebooks/KCCq28_Korean_sentences_UTF8.txt", encoding='utf-8') as f:
    file = []
    output = [line.split('.') for line in f.read().splitlines()]
    
    for i in output:
      for j in i:
        file.append(j.strip())

  file = list(filter(lambda x: x!= '',file))
  return file

#wordcloud를 만들기 위해 unigram 빈도 count에서 가장 빈도가 높은 3개의 단어를 뽑아내려고 정의한 함수입니다.
#이 함수에서는 text파일을 이미 wordcount.exe를 돌린 outs.txt를 입력으로 받습니다.
def open_for_uni():
  with codecs.open("/gdrive/My Drive/Colab Notebooks/outs.txt", encoding='utf-8') as k:
    output_uni = k.read()
  
  split_file = []
  split_file = output_uni.split()
  split_file[0] = split_file[0].replace('\ufeff','')

  return split_file

#file안에 있는 내용을 bigram형태로 바꿔 빈도count할 준비를 하기 위해 정의한 함수입니다.
def bi_output():
  bigram_output = []
  file = open_for_bi_tri()
  
  for i in file:
    tokens = word_tokenize(i)
    bigram = ngrams(tokens, 2, pad_left=True, pad_right=True, \
                     left_pad_symbol="SS", right_pad_symbol="SE")
    bigram_output += [t for t in bigram]
  
  return bigram_output
  
#file안에 있는 내용을 trigram형태로 바꿔 빈도 count할 준비를 하기 위해 정의한 함수입니다.
def tri_output(): 
  trigram_output = []
  file = open_for_bi_tri()
  for j in file:
    tokens = word_tokenize(j)
    trigram = ngrams(tokens, 3, pad_left=True, pad_right=True, \
                     left_pad_symbol="SS", right_pad_symbol="SE")
    trigram_output += [t for t in trigram]
  
  return trigram_output

#bigram 빈도 count를 위한 함수입니다.
def bigram_dic():
  bigram_output = bi_output()
  bigram_count = ConditionalFreqDist(bigram_output)
  global BI_SEED
  BI_SEED = bigram_count['SS'].most_common(3)
  return bigram_count

#trigram 빈도 count를 위한 함수입니다.    
def trigram_dic():
  trigram_output = tri_output()
  change_tri_to_count = (((a,a1),a2) for a,a1,a2 in trigram_output)
  trigram_count = ConditionalFreqDist(change_tri_to_count)
  global TRI_SEED
  TRI_SEED = trigram_count['SS','SS'].most_common(3)
  return trigram_count


def word_tri():
  trigram_output = tri_output()
  word_tri = ((a,(a1+'_'+a2)) for a,a1,a2 in trigram_output)
  word_trigram_count = ConditionalFreqDist(word_tri)
  return word_trigram_count


def wordcloud_bi():
  bigram_count = bigram_dic()
  split_file = open_for_uni()
  biword_1 = [(a,b) for a,b in bigram_count[split_file[1]].most_common(20)]
  biword_2 = [(a,b) for a,b in bigram_count[split_file[3]].most_common(20)]
  biword_3 = [(a,b) for a,b in bigram_count[split_file[5]].most_common(20)]

  font_path = "/gdrive/My Drive/Colab Notebooks/NanumBarunGothic.ttf"

  wc = WordCloud(font_path=font_path,background_color='black',width=800,height=600)
  cloud = wc.generate_from_frequencies(dict(biword_1))
  plt.figure(figsize=(10,8))
  plt.axis('off')
  plt.imshow(cloud)

  wc = WordCloud(font_path=font_path,background_color='white',width=800,height=600)
  cloud = wc.generate_from_frequencies(dict(biword_2))
  plt.figure(figsize=(10,8))
  plt.axis('off')
  plt.imshow(cloud)

  wc = WordCloud(font_path=font_path,background_color='black',width=800,height=600)
  cloud = wc.generate_from_frequencies(dict(biword_3))
  plt.figure(figsize=(10,8))
  plt.axis('off')
  plt.imshow(cloud)

def wordcloud_tri():
  word_trigram_count = word_tri()
  split_file = open_for_uni()
  triword_1 = [(a,b) for a,b in word_trigram_count[split_file[1]].most_common(20)]
  triword_2 = [(a,b) for a,b in word_trigram_count[split_file[3]].most_common(20)]
  triword_3 = [(a,b) for a,b in word_trigram_count[split_file[5]].most_common(20)]

  font_path = "/gdrive/My Drive/Colab Notebooks/NanumBarunGothic.ttf"

  wc = WordCloud(font_path=font_path,background_color='black',width=800,height=600)
  cloud = wc.generate_from_frequencies(dict(triword_1))
  plt.figure(figsize=(10,8))
  plt.axis('off')
  plt.imshow(cloud)

  wc = WordCloud(font_path=font_path,background_color='white',width=800,height=600)
  cloud = wc.generate_from_frequencies(dict(triword_2))
  plt.figure(figsize=(10,8))
  plt.axis('off')
  plt.imshow(cloud)

  wc = WordCloud(font_path=font_path,background_color='black',width=800,height=600)
  cloud = wc.generate_from_frequencies(dict(triword_3))
  plt.figure(figsize=(10,8))
  plt.axis('off')
  plt.imshow(cloud)
  
  

  
