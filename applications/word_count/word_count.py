def word_count(s):
    dic = {}
    words_raw = s.split()
    words = []
    for x in words_raw:
        new = x.lower().strip('":;,.-+=/\\|[]{}()*^&')
        words.append(new)
    u_words = set(words)
    
    for i in u_words:
            
            count = 0
            if i != "":
                for j in words:
            
                    if i == j:
                        count += 1
            
                
                dic[i]=count
    
    return dic



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    
    
print(word_count('a a\ra\na\ta \t\r\n'))