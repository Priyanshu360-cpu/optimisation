import random
populations=[]
#generating random binary numbers
for x in range(4):
    s=[]
    for y in range(6):
        s.append(random.randint(0,1))
    populations.append(s)
print(populations)
# Converting binary to decimal
def bits_to_int(bits):
    value=0
    for bit in bits:
        value=(value<<1)|bit
    return value
numeric=[]
#storing the decimal values in a list
for x in populations:
    numeric.append(bits_to_int(x))
#sorting the list for parent selection
def selection():
 for x in range(0,len(populations)):
    for y in range(0,len(populations)):
        if bits_to_int(populations[x])>bits_to_int(populations[y]):
            temp=populations[x]
            populations[x]=populations[y]
            populations[y]=temp
            numeric[x]=bits_to_int(populations[x])
            numeric[y]=bits_to_int(populations[y])
selection()
print(numeric)
populations2=[]
# one to one crossover
def crossover():
    global populations2
    r=random.randint(0,len(populations[0])-1)
    for i in range(0,len(populations),2):
     populations2.append(populations[i][0:r]+populations[i+1][r:6])
crossover()
# crossovered population
print(populations2)
bit_flip_mutation=[]
#bit flip mutation
def bit_flip():
    global bit_flip_mutation
    for i in range(0,len(populations2)):
        r=random.randint(0,len(populations2[i])-1)
        bit_flip_mutation.append(populations2[i][0:r]+[1-populations2[i][r]]+populations2[i][r+1:6])
bit_flip()
print(bit_flip_mutation)
swap_mutation=[]
#swap mutation
def swap():
    global swap_mutation
    for i in range(0,len(populations2)):
        swap_handler=[]
        # to prevent extra swaps
        while(len(swap_handler)!=6):
         r=random.randint(0,len(populations2[i])-1)
         r1=random.randint(0,len(populations2[i])-1)
         swap_handler=populations2[i][0:r]+[populations2[i][r1]]+populations2[i][r+1:r1]+[populations2[i][r]]+populations2[i][r1+1:6]
        swap_mutation.append(swap_handler)
swap()
print(swap_mutation)
inversion_mutation=[]
def inversion():
    global inversion_mutation
    for i in range(0,len(populations2)):
        inversion_handler=[]
        pop=populations2[i]
        for(x,y) in zip(pop[0:3],pop[3:6]):
            inversion_handler.append(x)
            inversion_handler.append(y)
        inversion_mutation.append(inversion_handler)
inversion()
print(inversion_mutation)
best=[0,0,0,0,0,0]
print('Comparison')
print('Population 1')
print(populations)
for x in populations:
    if(bits_to_int(best)<bits_to_int(x)):
        best=x
    print(bits_to_int(x))
print('After crossover')
print(populations2)
for x in populations2:
    if(bits_to_int(best)<bits_to_int(x)):
        best=x
    print(bits_to_int(x))
print('After bit flip mutation')
print(bit_flip_mutation)
for x in bit_flip_mutation:
    if(bits_to_int(best)<bits_to_int(x)):
        best=x
    print(bits_to_int(x))
print('After swap mutation')
print(swap_mutation)
for x in swap_mutation:
    if(bits_to_int(best)<bits_to_int(x)):
        best=x
    print(bits_to_int(x))
print('After inversion mutation')
print(inversion_mutation)
for x in inversion_mutation:
    if(bits_to_int(best)<bits_to_int(x)):
        best=x
    print(bits_to_int(x))
print('Best solution')
print("Chromosome "+str(best)+'\n'+"Numeric - "+str(bits_to_int(best)))