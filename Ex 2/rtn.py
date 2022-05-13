transition_table = [ [0]*3 for _ in range(20) ]
re = input("Enter the regular expression : ")
re += " "

i = 0
j = 1
while(i<len(re)):
    if re[i] == 'a':
        try:
            if re[i+1] != '|' and re[i+1] !='*':
                transition_table[j][0] = j+1
                j += 1
            elif re[i+1] == '|' and re[i+2] =='b':
                transition_table[j][2]=((j+1)*10)+(j+3)
                j+=1
                transition_table[j][0]=j+1
                j+=1
                transition_table[j][2]=j+3
                j+=1
                transition_table[j][1]=j+1
                j+=1
                transition_table[j][2]=j+1
                j+=1
                i=i+2
            elif re[i+1]=='*':
                transition_table[j][2]=((j+1)*10)+(j+3)
                j+=1
                transition_table[j][0]=j+1
                j+=1
                transition_table[j][2]=((j+1)*10)+(j-1)
                j+=1
        except:
            transition_table[j][0] = j+1

    elif re[i] == 'b':
        try:
            if re[i+1] != '|' and re[i+1] !='*':
                transition_table[j][1] = j+1
                j += 1
            elif re[i+1]=='|' and re[i+2]=='a':
                transition_table[j][2]=((j+1)*10)+(j+3)
                j+=1
                transition_table[j][1]=j+1
                j+=1
                transition_table[j][2]=j+3
                j+=1
                transition_table[j][0]=j+1
                j+=1
                transition_table[j][2]=j+1
                j+=1
                i=i+2
            elif re[i+1]=='*':
                transition_table[j][2]=((j+1)*10)+(j+3)
                j+=1
                transition_table[j][1]=j+1
                j+=1
                transition_table[j][2]=((j+1)*10)+(j-1)
                j+=1
        except:
            transition_table[j][1] = j+1
        
    elif re[i]=='e' and re[i+1]!='|'and re[i+1]!='*':
        transition_table[j][2]=j+1
        j+=1

    elif re[i]==')' and re[i+1]=='*':

        transition_table[0][2]=((j+1)*10)+1
        transition_table[j][2]=((j+1)*10)+1
        j+=1

    i +=1

print ("\nTransition function:")
# print("s  a  b  e\n")
for i in range(j):
    if(transition_table[i][0]!=0):
        # print(("{0}  {1}  -   -".format(i,transition_table[i][0]))
        print("q[{0},a]-->{1}".format(i,transition_table[i][0]))
    if(transition_table[i][1]!=0):
        # print("{0}  -  {1}  -".format(i,transition_table[i][1]))
        print("q[{0},b]-->{1}".format(i,transition_table[i][1]))
    if(transition_table[i][2]!=0):
        if(transition_table[i][2]<10):
            # print("{0}  -  -  {1}".format(i,transition_table[i][2]))
            print("q[{0},e]-->{1}".format(i,transition_table[i][2]))
        else:
            # print("{0}  -  -  {1} & {2}".format(i,int(transition_table[i][2]/10),transition_table[i][2]%10))
            print("q[{0},e]-->{1} & {2}".format(i,int(transition_table[i][2]/10),transition_table[i][2]%10))
# print(transition_table)
def costToBuy(ratings, n):
    
    left2right = [1]*n
    right2left = [1]*n
    
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            left2right[i] = left2right[i-1] + 1
    
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            right2left[i] = right2left[i+1] + 1
    
    res = list(map(lambda x, y: max(x, y), left2right, right2left))
    print("Cost of all books: ", res)
    return sum(res)
    
ratings = list(map(int, input("Enter the ratings of 'n' bananas:\n").strip().split()))
print("\nCost to buy all books is: ", costToBuy(ratings, len(ratings)))