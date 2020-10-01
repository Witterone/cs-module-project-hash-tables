def histogram(file):
    with open(file, "r") as file_output:
        data = file_output.read()
        
    words = data.split()
    dic = {}
    for i in words:
        x = i.lower().strip(" : ; , . - + = / \ | [ ] { } ( ) * ^ &")
        if x not in dic:
            dic[x] = ["#"]
        else:
            dic[x].append("#")
    
    x = sorted(dic.items(), key= lambda item:len(item[1]),reverse=True)
    print(x)
        
            
    
    return dic



histogram("robin.txt")