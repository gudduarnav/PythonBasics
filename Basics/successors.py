import re

def getwords(txt):
    wordlist = list()
    word = None
    for ch in txt:
        if word is None:
            word = ch
        elif ch ==  " " or ch ==  "\n":
            wordlist.append(word.strip())
            word = None
        elif ch== "." or ch=="!" or ch==",":
            wordlist.append(word.strip())
            word = None
            wordlist.append(ch)
        else:
            word = word+ch

    return wordlist

def successors(txt):
    toks = getwords(txt)
    ntoks = len(toks)
    d = dict()
    for index in range(ntoks):
        now = toks[index]
        if (index+1)<ntoks:
            next = toks[index+1]
            if now in d.keys():
                if not (next in d[now]):
                    d[now].append(next)
            else:
                d[now] = [next]
    return d

    return getwords(txt)


f = open("successorsinput.txt", "r")
txt = f.read().strip()
f.close()

print(successors(txt)["."])
print(successors(txt)["to"])
print(successors(txt)["fun"])
print(successors(txt)[","])
print(successors(txt))
