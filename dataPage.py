from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from resource import NavigationWidget, NavigationWidgetUp
import modelPage

class DataPage(modelPage.Ui_MainWindow):
    def __init__(self):
        super(DataPage, self).__init__()
        self.setupUi()
        self.tipsLabel.setText("这是数据页面")

        # 设置一个带匹配功能的输入框
        self.matchString = ['C', 'C++', 'Java', 'JavaScript']
        # 设置一个横向的Layout
        self.inputLayout = QHBoxLayout()
        self.lineEdit = QLineEdit()
        self.lineEdit.setCompleter(QCompleter(self.matchString))
        self.lineEdit.isClearButtonEnabled()
        self.queryBtn = QPushButton('确认查找')
        self.inputLayout.addWidget(QLabel('请输入表名'))
        self.inputLayout.addWidget(self.lineEdit)
        self.inputLayout.addWidget(self.queryBtn)
        self.inputLayout.addStretch(0.5)
        self.compareTable = QTableWidget()
        self.compareTable.setColumnCount(8)
        self.compareTable.setHorizontalHeaderLabels(['选择', '备份表', '升级表', 'Insert', 'Update', 'Delete', 'Same', 'Message'])
        self.compareTable.setMaximumHeight(100)

        self.comboBox = QComboBox()
        self.comboBox.addItems(['Difference', 'Insert', 'Delete', 'Update', 'Same', 'All'])
        self.comboBox.setFixedWidth(120)

        self.oldTableLayout = QVBoxLayout()
        self.newTableLayout = QVBoxLayout()
        self.oldTable = QTableWidget()
        self.newTable = QTableWidget()
        self.oldTableLayout.addWidget(QLabel('备份表'), alignment=Qt.AlignCenter)
        self.oldTableLayout.addWidget(self.oldTable)
        self.newTableLayout.addWidget(QLabel('新表'), alignment=Qt.AlignCenter)
        self.newTableLayout.addWidget(self.newTable)

        self.upLayout = QVBoxLayout()
        self.upLayout.addLayout(self.inputLayout)
        self.upLayout.addWidget(self.compareTable)
        self.upLayout.addWidget(self.comboBox)
        self.returnLayout().addLayout(self.upLayout, 1, 1, 1, 4)
        self.returnLayout().addLayout(self.oldTableLayout, 2, 0, 3, 3)
        self.returnLayout().addLayout(self.newTableLayout, 2, 3, 3, 3)

    def loadData(self):
        pass