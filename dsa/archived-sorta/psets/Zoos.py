#You are required to enter a word that consists of  and  that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if .
#Determine if the entered word is similar to word zoo.
#For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

string = input("enter zoo: ")
def zoos(string):
    string_seperated = [x for x in string]
    z_counter = 0
    o_counter = 0

    for i in string_seperated:
        if i == 'z':
            z_counter += 1
        elif i == 'o':
            o_counter += 1
    if(z_counter * 2 == o_counter):
        print("Yes")
    else:
        print("No")
zoos(string)
