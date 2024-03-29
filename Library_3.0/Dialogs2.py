import sys
from coms import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class DWindow(QMainWindow):
    def addDialog(self):
        text0,text1,text2,tex3='__0__','__0__','__0__','__0__'
        text0, ok = QInputDialog.getText(self,'Ввод параметров','Введите тему')
        if ok:
            a0=text0.replace(' ','_')
        text1, ok = QInputDialog.getText(self,'Ввод параметров','Введите название')
        if ok:
            a1=text1.replace(' ','_')
        text2, ok = QInputDialog.getText(self,'Ввод параметров','Введите автора')
        if ok:
            a2=text2.replace(' ','_')
        text3, ok = QInputDialog.getText(self,'Ввод параметров','Введите место')
        if ok:
            a3=text3.replace(' ','_')
            add(a0,a1,a2,a3)
    def exitDialog(self):
        save()
        self.close()
        f = open('caches/s_cache.txt','w')
        f.close()
        f1 = open('caches/u_cache.txt','w')
        f1.close()
        
    def searchDialog(self):
        a0,a1,a2='__0__','__0__','__0__'

        text0, ok = QInputDialog.getText(self,'Ввод параметров','Введuте тему')
        if ok:
            a0=text0.replace(' ','_')
            if a0=='':
                a0='__0__'
        text1, ok = QInputDialog.getText(self,'Ввод параметров','Введuте название')
        if ok:
            a1=text1.replace(' ','_')
            if a1=='':
                a1='__0__'
        text2, ok = QInputDialog.getText(self,'Ввод параметров','Введuте автора')
        if ok:
            a2=text2.replace(' ','_')
            if a2=='':
                a2='__0__'
        search(str(a0),str(a1),str(a2))
        f=open('caches/s_cache.txt','r')


        with f:
            data = f.read()
            self.textEdit.setText(data)
            f.close()



    def caddDialog(self):
        text0,text1,text2,tex3='__0__','__0__','__0__','__0__'
        text0, ok = QInputDialog.getText(self,'Ввод параметров','Введите тему')
        if ok:
            a0=text0.replace(' ','_')
        text1, ok = QInputDialog.getText(self,'Ввод параметров','Введите название')
        if ok:
            a1=text1.replace(' ','_')
        text2, ok = QInputDialog.getText(self,'Ввод параметров','Введите автора')
        if ok:
            a2=text2.replace(' ','_')
        text3, ok = QInputDialog.getText(self,'Ввод параметров','Введите место')
        if ok:
            a3=text3.replace(' ','_')
            cadd(a0,a1,a2,a3)
            
    def naddDialog(self):
        text0,text_0,text1,text2,tex3='__0__','__0__','__0__','__0__','__0__'
        text0, ok = QInputDialog.getText(self,'Ввод параметров','Введите номер книги')
        if ok:
            a0=text0.replace(' ','_')
        text_0, ok = QInputDialog.getText(self,'Ввод параметров','Введите тему книги')
        if ok:
            a_0=text_0.replace(' ','_')
        text1, ok = QInputDialog.getText(self,'Ввод параметров','Введите название')
        if ok:
            a1=text1.replace(' ','_')
        text2, ok = QInputDialog.getText(self,'Ввод параметров','Введите автора')
        if ok:
            a2=text2.replace(' ','_')
        text3, ok = QInputDialog.getText(self,'Ввод параметров','Введите место')
        if ok:
            a3=text3.replace(' ','_')
            nadd(a0,a_0,a1,a2,a3)

    def scDialog(self):
       f = open('base_files/cache.txt','r')

       with f:
           data = f.read()
           self.textEdit.setText(data)
           f.close()
            
    def saDialog(self):
       f = open('base_files/info.txt','r')

       with f:
           data = f.read()
           self.textEdit.setText(data)
           f.close()

    def helDialog(self):
       f = open('caches/new.txt','r')

       with f:
           data = f.read()
           self.textEdit.setText(data)
           f.close()

    def unDialog(self):
        f = open('caches/new.txt','r')
        out = []
        for line in f:
            out.append(line)
        f.close()
        
        f1 = open('caches/new.txt','w')
        for i in range(len(out)-1):
            f1.write(str(out[i]))
        f1.close()
        
        f2 = open('caches/u_cache.txt','a')
        f2.write(str(out[len(out)-1]) + '\n')
        f2.close()

    def delDialog(self):
        text, ok = QInputDialog.getText(self,'Ввод параметров','Введите номер книги')
        if ok:
            delete(str(text))

    def reDialog(self):
        out = []
        
        f = open('caches/u_cache.txt','r')
        for line in f:
            out.append(str(line))
            print(line)
        f.close()
        print(out)
        f1 = open('caches/u_cache.txt','w')
        for i in range(len(out)-1):
            f1.write(str(out[i]) + '\n')
        f1.close()

        f2 = open('caches/new.txt','a')
        f2.write(out[len(out)-1])
        f2.close()

    def chaDialog(self):
        text0,text_0,text1,text2,tex3='__0__','__0__','__0__','__0__','__0__'
        text0, ok = QInputDialog.getText(self,'Ввод старых параметров','Введите номер книги')
        if ok:
            a0=text0.replace(' ','_')
        text1, ok = QInputDialog.getText(self,'Ввод старых параметров','Введите название')
        if ok:
            a1=text1.replace(' ','_')
        text2, ok = QInputDialog.getText(self,'Ввод старых параметров','Введите автора')
        if ok:
            a2=text2.replace(' ','_')
            out = ssearch(a0,a1,a2)
        #number,topic,name,author,place=out[0],out[1],out[2],out[3],out[4]
        delete(out[0])
        
        text0, ok = QInputDialog.getText(self,'Ввод новых параметров','Введите номер книги')
        if ok:
            if text0=='':
                a0=out[0]
            else:
                a0=text0.replace(' ','_')
        text_0, ok = QInputDialog.getText(self,'Ввод новых параметров','Введите тему книги')
        if ok:
            if text_0=='':
                a_0=out[1]
            else:
                a_0=text_0.replace(' ','_')
        text1, ok = QInputDialog.getText(self,'Ввод новых параметров','Введите название')
        if ok:
            if text1=='':
                a1=out[2]
            else:
                a1=text1.replace(' ','_')
        text2, ok = QInputDialog.getText(self,'Ввод новых параметров','Введите автора')
        if ok:
            if text2=='':
                a2=out[3]
            else:
                a2=text2.replace(' ','_')
        text3, ok = QInputDialog.getText(self,'Ввод новых параметров','Введите место')
        if ok:
            if text3=='':
                a3=out[4]
            else:
                a3=text3.replace(' ','_')
            nadd(a0,a_0,a1,a2,a3)

        
        
        
        
