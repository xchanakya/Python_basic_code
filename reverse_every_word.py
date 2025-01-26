
def reverse_evry_word(str):
    str=str.split(" ")
    for i in str:
        print(i[-1::-1],end=" ")
    

reverse_evry_word("hello world")