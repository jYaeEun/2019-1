
import math
import os
import sys
import codecs
import binascii



#file open
f = open(os.getcwd()+'\\test.txt', 'rb')

output = f.read()  

global k
k = 0


#list set
ascii_check = [0]*127
a = [0]*2350
b = [0]*11172


#check KS or UTF8
def CHECKs(S):

    if hex(S[0]) == '0xef' and (hex(S[3]) >= '0xea' and hex(S[3]) <= '0xed') and (hex(S[4]) >='0x80' \
       and hex(S[4]) <='0xbf') and (hex(S[5]) >=  '0x80' and hex(S[5]) <=  '0xbf'):        
        k = 1
        print("UTF8")
        u_k_print(k)
        
    elif (hex(S[0]) >= '0xb0' and hex(S[0]) <= '0xc8') and (hex(S[1]) >= '0xa1' and hex(S[1]) <= '0xfe') :       
        k = 2
        print("KS")
        u_k_print(k)
        
    else:
        print(3)



#to print ks        
ks = list(range(0xb0a1,0xb0ff))+ list(range(0xb1a1,0xb1ff)) + list(range(0xb2a1,0xb2ff)) + \
     list(range(0xb3a1,0xb3ff))+ list(range(0xb4a1,0xb4ff)) + list(range(0xb5a1,0xb5ff)) + \
     list(range(0xb6a1,0xb6ff))+ list(range(0xb7a1,0xb7ff)) + list(range(0xb8a1,0xb8ff)) + \
     list(range(0xb9a1,0xb9ff))+ list(range(0xbaa1,0xbaff)) + list(range(0xbba1,0xbbff)) + \
     list(range(0xbca1,0xbcff))+ list(range(0xbda1,0xbdff)) + list(range(0xbea1,0xbeff)) + \
     list(range(0xbfa1,0xbfff))+ list(range(0xc0a1,0xc0ff)) + list(range(0xc1a1,0xc1ff)) + \
     list(range(0xc2a1,0xc2ff))+ list(range(0xc3a1,0xc3ff)) + list(range(0xc4a1,0xc4ff)) + \
     list(range(0xc5a1,0xc5ff))+ list(range(0xc6a1,0xc6ff)) + list(range(0xc7a1,0xc7ff)) + \
     list(range(0xc8a1,0xc8ff))


#UTF8 frequency count&print
#KS frequency count&print

def u_k_print(n):
    if n == 1:
        for i in range(3,len(output)):
            if hex(output[i]) >= '0xea' and hex(output[i]) <= '0xed' and hex(output[i+1]) >= '0x80' \
               and hex(output[i+1]) <= '0xbf' and hex(output[i+2]) >= '0x80' and hex(output[i+2]) <= '0xbf' :
                i = (output[i] & 15 ) << 12 | (output[i+1] & 63) << 6 | (output[i+2] & 63)
                i = i - 44032
                b[i] += 1
                i = i+3
            elif hex(output[i]) <= '0x7f':
                ascii_check[output[i]] += 1
                i = i+1
            else:
                i = i+1

        for i in range(0,127):
            if ascii_check[i] >= 1:
                print(chr(i),':',ascii_check[i])

        for i in range(0,11172):
            if b[i] >= 1:
                u = chr(i+44032)
                print(u,':',b[i])
      
    
             
    elif n == 2:
        i = 0
        while i < len(output):
            if ((hex(output[i]) >= '0xb0' and  hex(output[i]) <= '0xc8') and (hex(output[i+1])>='0xa1' and hex(output[i+1]) <= '0xfe')):
                a[(output[i]-176)*94+(output[i+1]-161)] += 1
                i = i+2
            elif hex(output[i]) <='0x7f':
                ascii_check[output[i]] += 1
                i = i+1
            else:
                i = i+1

        for i in range(0,127):
            if ascii_check[i] >= 1:
                print(chr(i),':',ascii_check[i])

        for i in range(0,2350):
            if a[i] >=1:
                print(hex(ks[i]),':',a[i])

        
#main       
if __name__=="__main__":
    CHECKs(output)
    
    

f.close()
