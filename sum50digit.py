# AUTHOR : HARHSIT GARG
# DATE : APRIL 14, 2014
# PROJECT : TO SUM 100 50-digit numbers

import math;
import string;

f = open("50digitnumbers.txt", "r");
#line = f.readline();
lines = []
ans = []
i = 1;
for line in f:
    lines.append(line);
    print i, line,
    i = i + 1;
    #if( i != len(line)-1):
     #   print i, line[i]+ " " 
print "\n",lines

sum1 = 0;
carry = 0;
sum2 = 0;

for i in range(49,-1,-1):
    sum1 = 0;
    for j in range(100):
        #print "val = ",int(lines[j][i])
        sum1 = sum1 + int(lines[j][i]);
    print "i = ", i,"sum", sum1,    
    sum1 = sum1 + carry;
    print "sum",sum1    
    sum2 = sum1 % 10;    
    carry = sum1 - sum2;
    carry = carry / 10;
    print "sum1",sum1,   
    print "sum2",sum2,
    print "carry", carry
    ans.append(sum2);
    
print ans     

fans = []
fans1 = ""
fans.append(carry);
fans1 = fans1 + repr(carry);
for i in range(len(ans)-1,-1,-1):
    fans.append(ans[i]);
    fans1 = fans1 + repr(ans[i]);
print fans 
print "fans1",fans1

f.close();
f = open("50digitnumbers.txt","a");
f.write("\n");
f.write(repr(fans));
f.write("\n");
f.write(fans1);
