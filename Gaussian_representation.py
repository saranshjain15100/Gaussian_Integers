import math

def normalize( a, b, c, d, norm, A , N):
   rval = [a,b,c,d]
   num_of_zer = 0
   index = 0
   L = math.ceil(math.log2(N)) + 1
   temp = True
   i = 0
   while(temp):  
    if num_of_zer==L:
        break
    t = int(rval[i]/norm)
    next1 = int(t*pow(A-1,2))
    next2 = int(t*(2 * A - 1))
    next3 =  t 
    rval.append(0)
    rval.append(0)
    rval.append(0)
    rval[i] -= t * norm
    rval[i + 1] += next1
    rval[i + 2] += next2
    rval[i + 3] += next3
    index = i
    if rval[i] == 0:
        num_of_zer += 1
    else:
        num_of_zer = 0
    i += 1
   print('\u03B1' + ' = ' + str(rval[0]) ,end = "")
   for i in range(1,index+1):
    if rval[i] != 0 :
        print(' + ' + str(rval[i]) + '\u03B8' + '^' + str(i),end = "")
   print('\n')

A = int(input('Enter value of A'))
# A = 1
E = int(input('Enter value of E'))
F = int(input('Enter value of F'))

N = E*E + F*F
C =  E + A*F
D = F
norm = A * A + 1
if C == 0 and D == 0 :
    print('0')
    exit()
elif C >= 0 and D >= 0:
    normalize(C, D, 0, 0,norm,A,N)
elif C >= 0 and D <= 0:
    normalize(C, (A * A * abs(D)), (2 * A * abs(D)), abs(D), norm, A,N)
elif C <= 0 and D <= 0:
    normalize((A * A * abs(C)), (2 * A * abs(C) + A * A * abs(D)), (2 * A * abs(D) + abs(C)), (abs(D)), norm, A,N)
elif C <= 0 and D >= 0:
    normalize(A * A * D, (2 * A * abs(C) + D), abs(C), 0, norm, A,N)
print('\u03B1' + ' = '+ str(E) + ' + ' + str(F) + 'i')
print('\u03B8' + ' = -' + str(A) + ' + i')
 