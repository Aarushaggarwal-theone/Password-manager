
def store(url_s, pwd_s):
    data = open('database.txt', "w")
    for url in url_s:
        for pwd in pwd_s:
            if pwd_s[url_s.index(url)] == pwd:
                data.write(f"{url}:{pwd}\n")
                
def get(pwd_s, url_s):
    
    final_list = []
    data = open("database.txt", "r")
    
    content = data.readlines()
    for i in content:
        var1 = i.split(':')[0]
        var3 = var1.strip()
        var2 = i.split(":")[1].strip()
        url_s.append(var3)
        pwd_s.append(var2)
    
                