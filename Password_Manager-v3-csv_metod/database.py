import pandas
def store(url_s, pwd_s):
    data_dict = {"URLs":{}, "Passwords":{}}
    for index, value in enumerate(url_s):
        data_dict["URLs"][index] = str(value)
    
    for index, value in enumerate(pwd_s):
        data_dict["Passwords"][index] = str(value)
        
    data = pandas.DataFrame.from_dict(data_dict).to_csv("data.csv")
                
def get(pwd_s, url_s):
    data1 = pandas.read_csv('data.csv')

    pwd_s = data1['Passwords'].to_list()
    url_s = data1['URLs'].to_list()