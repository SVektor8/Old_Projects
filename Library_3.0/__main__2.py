from Dialogs import *

class Window(DWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(0, 0, 1350, 670)
        self.setWindowTitle('Book base')             
        self.show()

        exitAction = QAction(QIcon('badges/exit.png'),'&Save and exit',self)  
        exitAction.setShortcut('Ctrl+Q')                                
        exitAction.setStatusTip('Сохранить и выйти')
        exitAction.triggered.connect(self.exitDialog)                               

        saveAction = QAction(QIcon('badges/save.png'),'&Save',self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Сохранить изменения')
        saveAction.triggered.connect(save)

        searchAction = QAction(QIcon('badges/search.png'),'&Search',self)
        searchAction.setShortcut('Ctrl+F')
        searchAction.setStatusTip('Искать')
        searchAction.triggered.connect(self.searchDialog)

        addAction = QAction(QIcon('badges/add.png'),'&Add',self)
        addAction.setShortcut('Ctrl+A')
        addAction.setStatusTip('Добавить произведение')
        addAction.triggered.connect(self.addDialog)

        caddAction = QAction(QIcon('badges/cadd.png'),'&Cadd',self)
        caddAction.setShortcut('Ctrl+J')
        caddAction.setStatusTip('Добавить произведение в последнюю книгу')
        caddAction.triggered.connect(self.caddDialog)

        naddAction = QAction(QIcon('badges/nadd.png'),'&Nadd',self)
        naddAction.setShortcut('Ctrl+N')
        naddAction.setStatusTip('Добавить произведение в книгу с выбранным номером')
        naddAction.triggered.connect(self.naddDialog)

        scacheAction = QAction(QIcon('badges/scache.png'),'&Show cache',self)
        scacheAction.setStatusTip('Показать кэш')
        scacheAction.triggered.connect(self.scDialog)

        ccacheAction = QAction(QIcon('badges/ccache.png'),'&Clear cache',self)
        ccacheAction.setStatusTip('Очиистить кэш')
        ccacheAction.triggered.connect(clearcache)

        sallAction = QAction(QIcon('badges/sall.png'),'&Show base',self)
        sallAction.setStatusTip('Показать базу книг')
        sallAction.triggered.connect(self.saDialog)

        callAction = QAction(QIcon('badges/call.png'),'&Clear base',self)
        callAction.setStatusTip('Очистить базу книг')
        callAction.triggered.connect(clearall)

        helAction = QAction(QIcon('badges/hel.png'),'&Show file',self)
        helAction.setStatusTip('Показать вспомогательный файл')
        helAction.triggered.connect(self.helDialog)

        undoAction = QAction(QIcon('badges/undo.png'),'&Undo',self)
        undoAction.setStatusTip('Отменить последнее действие')
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.unDialog)

        redoAction = QAction(QIcon('badges/redo.png'),'&Redo',self)
        redoAction.setStatusTip('Повторить отменённое действие')
        redoAction.setShortcut('Ctrl+Shift+Z')
        #redoAction.triggered.connect(self.reDialog)

        deleteAction = QAction(QIcon('badges/del.png'),'&Delete',self)
        deleteAction.setStatusTip('Удалить книгу')
        deleteAction.setShortcut('Ctrl+delete')
        deleteAction.triggered.connect(self.delDialog)

        changeAction = QAction(QIcon('badges/change.png'),'&Change',self)
        changeAction.setShortcut('Ctrl+R')
        changeAction.setStatusTip('Изменить произведение')
        changeAction.triggered.connect(self.chaDialog)
        
        

        self.toolbar=self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar=self.addToolBar('Search')
        self.toolbar.addAction(searchAction)
        self.toolbar=self.addToolBar('Add')
        self.toolbar.addAction(addAction)
        self.toolbar=self.addToolBar('Delete')
        self.toolbar.addAction(deleteAction)
        self.toolbar=self.addToolBar('Change')
        self.toolbar.addAction(changeAction)


        self.textEdit = QTextEdit()            
        self.setCentralWidget(self.textEdit)




        menubar = self.menuBar()             
        
        fileMenu = menubar.addMenu('&File')     
        fileMenu.addAction(exitAction)              
        fileMenu.addAction(undoAction)
        fileMenu.addAction(redoAction)
        fileMenu.addAction(saveAction)

        addMenu = menubar.addMenu('&Add')
        addMenu.addAction(addAction)
        addMenu.addAction(caddAction)
        addMenu.addAction(naddAction)

        settMenu = menubar.addMenu('&Special Settings')
        settMenu.addAction(scacheAction)
        settMenu.addAction(ccacheAction)
        settMenu.addAction(sallAction)
        settMenu.addAction(callAction)
        settMenu.addAction(helAction)
        


        self.statusBar()       
        self.statusBar().showMessage('Добро пожаловать!')  



if __name__ == '__main__' :
    app=QApplication(sys.argv)
    ex=Window()
    sys.exit(app.exec_())




    

