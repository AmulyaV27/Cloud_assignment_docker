import os
from collections import Counter
import socket

p = "/home/data"

os.chdir(p)

def read_text_file(path_file):
    with open(path_file, 'rt') as f:
        return f.read()
with open("/home/output/result.txt","w") as f:
    for file in os.listdir():
        if file.endswith(".txt"):
            f.write(file+"\n")

    cnt=0
    for file in os.listdir():
        f.write("Number of Words in {} : ".format(file))
        if file.endswith(".txt"):
                file_p = f"{p}/{file}"
                rf = read_text_file(file_p)
                wordslist = rf.split()
        cnt=cnt+len(wordslist)
        f.write(f'{len(wordslist)} \n')
        if file == "IF.txt":
            IF_words=wordslist

    f.write("Total number of words in  both files : {} \n".format(cnt))

    frequency = {}
    for i in IF_words:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    l = Counter(frequency)
    high_w = l.most_common(3)
    for i in high_w:
        f.write(f'{i[0]}: {i[1]}\n')

    f.write("IP address: "+"\n")
    f.write(socket.gethostbyname(socket.gethostname())+"\n")
result=read_text_file("/home/output/result.txt")
print(result)
