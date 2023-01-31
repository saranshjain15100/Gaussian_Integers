import math

def normalize( a, b, c, d, norm, A , N):
   rval = [a,b,c,d]
   num_of_zer = 0
   index = 0
   L = math.ceil(math.log2(N)) + 1
   temp = True
   i = 0
   summu = 0
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
   rval = rval[:index]
   return sum(rval)

A = 1
E = int(input('Enter range for E'))
F = int(input('Enter range for F'))
k = int(input('Enter at most sum'))
sum_n = []
summu = 0
for e in range(-E,E+1):
    for f in range (-F,F+1):
        N = e*e + f*f
        C = e + A*f
        D = f
        norm = A * A + 1
        if C == 0 and D == 0 :
            summu = 0
            break
        elif C >= 0 and D >= 0:
            summu = normalize(C, D, 0, 0,norm,A,N)
        elif C >= 0 and D <= 0:
            summu = normalize(C, (A * A * abs(D)), (2 * A * abs(D)), abs(D), norm, A,N)
        elif C <= 0 and D <= 0:
            summu = normalize((A * A * abs(C)), (2 * A * abs(C) + A * A * abs(D)), (2 * A * abs(D) + abs(C)), (abs(D)), norm, A,N)
        elif C <= 0 and D >= 0:
            summu = normalize(A * A * D, (2 * A * abs(C) + D), abs(C), 0, norm, A,N)
        if summu <= k :
            temp = [summu,e,f,0]
            sum_n.append(temp) 
            e1 = e*e - f*f
            f1 = 2*e*f
            NN = e1*e1 + f1*f1
            C = e1 + A*f1
            D = f1
            if C == 0 and D == 0 :
                summu = 0
                break
            elif C >= 0 and D >= 0:
                summu = normalize(C, D, 0, 0,norm,A,NN)
            elif C >= 0 and D <= 0:
                summu = normalize(C, (A * A * abs(D)), (2 * A * abs(D)), abs(D), norm, A,NN)
            elif C <= 0 and D <= 0:
                summu = normalize((A * A * abs(C)), (2 * A * abs(C) + A * A * abs(D)), (2 * A * abs(D) + abs(C)), (abs(D)), norm, A,NN)
            elif C <= 0 and D >= 0:
                summu = normalize(A * A * D, (2 * A * abs(C) + D), abs(C), 0, norm, A,NN)
            sum_n[-1][3] = summu
sum_n.sort()
index = 0
l = sum_n[index][0]
print('For sum = ' +str(l))
print('[',end = "")
if sum_n[index][0] == sum_n[index][3] and sum_n[index][0] == l and ((sum_n[index][1] + sum_n[index][2])%2 == 1):
    print(str(sum_n[index][1]) + '+' + str(sum_n[index][2]) + 'i',end = "")
for index in range(1, len(sum_n)):
    if (sum_n[index][0] != l):
        print(']')
        l = sum_n[index][0]
        print('For sum = ' +str(l))
        print('[',end = "")
    if sum_n[index][0] == sum_n[index][3] and sum_n[index][0] == l and ((sum_n[index][1]+sum_n[index][2])%2 == 1):
        print(str(sum_n[index][1]) + '+' + str(sum_n[index][2]) + 'i',end = " ")
print(']')

