import math
import os
import sys
import codecs
import binascii




f = open(os.getcwd()+'\\tests.txt', 'rb')
output = f.read()


sentence = open(os.getcwd()+'\\sentences.txt', 'rb')
sentence_output = sentence.read()

ascii_check = [0]*127
P_ascii = [0]*127
a = [0]*2350
b = [0]*11172
Pa = [0]*2350
Pb = [0]*11172


#텍스트 파일이 utf8인지 ks완성형인지 판단해주는 함수
def CHECKs(S):

    if hex(S[0]) == '0xef' and (hex(S[3]) >= '0xea' and hex(S[3]) <= '0xed') and (hex(S[4]) >='0x80' \
       and hex(S[4]) <='0xbf') and (hex(S[5]) >=  '0x80' and hex(S[5]) <=  '0xbf'):
        utf8_count(output,ascii_check)
        pro_cal(Pb,b,ascii_check)
        pro_cal(P_ascii,ascii_check,b)
      
        
    elif (hex(S[0]) >= '0xb0' and hex(S[0]) <= '0xc8') and (hex(S[1]) >= '0xa1' and hex(S[1]) <= '0xfe') :       
        euc_count(output,ascii_check)
        pro_cal(Pa,a,ascii_check)
        pro_cal(P_ascii,ascii_check,a)

        
        

#텍스트 파일이 ks완성형일때 빈도수 계산 
def euc_count(K,K2):
    i = 0
    while i < len(K):
        if ((hex(K[i]) >= '0xb0' and  hex(K[i]) <= '0xc8') and (hex(K[i+1])>='0xa1' and hex(K[i+1]) <= '0xfe')):
            a[(K[i]-176)*94+(K[i+1]-161)] += 1
            i = i+2
        elif hex(K[i]) <='0x7f' and hex(K[i]) != '0x20':
            K2[K[i]] += 1
            i = i+1
        else:
            i = i+1

  
#텍스트 파일이 utf8일 때 빈도수 계산          
def utf8_count(K,K2):

    for i in range(3,len(K)):
            if hex(K[i]) >= '0xea' and hex(K[i]) <= '0xed' and hex(K[i+1]) >= '0x80' \
               and hex(K[i+1]) <= '0xbf' and hex(K[i+2]) >= '0x80' and hex(K[i+2]) <= '0xbf' :
                i = (K[i] & 15 ) << 12 | (K[i+1] & 63) << 6 | (K[i+2] & 63)
                i = i - 44032
                b[i] += 1
                i = i+3
            elif hex(K[i]) <= '0x7f' and hex(K[i]) != '0x20':
                K2[K[i]] += 1
                i = i+1
            else:
                i = i+1

     
#각 음절의 출현 확률계산 함수
def pro_cal(M,N,X):
    for i in range(0,len(N)):
        M[i] = N[i]/(sum(N)+sum(X))


#입력받은 문장이 ks완성형인지 utf8인지 판단해주는 함수
def CHECKss(S):

    if hex(S[0]) == '0xef' and (hex(S[3]) >= '0xea' and hex(S[3]) <= '0xed') and (hex(S[4]) >='0x80' \
       and hex(S[4]) <='0xbf') and (hex(S[5]) >=  '0x80' and hex(S[5]) <=  '0xbf'):
        cal_sen_utf8(sentence_output,Pb,P_ascii)
                
    elif (hex(S[0]) >= '0xb0' and hex(S[0]) <= '0xc8') and (hex(S[1]) >= '0xa1' and hex(S[1]) <= '0xfe') :       
        cal_sen_ks(sentence_output,Pa,P_ascii)
        
#입력받은 문장이 ks완성형일때 문장생성확률을 구하는 함수
def cal_sen_ks(K,K2,K3):
    j = 0
    final = 1
    while j <len(K):
        if ((hex(K[j]) >= '0xb0' and  hex(K[j]) <= '0xc8') and (hex(K[j+1])>='0xa1' \
               and hex(K[j+1]) <= '0xfe')) :
            final = final * K2[(K[j]-176)*94+(K[j+1]-161)]
            j = j+2
        elif hex(K[j]) <= '0x7f' and hex(K[j]) != '0x20':
            final = final * K3[K[j]]
            j = j+1
        else:
            j = j+1
    print(final)
    
#입력받은 문장이 utf8일때 문장생성확률을 구하는 함수
def cal_sen_utf8(K,K2,K3):
    final = 1
    for i in range(3,len(K)):
        if hex(K[i]) >= '0xea' and hex(K[i]) <= '0xed' and hex(K[i+1]) >= '0x80' \
               and hex(K[i+1]) <= '0xbf' and hex(K[i+2]) >= '0x80' and hex(K[i+2]) <= '0xbf' :
            
            i = (K[i] & 15 ) << 12 | (K[i+1] & 63) << 6 | (K[i+2] & 63)
            i = i - 44032
            final = final * K2[i]    
           
            i = i+3
        elif hex(K[i]) <= '0x7f' and hex(K[i]) != '0x20':
            final = final * K3[K[i]] 
            i = i+1
        else:
            i = i+1
    print(final)
    
    
if __name__=="__main__":
    CHECKs(output)
    CHECKss(sentence_output)
   






