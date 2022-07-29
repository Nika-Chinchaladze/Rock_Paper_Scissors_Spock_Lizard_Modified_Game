from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QPoint
from random import choice


class Ui_Animation_Game(object):
    def setupUi(self, Animation_Game):
        Animation_Game.setObjectName("Animation_Game")
        Animation_Game.resize(861, 630)
        
        self.centralwidget = QtWidgets.QWidget(Animation_Game)
        self.centralwidget.setObjectName("centralwidget")
        
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(10, 10, 841, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.welcome_label.setFont(font)
        self.welcome_label.setFrameShape(QtWidgets.QFrame.Box)
        self.welcome_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(70, 50, 731, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.start_button.setObjectName("start_button")
        
        self.computer_label = QtWidgets.QLabel(self.centralwidget)
        self.computer_label.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.computer_label.setFont(font)
        self.computer_label.setFrameShape(QtWidgets.QFrame.Box)
        self.computer_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.computer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.computer_label.setObjectName("computer_label")

        self.rule_label = QtWidgets.QLabel(self.centralwidget)
        self.rule_label.setGeometry(QtCore.QRect(160, 100, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rule_label.setFont(font)
        self.rule_label.setFrameShape(QtWidgets.QFrame.Box)
        self.rule_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rule_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rule_label.setObjectName("rule_label")
        
        self.player_label = QtWidgets.QLabel(self.centralwidget)
        self.player_label.setGeometry(QtCore.QRect(650, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.player_label.setFont(font)
        self.player_label.setFrameShape(QtWidgets.QFrame.Box)
        self.player_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.player_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_label.setObjectName("player_label")
        
        self.rock_first = QtWidgets.QLabel(self.centralwidget)
        self.rock_first.setGeometry(QtCore.QRect(25, 140, 80, 40))
        self.rock_first.setFrameShape(QtWidgets.QFrame.Box)
        self.rock_first.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rock_first.setText("")
        self.rock_first.setPixmap(QtGui.QPixmap("rock2.jpg"))
        self.rock_first.setScaledContents(True)
        self.rock_first.setObjectName("rock_first")
        
        self.paper_first = QtWidgets.QLabel(self.centralwidget)
        self.paper_first.setGeometry(QtCore.QRect(25, 190, 80, 40))
        self.paper_first.setFrameShape(QtWidgets.QFrame.Box)
        self.paper_first.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.paper_first.setText("")
        self.paper_first.setPixmap(QtGui.QPixmap("paper2.jpg"))
        self.paper_first.setScaledContents(True)
        self.paper_first.setObjectName("paper_first")
        
        self.scissors_first = QtWidgets.QLabel(self.centralwidget)
        self.scissors_first.setGeometry(QtCore.QRect(25, 240, 80, 40))
        self.scissors_first.setFrameShape(QtWidgets.QFrame.Box)
        self.scissors_first.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scissors_first.setText("")
        self.scissors_first.setPixmap(QtGui.QPixmap("scissors2.jpg"))
        self.scissors_first.setScaledContents(True)
        self.scissors_first.setObjectName("scissors_first")
        
        self.spock_first = QtWidgets.QLabel(self.centralwidget)
        self.spock_first.setGeometry(QtCore.QRect(25, 290, 80, 40))
        self.spock_first.setFrameShape(QtWidgets.QFrame.Box)
        self.spock_first.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.spock_first.setText("")
        self.spock_first.setPixmap(QtGui.QPixmap("spock2.jpg"))
        self.spock_first.setScaledContents(True)
        self.spock_first.setObjectName("spock_first")

        self.lizard_first = QtWidgets.QLabel(self.centralwidget)
        self.lizard_first.setGeometry(QtCore.QRect(25, 340, 80, 60))
        self.lizard_first.setFrameShape(QtWidgets.QFrame.Box)
        self.lizard_first.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lizard_first.setText("")
        self.lizard_first.setPixmap(QtGui.QPixmap("lizard2.jpg"))
        self.lizard_first.setScaledContents(True)
        self.lizard_first.setObjectName("lizard_first")
        
        self.rock_second = QtWidgets.QLabel(self.centralwidget)
        self.rock_second.setGeometry(QtCore.QRect(667, 140, 80, 40))
        self.rock_second.setFrameShape(QtWidgets.QFrame.Box)
        self.rock_second.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rock_second.setText("")
        self.rock_second.setPixmap(QtGui.QPixmap("rock1.jpg"))
        self.rock_second.setScaledContents(True)
        self.rock_second.setObjectName("rock_second")
        
        self.paper_second = QtWidgets.QLabel(self.centralwidget)
        self.paper_second.setGeometry(QtCore.QRect(667, 190, 80, 40))
        self.paper_second.setFrameShape(QtWidgets.QFrame.Box)
        self.paper_second.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.paper_second.setText("")
        self.paper_second.setPixmap(QtGui.QPixmap("paper1.jpg"))
        self.paper_second.setScaledContents(True)
        self.paper_second.setObjectName("paper_second")

        self.scissors_second = QtWidgets.QLabel(self.centralwidget)
        self.scissors_second.setGeometry(QtCore.QRect(667, 240, 80, 40))
        self.scissors_second.setFrameShape(QtWidgets.QFrame.Box)
        self.scissors_second.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scissors_second.setText("")
        self.scissors_second.setPixmap(QtGui.QPixmap("scissors1.jpg"))
        self.scissors_second.setScaledContents(True)
        self.scissors_second.setObjectName("scissors_second")

        self.spock_second = QtWidgets.QLabel(self.centralwidget)
        self.spock_second.setGeometry(QtCore.QRect(667, 290, 80, 40))
        self.spock_second.setFrameShape(QtWidgets.QFrame.Box)
        self.spock_second.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.spock_second.setText("")
        self.spock_second.setPixmap(QtGui.QPixmap("spock1.jpg"))
        self.spock_second.setScaledContents(True)
        self.spock_second.setObjectName("spock_second")

        self.lizard_second = QtWidgets.QLabel(self.centralwidget)
        self.lizard_second.setGeometry(QtCore.QRect(667, 340, 80, 60))
        self.lizard_second.setFrameShape(QtWidgets.QFrame.Box)
        self.lizard_second.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lizard_second.setText("")
        self.lizard_second.setPixmap(QtGui.QPixmap("lizard1.jpg"))
        self.lizard_second.setScaledContents(True)
        self.lizard_second.setObjectName("lizard_second")
        
        self.rock_button = QtWidgets.QPushButton(self.centralwidget)
        self.rock_button.setGeometry(QtCore.QRect(770, 145, 81, 30))
        self.rock_button.setObjectName("rock_button")
        self.rock_button.setEnabled(False)
        
        self.paper_button = QtWidgets.QPushButton(self.centralwidget)
        self.paper_button.setGeometry(QtCore.QRect(770, 194, 81, 30))
        self.paper_button.setObjectName("paper_button")
        self.paper_button.setEnabled(False)
        
        self.scissor_button = QtWidgets.QPushButton(self.centralwidget)
        self.scissor_button.setGeometry(QtCore.QRect(770, 244, 81, 30))
        self.scissor_button.setObjectName("scissor_button")
        self.scissor_button.setEnabled(False)

        self.spock_button = QtWidgets.QPushButton(self.centralwidget)
        self.spock_button.setGeometry(QtCore.QRect(770, 293, 81, 30))
        self.spock_button.setObjectName("spock_button")
        self.spock_button.setEnabled(False)

        self.lizard_button = QtWidgets.QPushButton(self.centralwidget)
        self.lizard_button.setGeometry(QtCore.QRect(770, 355, 81, 30))
        self.lizard_button.setObjectName("lizard_button")
        self.lizard_button.setEnabled(False)

        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(667, 410, 184, 30))
        self.return_button.setObjectName("return_button")
        self.return_button.setEnabled(False)
        
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 455, 841, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_label.setFont(font)
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_label.setText("")
        self.output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label.setWordWrap(True)
        self.output_label.setObjectName("output_label")
        
        self.c_label = QtWidgets.QLabel(self.centralwidget)
        self.c_label.setGeometry(QtCore.QRect(10, 515, 110, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.c_label.setFont(font)
        self.c_label.setObjectName("c_label")
        
        self.p_label = QtWidgets.QLabel(self.centralwidget)
        self.p_label.setGeometry(QtCore.QRect(680, 515, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p_label.setFont(font)
        self.p_label.setObjectName("p_label")
        
        self.comp_result = QtWidgets.QLabel(self.centralwidget)
        self.comp_result.setGeometry(QtCore.QRect(130, 515, 71, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comp_result.setFont(font)
        self.comp_result.setFrameShape(QtWidgets.QFrame.Box)
        self.comp_result.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.comp_result.setText("")
        self.comp_result.setAlignment(QtCore.Qt.AlignCenter)
        self.comp_result.setObjectName("comp_result")
        
        self.player_result = QtWidgets.QLabel(self.centralwidget)
        self.player_result.setGeometry(QtCore.QRect(780, 515, 71, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.player_result.setFont(font)
        self.player_result.setFrameShape(QtWidgets.QFrame.Box)
        self.player_result.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.player_result.setText("")
        self.player_result.setAlignment(QtCore.Qt.AlignCenter)
        self.player_result.setObjectName("player_result")
        
        self.vs_label = QtWidgets.QLabel(self.centralwidget)
        self.vs_label.setGeometry(QtCore.QRect(370, 240, 35, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vs_label.setFont(font)
        self.vs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vs_label.setObjectName("vs_label")

# ------------------------------- SECRET LABELS ------------------------------------- #
        self.p_moved_label = QtWidgets.QLabel(self.centralwidget)
        self.p_moved_label.setGeometry(QtCore.QRect(700, 580, 41, 20))
        self.p_moved_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.p_moved_label.setObjectName("p_moved_label")

        self.com_moved_label = QtWidgets.QLabel(self.centralwidget)
        self.com_moved_label.setGeometry(QtCore.QRect(100, 580, 41, 20))
        self.com_moved_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.com_moved_label.setObjectName("com_moved_label")

# ----------------------------------------------------------------------------------- #
        
        self.restart_button = QtWidgets.QPushButton(self.centralwidget)
        self.restart_button.setGeometry(QtCore.QRect(300, 570, 111, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.restart_button.setFont(font)
        self.restart_button.setStyleSheet("background-color: rgb(189, 189, 142);")
        self.restart_button.setObjectName("restart_button")
        self.restart_button.setEnabled(False)
        
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(430, 570, 111, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.exit_button.setObjectName("exit_button")
        
        Animation_Game.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Animation_Game)
        self.statusbar.setObjectName("statusbar")
        Animation_Game.setStatusBar(self.statusbar)

        self.retranslateUi(Animation_Game)
        QtCore.QMetaObject.connectSlotsByName(Animation_Game)

# -------------------------------------- LOGIC ------------------------------------------ #
        # Define Nesessary Variables: List For Computer's Answer, Player's score counter and Computer's score counter:
        self.Computer_Answer = ["rock", "paper", "scissors", "spock", "lizard"]
        self.player_score = 0
        self.computer_score = 0
        
        # call methods from here:
        self.start_button.clicked.connect(self.Start_Game)
        self.rock_button.clicked.connect(self.SendRock)
        self.rock_button.clicked.connect(self.Result)
        self.rock_button.clicked.connect(self.Winner)

        self.paper_button.clicked.connect(self.SendPaper)
        self.paper_button.clicked.connect(self.Result)
        self.paper_button.clicked.connect(self.Winner)

        self.scissor_button.clicked.connect(self.SendScissor)
        self.scissor_button.clicked.connect(self.Result)
        self.scissor_button.clicked.connect(self.Winner)

        self.spock_button.clicked.connect(self.SendSpock)
        self.spock_button.clicked.connect(self.Result)
        self.spock_button.clicked.connect(self.Winner)

        self.lizard_button.clicked.connect(self.SendLizard)
        self.lizard_button.clicked.connect(self.Result)
        self.lizard_button.clicked.connect(self.Winner)

        self.return_button.clicked.connect(self.ComeBack)
        self.restart_button.clicked.connect(self.Restart_Results)
        self.exit_button.clicked.connect(Animation_Game.close)

    # define method for disabled buttons:
    def Start_Game(self):
        self.rock_button.setEnabled(True)
        self.paper_button.setEnabled(True)
        self.scissor_button.setEnabled(True)
        self.spock_button.setEnabled(True)
        self.lizard_button.setEnabled(True)
        self.return_button.setEnabled(True)
        self.restart_button.setEnabled(True)
        self.start_button.setEnabled(False)
    
    # define method to send rock button:
    def SendRock(self):
        self.p_moved_label.setText("1")
        
        self.animation = QPropertyAnimation(self.rock_second, b"pos")
        self.animation.setStartValue(QPoint(667, 140))
        self.animation.setEndValue(QPoint(405, 238))
        self.animation.setDuration(1500)
        self.animation.start()

        Answer = choice(self.Computer_Answer)
        if Answer == "rock":
            self.com_moved_label.setText("r")
            self.anim = QPropertyAnimation(self.rock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 140))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "paper":
            self.com_moved_label.setText("p")
            self.anim = QPropertyAnimation(self.paper_first, b"pos")
            self.anim.setStartValue(QPoint(25, 190))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "scissors":
            self.com_moved_label.setText("s")
            self.anim = QPropertyAnimation(self.scissors_first, b"pos")
            self.anim.setStartValue(QPoint(25, 240))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "spock":
            self.com_moved_label.setText("ck")
            self.anim = QPropertyAnimation(self.spock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 290))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "lizard":
            self.com_moved_label.setText("l")
            self.anim = QPropertyAnimation(self.lizard_first, b"pos")
            self.anim.setStartValue(QPoint(25, 340))
            self.anim.setEndValue(QPoint(290, 227))
            self.anim.setDuration(1500)
            self.anim.start()
        
        self.rock_button.setEnabled(False)
        self.paper_button.setEnabled(False)
        self.scissor_button.setEnabled(False)
        self.spock_button.setEnabled(False)
        self.lizard_button.setEnabled(False)

    
    # define method to send paper button:
    def SendPaper(self):
        self.p_moved_label.setText("2")

        self.animation = QPropertyAnimation(self.paper_second, b"pos")
        self.animation.setStartValue(QPoint(667, 190))
        self.animation.setEndValue(QPoint(405, 238))
        self.animation.setDuration(1500)
        self.animation.start()

        Answer = choice(self.Computer_Answer)
        if Answer == "rock":
            self.com_moved_label.setText("r")
            self.anim = QPropertyAnimation(self.rock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 140))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "paper":
            self.com_moved_label.setText("p")
            self.anim = QPropertyAnimation(self.paper_first, b"pos")
            self.anim.setStartValue(QPoint(25, 190))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "scissors":
            self.com_moved_label.setText("s")
            self.anim = QPropertyAnimation(self.scissors_first, b"pos")
            self.anim.setStartValue(QPoint(25, 240))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "spock":
            self.com_moved_label.setText("ck")
            self.anim = QPropertyAnimation(self.spock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 290))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "lizard":
            self.com_moved_label.setText("l")
            self.anim = QPropertyAnimation(self.lizard_first, b"pos")
            self.anim.setStartValue(QPoint(25, 340))
            self.anim.setEndValue(QPoint(290, 227))
            self.anim.setDuration(1500)
            self.anim.start()
        
        self.rock_button.setEnabled(False)
        self.paper_button.setEnabled(False)
        self.scissor_button.setEnabled(False)
        self.spock_button.setEnabled(False)
        self.lizard_button.setEnabled(False)
    
    # define method to send scissor button:
    def SendScissor(self):
        self.p_moved_label.setText("3")

        self.animation = QPropertyAnimation(self.scissors_second, b"pos")
        self.animation.setStartValue(QPoint(667, 240))
        self.animation.setEndValue(QPoint(405, 238))
        self.animation.setDuration(1500)
        self.animation.start()

        Answer = choice(self.Computer_Answer)
        if Answer == "rock":
            self.com_moved_label.setText("r")
            self.anim = QPropertyAnimation(self.rock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 140))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "paper":
            self.com_moved_label.setText("p")
            self.anim = QPropertyAnimation(self.paper_first, b"pos")
            self.anim.setStartValue(QPoint(25, 190))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "scissors":
            self.com_moved_label.setText("s")
            self.anim = QPropertyAnimation(self.scissors_first, b"pos")
            self.anim.setStartValue(QPoint(25, 240))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "spock":
            self.com_moved_label.setText("ck")
            self.anim = QPropertyAnimation(self.spock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 290))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "lizard":
            self.com_moved_label.setText("l")
            self.anim = QPropertyAnimation(self.lizard_first, b"pos")
            self.anim.setStartValue(QPoint(25, 340))
            self.anim.setEndValue(QPoint(290, 227))
            self.anim.setDuration(1500)
            self.anim.start()
        
        self.rock_button.setEnabled(False)
        self.paper_button.setEnabled(False)
        self.scissor_button.setEnabled(False)
        self.spock_button.setEnabled(False)
        self.lizard_button.setEnabled(False)
    
    # define method for send pock button:
    def SendSpock(self):
        self.p_moved_label.setText("4")

        self.animation = QPropertyAnimation(self.spock_second, b"pos")
        self.animation.setStartValue(QPoint(667, 290))
        self.animation.setEndValue(QPoint(405, 238))
        self.animation.setDuration(1500)
        self.animation.start()

        Answer = choice(self.Computer_Answer)
        if Answer == "rock":
            self.com_moved_label.setText("r")
            self.anim = QPropertyAnimation(self.rock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 140))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "paper":
            self.com_moved_label.setText("p")
            self.anim = QPropertyAnimation(self.paper_first, b"pos")
            self.anim.setStartValue(QPoint(25, 190))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "scissors":
            self.com_moved_label.setText("s")
            self.anim = QPropertyAnimation(self.scissors_first, b"pos")
            self.anim.setStartValue(QPoint(25, 240))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "spock":
            self.com_moved_label.setText("ck")
            self.anim = QPropertyAnimation(self.spock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 290))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "lizard":
            self.com_moved_label.setText("l")
            self.anim = QPropertyAnimation(self.lizard_first, b"pos")
            self.anim.setStartValue(QPoint(25, 340))
            self.anim.setEndValue(QPoint(290, 227))
            self.anim.setDuration(1500)
            self.anim.start()
        
        self.rock_button.setEnabled(False)
        self.paper_button.setEnabled(False)
        self.scissor_button.setEnabled(False)
        self.spock_button.setEnabled(False)
        self.lizard_button.setEnabled(False)
    
    # define method for send lizard button:
    def SendLizard(self):
        self.p_moved_label.setText("5")

        self.animation = QPropertyAnimation(self.lizard_second, b"pos")
        self.animation.setStartValue(QPoint(667, 340))
        self.animation.setEndValue(QPoint(405, 227))
        self.animation.setDuration(1500)
        self.animation.start()

        Answer = choice(self.Computer_Answer)
        if Answer == "rock":
            self.com_moved_label.setText("r")
            self.anim = QPropertyAnimation(self.rock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 140))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "paper":
            self.com_moved_label.setText("p")
            self.anim = QPropertyAnimation(self.paper_first, b"pos")
            self.anim.setStartValue(QPoint(25, 190))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "scissors":
            self.com_moved_label.setText("s")
            self.anim = QPropertyAnimation(self.scissors_first, b"pos")
            self.anim.setStartValue(QPoint(25, 240))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "spock":
            self.com_moved_label.setText("ck")
            self.anim = QPropertyAnimation(self.spock_first, b"pos")
            self.anim.setStartValue(QPoint(25, 290))
            self.anim.setEndValue(QPoint(290, 238))
            self.anim.setDuration(1500)
            self.anim.start()
        elif Answer == "lizard":
            self.com_moved_label.setText("l")
            self.anim = QPropertyAnimation(self.lizard_first, b"pos")
            self.anim.setStartValue(QPoint(25, 340))
            self.anim.setEndValue(QPoint(290, 227))
            self.anim.setDuration(1500)
            self.anim.start()
        
        self.rock_button.setEnabled(False)
        self.paper_button.setEnabled(False)
        self.scissor_button.setEnabled(False)
        self.spock_button.setEnabled(False)
        self.lizard_button.setEnabled(False)
    
    # define method for Come Back button:
    def ComeBack(self):
        screen = self.p_moved_label.text()
        if screen == "1":
            self.animation = QPropertyAnimation(self.rock_second, b"pos")
            self.animation.setStartValue(QPoint(405, 238))
            self.animation.setEndValue(QPoint(667, 140))
            self.animation.setDuration(1500)
            self.animation.start()
        elif screen == "2":
            self.animation = QPropertyAnimation(self.paper_second, b"pos")
            self.animation.setStartValue(QPoint(405, 238))
            self.animation.setEndValue(QPoint(667, 190))
            self.animation.setDuration(1500)
            self.animation.start()
        elif screen == "3":
            self.animation = QPropertyAnimation(self.scissors_second, b"pos")
            self.animation.setStartValue(QPoint(405, 238))
            self.animation.setEndValue(QPoint(667, 240))
            self.animation.setDuration(1500)
            self.animation.start()
        elif screen == "4":
            self.animation = QPropertyAnimation(self.spock_second, b"pos")
            self.animation.setStartValue(QPoint(405, 238))
            self.animation.setEndValue(QPoint(667, 290))
            self.animation.setDuration(1500)
            self.animation.start()
        elif screen == "5":
            self.animation = QPropertyAnimation(self.lizard_second, b"pos")
            self.animation.setStartValue(QPoint(405, 227))
            self.animation.setEndValue(QPoint(667, 340))
            self.animation.setDuration(1500)
            self.animation.start()
        
        computer_answer = self.com_moved_label.text()
        if computer_answer == "r":
            self.anim = QPropertyAnimation(self.rock_first, b"pos")
            self.anim.setStartValue(QPoint(290, 238))
            self.anim.setEndValue(QPoint(25, 140))
            self.anim.setDuration(1500)
            self.anim.start()
        elif computer_answer == "p":
            self.anim = QPropertyAnimation(self.paper_first, b"pos")
            self.anim.setStartValue(QPoint(290, 238))
            self.anim.setEndValue(QPoint(25, 190))
            self.anim.setDuration(1500)
            self.anim.start()
        elif computer_answer == "s":
            self.anim = QPropertyAnimation(self.scissors_first, b"pos")
            self.anim.setStartValue(QPoint(290, 238))
            self.anim.setEndValue(QPoint(25, 240))
            self.anim.setDuration(1500)
            self.anim.start()
        elif computer_answer == "ck":
            self.anim = QPropertyAnimation(self.spock_first, b"pos")
            self.anim.setStartValue(QPoint(290, 238))
            self.anim.setEndValue(QPoint(25, 290))
            self.anim.setDuration(1500)
            self.anim.start()
        elif computer_answer == "l":
            self.anim = QPropertyAnimation(self.lizard_first, b"pos")
            self.anim.setStartValue(QPoint(290, 227))
            self.anim.setEndValue(QPoint(25, 340))
            self.anim.setDuration(1500)
            self.anim.start()
        
        self.p_moved_label.setText("")
        self.com_moved_label.setText("")

        self.rock_button.setEnabled(True)
        self.paper_button.setEnabled(True)
        self.scissor_button.setEnabled(True)
        self.spock_button.setEnabled(True)
        self.lizard_button.setEnabled(True)
    
    # define method for output label:
    def Result(self):
        comp_bet = self.com_moved_label.text()
        player_bet = self.p_moved_label.text()

        if player_bet == "1" and comp_bet == "r":
            self.output_label.setText("Results Are Equal, Try Again!")
            self.output_label.setStyleSheet("background-color: rgb(193, 193, 145);")
        elif player_bet == "1" and comp_bet == "p":
            self.output_label.setText("Paper Covers Rock, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        elif player_bet == "1" and comp_bet == "s":
            self.output_label.setText("Rock Crushes Scissors, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        elif player_bet == "1" and comp_bet == "ck":
            self.output_label.setText("Spock Vaporizes Rock, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        elif player_bet == "1" and comp_bet == "l":
            self.output_label.setText("Rock Crushes Lizard, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        
        elif player_bet == "2" and comp_bet == "r":
            self.output_label.setText("Paper Covers Rock, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        elif player_bet == "2" and comp_bet == "p":
            self.output_label.setText("Results Are Equal, Try Again!")
            self.output_label.setStyleSheet("background-color: rgb(193, 193, 145);")
        elif player_bet == "2" and comp_bet == "s":
            self.output_label.setText("Scissors Cuts Paper, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        elif player_bet == "2" and comp_bet == "ck":
            self.output_label.setText("Paper Disproves Spock, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        elif player_bet == "2" and comp_bet == "l":
            self.output_label.setText("Lizard Eats Paper, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        
        elif player_bet == "3" and comp_bet == "r":
            self.output_label.setText("Rock Crushes Scissors, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        elif player_bet == "3" and comp_bet == "p":
            self.output_label.setText("Scissors Cuts Paper, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        elif player_bet == "3" and comp_bet == "s":
            self.output_label.setText("Results Are Equal, Try Again!")
            self.output_label.setStyleSheet("background-color: rgb(193, 193, 145);")
        elif player_bet == "3" and comp_bet == "ck":
            self.output_label.setText("Spock Smashes Scissors, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        elif player_bet == "3" and comp_bet == "l":
            self.output_label.setText("Scissors Decapitates Lizard, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        
        elif player_bet == "4" and comp_bet == "r":
            self.output_label.setText("Spock Vaporizes Rock, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        elif player_bet == "4" and comp_bet == "p":
            self.output_label.setText("Paper Disproves Spock, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        elif player_bet == "4" and comp_bet == "s":
            self.output_label.setText("Spock Smashes Scissors, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        elif player_bet == "4" and comp_bet == "ck":
            self.output_label.setText("Results Are Equal, Try Again!")
            self.output_label.setStyleSheet("background-color: rgb(193, 193, 145);")
        elif player_bet == "4" and comp_bet == "l":
            self.output_label.setText("Lizard Poisons Spock, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        
        elif player_bet == "5" and comp_bet == "r":
            self.output_label.setText("Rock Crushes Lizard, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        elif player_bet == "5" and comp_bet == "p":
            self.output_label.setText("Lizard Eats Paper, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        elif player_bet == "5" and comp_bet == "s":
            self.output_label.setText("Scissors Decapitates Lizard, One Score To Computer!")
            self.output_label.setStyleSheet("background-color: rgb(200, 85, 86);")
            self.computer_score += 1
            self.comp_result.setText(f'{self.computer_score}')
        elif player_bet == "5" and comp_bet == "ck":
            self.output_label.setText("Lizard Poisons Spock, One Score To Player!")
            self.output_label.setStyleSheet("background-color: rgb(0, 204, 204);")
            self.player_score += 1
            self.player_result.setText(f'{self.player_score}')
        elif player_bet == "5" and comp_bet == "l":
            self.output_label.setText("Results Are Equal, Try Again!")
            self.output_label.setStyleSheet("background-color: rgb(193, 193, 145);")
    
    # define method for restart button:
    def Restart_Results(self):
        self.player_result.setText("")
        self.comp_result.setText("")
        self.output_label.setText("Game Is Restarted, Let's Play Again!")
        self.output_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.player_score = 0
        self.computer_score = 0
        self.return_button.setEnabled(True)
    
    # define method to see who won the game:
    def Winner(self):
        PlayerResult = self.player_result.text()
        ComputerResult = self.comp_result.text()
        if PlayerResult == "5":
            self.output_label.setText("Congratulations, You Won The Game!")
            self.output_label.setStyleSheet("background-color: rgb(56, 170, 0);")
            self.rock_button.setEnabled(False)
            self.paper_button.setEnabled(False)
            self.scissor_button.setEnabled(False)
            self.spock_button.setEnabled(False)
            self.lizard_button.setEnabled(False)
            self.return_button.setEnabled(False)
        if ComputerResult == "5":
            self.output_label.setText("Unfortunately You Lose, Computer Won The Game!")
            self.output_label.setStyleSheet("background-color: rgb(249, 1, 18);")
            self.rock_button.setEnabled(False)
            self.paper_button.setEnabled(False)
            self.scissor_button.setEnabled(False)
            self.spock_button.setEnabled(False)
            self.lizard_button.setEnabled(False)
            self.return_button.setEnabled(False)

# --------------------------------------- END ------------------------------------------- #

    def retranslateUi(self, Animation_Game):
        _translate = QtCore.QCoreApplication.translate
        Animation_Game.setWindowTitle(_translate("Animation_Game", "MainWindow"))
        self.welcome_label.setText(_translate("Animation_Game", "Welcome To Rock - Paper - Scissors - Spock - Lizard Game!"))
        self.start_button.setText(_translate("Animation_Game", "Start The Game"))
        self.computer_label.setText(_translate("Animation_Game", "Computer"))
        self.rule_label.setText(_translate("Animation_Game", "Winner will be the Side, Which reaches 5 Point before the Opponent"))
        self.player_label.setText(_translate("Animation_Game", "Player"))
        self.rock_button.setText(_translate("Animation_Game", "Send Rock"))
        self.paper_button.setText(_translate("Animation_Game", "Send Paper"))
        self.scissor_button.setText(_translate("Animation_Game", "Send Scissors"))
        self.spock_button.setText(_translate("Animation_Game", "Send Spock"))
        self.lizard_button.setText(_translate("Animation_Game", "Send Lizard"))
        self.c_label.setText(_translate("Animation_Game", "Computer\'s Score:"))
        self.p_label.setText(_translate("Animation_Game", "Player\'s Score:"))
        self.vs_label.setText(_translate("Animation_Game", "VS"))
        self.restart_button.setText(_translate("Animation_Game", "Restart"))
        self.exit_button.setText(_translate("Animation_Game", "Exit"))
        self.return_button.setText(_translate("Animation_Game", "Come Back"))
        self.p_moved_label.setText(_translate("Animation_Game", ""))
        self.com_moved_label.setText(_translate("Animation_Game", ""))
        self.player_result.setText(_translate("Animation_Game", ""))
        self.comp_result.setText(_translate("Animation_Game", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Animation_Game = QtWidgets.QMainWindow()
    ui = Ui_Animation_Game()
    ui.setupUi(Animation_Game)
    Animation_Game.show()
    sys.exit(app.exec_())
