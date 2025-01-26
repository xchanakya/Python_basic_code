def higest_occ(s):
    freq={}

    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return max(freq,key=freq.get)

print(higest_occ('aaabbbccddddd'))