import math
import os
import sys
import codecs
import binascii


DIC = {}
DIC2 = {}
DIC3 = {}


#1)원래 파일(test 파일)을 wordcount.exe로 돌려 어절빈도수를 측정한 후 결과값을 out.txt에 저장하고 시작합니다. 
f = open(os.getcwd()+'\\out.txt', 'rb')
output = f.read()


#읽은 파일을 split를 이용해서 어절과 빈도수를 각각 분리해 리스트에 저장합니다.
split_file = output.split()


#리스트에 저장한 값을 DIC에다가 {어절:빈도수}형태로 저장합니다.
#이 때 나중에 스무딩기법(Laplace(add-one) Smoothing)을 사용하기 위해 각 빈도수에 +1을 한값으로 DIC에 저장해줍니다.
i = 0
while i<len(split_file)-1:
    DIC[split_file[i+1]] = int(split_file[i])+1
    i = i+2


#2)문장생성확률을 구할 문장을 wordcount.exe로 돌린파일을 pmake.txt에 저장하고 시작합니다.
m = open(os.getcwd()+'\\pmake.txt', 'rb')
output2 = m.read()


#읽은 파일을 split를 이용해서 어절과 빈도수를 각각 분리해 리스트에 저장합니다.
split_file2 = output2.split()


#리스트에 저장한 값을 DIC2에다가 {어절:빈도수}에 형태로 저장합니다.
#이 때 스무딩기법(Laplace(add-one) Smoothing)을 사용하기 위해 만약 DIC에 포함되어 있지 않은 어절이 들어오면
#DIC에다가 빈도수 1을 가진 새로운 어절로 추가해줍니다.
j = 0
while j<len(split_file2)-1:
    DIC2[split_file2[j+1]] = int(split_file2[j])
    if (split_file2[j+1] in DIC) == False:
      DIC[split_file2[j+1]] = 1
      j = j+2
    else:
      j = j+2


#확률 딕셔너리를 만듭니다
for k in DIC : DIC3[k] = DIC[k]/sum(DIC.values()) 


#문장생성확률을 계산합니다.
prob_cal = 1

for a in DIC2:
  prob_cal *=  pow(DIC3[a],DIC2[a])


#문장생성확률을 프린트합니다.
print(prob_cal)


