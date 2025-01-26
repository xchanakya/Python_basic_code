def remove_all_dup(s):
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    return l

str=remove_all_dup('aaabbbccddddd')
#convert list to string
str1=''.join(str)
print(str1)