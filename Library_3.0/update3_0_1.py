#def search(topic,name,author):
    out=[]
    mas = load()
    f = open('caches/s_cache.txt','w')
    for i in range(len(mas)-1):
        if   str(topic)==str(mas[i][1]) and str(name)==str(mas[i][2]) and str(mas[i][3]).split().count(str(author))>0:
            f.write(str(mas[i][0]) + ' ' + str(mas[i][1]) + ' ' + str(mas[i][2]) + ' ' + str(mas[i][3]) + ' ' + str(mas[i][4]) + '\n')
        elif str(topic)==str(mas[i][1]) and str(name)==str(mas[i][2]) and str(author)=='__0__'       :
            f.write(str(mas[i][0]) + ' ' + str(mas[i][1]) + ' ' + str(mas[i][2]) + ' ' + str(mas[i][3]) + ' ' + str(mas[i][4]) + '\n')
        elif str(topic)==str(mas[i][1]) and str(name)=='__0__'        and str(mas[i][3]).split().count(str(author))>0:
            f.write(str(mas[i][0]) + ' ' + str(mas[i][1]) + ' ' + str(mas[i][2]) + ' ' + str(mas[i][3]) + ' ' + str(mas[i][4]) + '\n')
        elif str(topic)=='__0__'        and str(name)==str(mas[i][2]) and str(mas[i][3]).split().count(str(author))>0:
            f.write(str(mas[i][0]) + ' ' + str(mas[i][1]) + ' ' + str(mas[i][2]) + ' ' + str(mas[i][3]) + ' ' + str(mas[i][4]) + '\n')
        elif str(topic)=='__0__'        and str(name)==str(mas[i][2]) and str(author)=='__0__'       :
            f.write(str(mas[i][0]) + ' ' + str(mas[i][1]) + ' ' + str(mas[i][2]) + ' ' + str(mas[i][3]) + ' ' + str(mas[i][4]) + '\n')
        elif str(topic)==str(mas[i][1]) and str(name)=='__0__'        and str(author)=='__0__'       :
            f.write(str(mas[i][0]) + ' ' + str(mas[i][1]) + ' ' + str(mas[i][2]) + ' ' + str(mas[i][3]) + ' ' + str(mas[i][4]) + '\n')
        elif str(topic)=='__0__'        and str(name)=='__0__'        and str(mas[i][3]).split().count(str(author))>0:
            f.write(str(mas[i][0]) + ' ' + str(mas[i][1]) + ' ' + str(mas[i][2]) + ' ' + str(mas[i][3]) + ' ' + str(mas[i][4]) + '\n')
        elif str(topic)=='__0__'        and str(name)=='__0__'        and str(author)=='__0__'       :
            f.write(str(mas[i][0]) + ' ' + str(mas[i][1]) + ' ' + str(mas[i][2]) + ' ' + str(mas[i][3]) + ' ' + str(mas[i][4]) + '\n')
    f.close()
