import pandas
def store(url_s, pwd_s):
    """saves the urls and passwords from url_s, pwd_s to a csv file in order to make it easier to access the database

    Args:
        url_s (str): list containg  all url_s for which passwords are saved
        pwd_s (str): list containg  all pwd_s which are saved
    """
    data_dict = {"URLs":{}, "Passwords":{}}
    for index, value in enumerate(url_s):
        data_dict["URLs"][index] = str(value)
    
    for index, value in enumerate(pwd_s):
        data_dict["Passwords"][index] = str(value)
        
    data = pandas.DataFrame.from_dict(data_dict).to_csv("data.csv")
                
def get(pwd_s, url_s):
    """pulls past additions of url_s and pwd_s to the new running of the project so user can access them

    Args:
        pwd_s (list): list containg all passwords which are saved
        url_s (list): list containg all urls fo which passwords are saved
    """
    data1 = pandas.read_csv('data.csv')

    pwd_s = data1['Passwords'].to_list()
    url_s = data1['URLs'].to_list()
    for pwd in pwd_s:
        if pwd == False:
            print('fALSE')
            
    for url in url_s:
        if url == False:
            print("fALSE")