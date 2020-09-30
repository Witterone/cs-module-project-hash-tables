def no_dups(s):
    l_s = s.split()
    
    words = ""
    used = {}
    for i in l_s:
        if i not in used:
            words = words+str(i)+" "
            used[i] = 1
        
    return str(words.strip(" "))



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))