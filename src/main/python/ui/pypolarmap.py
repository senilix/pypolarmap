# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pypolarmap.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1638, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.menuGridLayout = QtWidgets.QGridLayout()
        self.menuGridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.menuGridLayout.setObjectName("menuGridLayout")
        self.optionsFormLayout = QtWidgets.QFormLayout()
        self.optionsFormLayout.setObjectName("optionsFormLayout")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.optionsFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.fs = QtWidgets.QSpinBox(self.centralwidget)
        self.fs.setEnabled(False)
        self.fs.setMinimum(44100)
        self.fs.setMaximum(384000)
        self.fs.setSingleStep(100)
        self.fs.setProperty("value", 48000)
        self.fs.setDisplayIntegerBase(10)
        self.fs.setObjectName("fs")
        self.optionsFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fs)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.optionsFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.optionsFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.optionsFormLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label_18)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.optionsFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.smoothingType = QtWidgets.QComboBox(self.centralwidget)
        self.smoothingType.setObjectName("smoothingType")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.optionsFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.smoothingType)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.optionsFormLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.colourMapSelector = QtWidgets.QComboBox(self.centralwidget)
        self.colourMapSelector.setObjectName("colourMapSelector")
        self.optionsFormLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.colourMapSelector)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.optionsFormLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.yAxisRange = QtWidgets.QSpinBox(self.centralwidget)
        self.yAxisRange.setMinimum(10)
        self.yAxisRange.setMaximum(120)
        self.yAxisRange.setSingleStep(5)
        self.yAxisRange.setProperty("value", 60)
        self.yAxisRange.setObjectName("yAxisRange")
        self.optionsFormLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.yAxisRange)
        self.normaliseCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.normaliseCheckBox.setObjectName("normaliseCheckBox")
        self.optionsFormLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.normaliseCheckBox)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.optionsFormLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.normalisationAngle = QtWidgets.QComboBox(self.centralwidget)
        self.normalisationAngle.setObjectName("normalisationAngle")
        self.normalisationAngle.addItem("")
        self.optionsFormLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.normalisationAngle)
        self.menuGridLayout.addLayout(self.optionsFormLayout, 3, 0, 2, 2)
        self.selectDirBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectDirBtn.setObjectName("selectDirBtn")
        self.menuGridLayout.addWidget(self.selectDirBtn, 0, 0, 1, 1)
        self.dataPath = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataPath.sizePolicy().hasHeightForWidth())
        self.dataPath.setSizePolicy(sizePolicy)
        self.dataPath.setMaximumSize(QtCore.QSize(320, 16777215))
        self.dataPath.setObjectName("dataPath")
        self.menuGridLayout.addWidget(self.dataPath, 1, 0, 1, 2)
        self.saveImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveImageBtn.setObjectName("saveImageBtn")
        self.menuGridLayout.addWidget(self.saveImageBtn, 0, 1, 1, 1)
        self.measurementView = QtWidgets.QTreeView(self.centralwidget)
        self.measurementView.setObjectName("measurementView")
        self.menuGridLayout.addWidget(self.measurementView, 2, 0, 1, 2)
        self.gridLayout.addLayout(self.menuGridLayout, 0, 0, 1, 1)
        self.graphTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.graphTabs.setMinimumSize(QtCore.QSize(0, 0))
        self.graphTabs.setObjectName("graphTabs")
        self.impulseTab = QtWidgets.QWidget()
        self.impulseTab.setObjectName("impulseTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.impulseTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphLayout = QtWidgets.QGridLayout()
        self.graphLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.graphLayout.setObjectName("graphLayout")
        self.impulseGraph = MplWidget(self.impulseTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.impulseGraph.sizePolicy().hasHeightForWidth())
        self.impulseGraph.setSizePolicy(sizePolicy)
        self.impulseGraph.setMinimumSize(QtCore.QSize(600, 400))
        self.impulseGraph.setObjectName("impulseGraph")
        self.graphLayout.addWidget(self.impulseGraph, 0, 1, 1, 8)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_3.setObjectName("formLayout_3")
        self.applyWindowBtn = QtWidgets.QPushButton(self.impulseTab)
        self.applyWindowBtn.setEnabled(False)
        self.applyWindowBtn.setObjectName("applyWindowBtn")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.applyWindowBtn)
        self.removeWindowBtn = QtWidgets.QPushButton(self.impulseTab)
        self.removeWindowBtn.setEnabled(False)
        self.removeWindowBtn.setCheckable(True)
        self.removeWindowBtn.setFlat(False)
        self.removeWindowBtn.setObjectName("removeWindowBtn")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.removeWindowBtn)
        self.label = QtWidgets.QLabel(self.impulseTab)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leftWindowType = QtWidgets.QComboBox(self.impulseTab)
        self.leftWindowType.setObjectName("leftWindowType")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leftWindowType)
        self.leftWindowPercent = QtWidgets.QSpinBox(self.impulseTab)
        self.leftWindowPercent.setMinimum(12)
        self.leftWindowPercent.setMaximum(75)
        self.leftWindowPercent.setProperty("value", 50)
        self.leftWindowPercent.setObjectName("leftWindowPercent")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.leftWindowPercent)
        self.leftWindowSample = QtWidgets.QSpinBox(self.impulseTab)
        self.leftWindowSample.setObjectName("leftWindowSample")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.leftWindowSample)
        self.label_2 = QtWidgets.QLabel(self.impulseTab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.rightWindowType = QtWidgets.QComboBox(self.impulseTab)
        self.rightWindowType.setObjectName("rightWindowType")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.rightWindowType)
        self.rightWindowPercent = QtWidgets.QSpinBox(self.impulseTab)
        self.rightWindowPercent.setMinimum(12)
        self.rightWindowPercent.setMaximum(75)
        self.rightWindowPercent.setProperty("value", 50)
        self.rightWindowPercent.setObjectName("rightWindowPercent")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.rightWindowPercent)
        self.rightWindowSample = QtWidgets.QSpinBox(self.impulseTab)
        self.rightWindowSample.setObjectName("rightWindowSample")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.rightWindowSample)
        self.zoomInButton = QtWidgets.QPushButton(self.impulseTab)
        self.zoomInButton.setEnabled(False)
        self.zoomInButton.setObjectName("zoomInButton")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.zoomInButton)
        self.zoomOutBtn = QtWidgets.QPushButton(self.impulseTab)
        self.zoomOutBtn.setEnabled(False)
        self.zoomOutBtn.setObjectName("zoomOutBtn")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.zoomOutBtn)
        self.label_5 = QtWidgets.QLabel(self.impulseTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.measurementDistance = QtWidgets.QDoubleSpinBox(self.impulseTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurementDistance.sizePolicy().hasHeightForWidth())
        self.measurementDistance.setSizePolicy(sizePolicy)
        self.measurementDistance.setMinimum(0.1)
        self.measurementDistance.setMaximum(10.0)
        self.measurementDistance.setSingleStep(0.01)
        self.measurementDistance.setProperty("value", 1.0)
        self.measurementDistance.setObjectName("measurementDistance")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.measurementDistance)
        self.label_12 = QtWidgets.QLabel(self.impulseTab)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.boxRadius = QtWidgets.QDoubleSpinBox(self.impulseTab)
        self.boxRadius.setMinimum(0.01)
        self.boxRadius.setMaximum(3.0)
        self.boxRadius.setSingleStep(0.01)
        self.boxRadius.setProperty("value", 0.25)
        self.boxRadius.setObjectName("boxRadius")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.boxRadius)
        self.label_6 = QtWidgets.QLabel(self.impulseTab)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.driverRadius = QtWidgets.QDoubleSpinBox(self.impulseTab)
        self.driverRadius.setDecimals(1)
        self.driverRadius.setMinimum(1.0)
        self.driverRadius.setMaximum(40.0)
        self.driverRadius.setSingleStep(0.1)
        self.driverRadius.setProperty("value", 15.0)
        self.driverRadius.setObjectName("driverRadius")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.driverRadius)
        self.label_7 = QtWidgets.QLabel(self.impulseTab)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.modalCoeffs = QtWidgets.QSpinBox(self.impulseTab)
        self.modalCoeffs.setMinimum(5)
        self.modalCoeffs.setMaximum(14)
        self.modalCoeffs.setProperty("value", 14)
        self.modalCoeffs.setObjectName("modalCoeffs")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.modalCoeffs)
        self.label_8 = QtWidgets.QLabel(self.impulseTab)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.f0 = QtWidgets.QSpinBox(self.impulseTab)
        self.f0.setMinimum(1)
        self.f0.setMaximum(200)
        self.f0.setProperty("value", 70)
        self.f0.setObjectName("f0")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.f0)
        self.label_9 = QtWidgets.QLabel(self.impulseTab)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.q0 = QtWidgets.QDoubleSpinBox(self.impulseTab)
        self.q0.setDecimals(3)
        self.q0.setMinimum(0.2)
        self.q0.setMaximum(1.5)
        self.q0.setSingleStep(0.001)
        self.q0.setProperty("value", 0.7)
        self.q0.setObjectName("q0")
        self.formLayout_3.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.q0)
        self.label_10 = QtWidgets.QLabel(self.impulseTab)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.transFreq = QtWidgets.QSpinBox(self.impulseTab)
        self.transFreq.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.transFreq.setMinimum(1)
        self.transFreq.setMaximum(1000)
        self.transFreq.setProperty("value", 200)
        self.transFreq.setObjectName("transFreq")
        self.formLayout_3.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.transFreq)
        self.label_11 = QtWidgets.QLabel(self.impulseTab)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lfGain = QtWidgets.QDoubleSpinBox(self.impulseTab)
        self.lfGain.setDecimals(1)
        self.lfGain.setMinimum(-10.0)
        self.lfGain.setMaximum(10.0)
        self.lfGain.setSingleStep(0.1)
        self.lfGain.setObjectName("lfGain")
        self.formLayout_3.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.lfGain)
        self.refreshSpatialBtn = QtWidgets.QPushButton(self.impulseTab)
        self.refreshSpatialBtn.setObjectName("refreshSpatialBtn")
        self.formLayout_3.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.refreshSpatialBtn)
        self.graphLayout.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.graphLayout, 0, 0, 1, 1)
        self.graphTabs.addTab(self.impulseTab, "")
        self.measuredMagnitudeTab = QtWidgets.QWidget()
        self.measuredMagnitudeTab.setObjectName("measuredMagnitudeTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.measuredMagnitudeTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.measuredMagnitudeGraph = MplWidget(self.measuredMagnitudeTab)
        self.measuredMagnitudeGraph.setMinimumSize(QtCore.QSize(847, 400))
        self.measuredMagnitudeGraph.setObjectName("measuredMagnitudeGraph")
        self.gridLayout_3.addWidget(self.measuredMagnitudeGraph, 0, 0, 1, 1)
        self.graphTabs.addTab(self.measuredMagnitudeTab, "")
        self.measuredPolarTab = QtWidgets.QWidget()
        self.measuredPolarTab.setObjectName("measuredPolarTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.measuredPolarTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.measuredPolarGraph = MplWidget(self.measuredPolarTab)
        self.measuredPolarGraph.setMinimumSize(QtCore.QSize(847, 400))
        self.measuredPolarGraph.setObjectName("measuredPolarGraph")
        self.gridLayout_4.addWidget(self.measuredPolarGraph, 0, 0, 1, 1)
        self.graphTabs.addTab(self.measuredPolarTab, "")
        self.measuredMultiTab = QtWidgets.QWidget()
        self.measuredMultiTab.setObjectName("measuredMultiTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.measuredMultiTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.measuredMultiGraph = MplWidget(self.measuredMultiTab)
        self.measuredMultiGraph.setMinimumSize(QtCore.QSize(847, 400))
        self.measuredMultiGraph.setObjectName("measuredMultiGraph")
        self.gridLayout_5.addWidget(self.measuredMultiGraph, 0, 0, 1, 1)
        self.graphTabs.addTab(self.measuredMultiTab, "")
        self.modalPolarTab = QtWidgets.QWidget()
        self.modalPolarTab.setObjectName("modalPolarTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.modalPolarTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.modalPolarGraph = MplWidget(self.modalPolarTab)
        self.modalPolarGraph.setMinimumSize(QtCore.QSize(847, 400))
        self.modalPolarGraph.setObjectName("modalPolarGraph")
        self.gridLayout_6.addWidget(self.modalPolarGraph, 0, 0, 1, 1)
        self.graphTabs.addTab(self.modalPolarTab, "")
        self.modalMultiTab = QtWidgets.QWidget()
        self.modalMultiTab.setObjectName("modalMultiTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.modalMultiTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.modalMultiGraph = MplWidget(self.modalMultiTab)
        self.modalMultiGraph.setMinimumSize(QtCore.QSize(847, 400))
        self.modalMultiGraph.setObjectName("modalMultiGraph")
        self.gridLayout_7.addWidget(self.modalMultiGraph, 0, 0, 1, 1)
        self.graphTabs.addTab(self.modalMultiTab, "")
        self.gridLayout.addWidget(self.graphTabs, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1638, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave_Current_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Image.setObjectName("actionSave_Current_Image")
        self.actionShow_Logs = QtWidgets.QAction(MainWindow)
        self.actionShow_Logs.setObjectName("actionShow_Logs")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave_Current_Image)
        self.menuHelp.addAction(self.actionShow_Logs)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.graphTabs.setCurrentIndex(0)
        self.selectDirBtn.clicked.connect(MainWindow.selectDirectory)
        self.zoomInButton.clicked.connect(MainWindow.zoomIn)
        self.removeWindowBtn.clicked.connect(MainWindow.removeWindow)
        self.graphTabs.currentChanged['int'].connect(MainWindow.onGraphTabChange)
        self.zoomOutBtn.clicked.connect(MainWindow.zoomOut)
        self.colourMapSelector.currentIndexChanged['QString'].connect(MainWindow.updateColourMap)
        self.measurementDistance.valueChanged['double'].connect(MainWindow.updateMeasurementDistance)
        self.driverRadius.valueChanged['double'].connect(MainWindow.updateDriverRadius)
        self.modalCoeffs.valueChanged['int'].connect(MainWindow.updateModalCoeffs)
        self.f0.valueChanged['int'].connect(MainWindow.updateF0)
        self.q0.valueChanged['double'].connect(MainWindow.updateQ0)
        self.transFreq.valueChanged['int'].connect(MainWindow.updateTransitionFrequency)
        self.lfGain.valueChanged['double'].connect(MainWindow.updateLFGain)
        self.boxRadius.valueChanged['double'].connect(MainWindow.updateBoxRadius)
        self.refreshSpatialBtn.clicked.connect(MainWindow.refreshModal)
        self.smoothingType.currentIndexChanged['QString'].connect(MainWindow.updateSmoothing)
        self.applyWindowBtn.clicked.connect(MainWindow.updateWindow)
        self.zoomOutBtn.clicked.connect(MainWindow.zoomOut)
        self.rightWindowSample.editingFinished.connect(MainWindow.updateRightWindow)
        self.leftWindowSample.editingFinished.connect(MainWindow.updateLeftWindow)
        self.leftWindowPercent.valueChanged['int'].connect(MainWindow.updateLeftWindow)
        self.leftWindowType.currentTextChanged['QString'].connect(MainWindow.updateLeftWindow)
        self.rightWindowType.currentTextChanged['QString'].connect(MainWindow.updateRightWindow)
        self.rightWindowPercent.valueChanged['int'].connect(MainWindow.updateRightWindow)
        self.yAxisRange.valueChanged['int'].connect(MainWindow.setYRange)
        self.normaliseCheckBox.clicked.connect(MainWindow.toggleNormalised)
        self.normalisationAngle.currentIndexChanged['QString'].connect(MainWindow.setNormalisationAngle)
        self.saveImageBtn.clicked.connect(MainWindow.saveCurrentChart)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pypolarmap"))
        self.label_13.setText(_translate("MainWindow", "Fs"))
        self.fs.setSuffix(_translate("MainWindow", " Hz"))
        self.label_16.setText(_translate("MainWindow", "Active Axis"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Horizontal"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Vertical"))
        self.label_18.setText(_translate("MainWindow", "Display Controls"))
        self.label_14.setText(_translate("MainWindow", "Smoothing"))
        self.smoothingType.setItemText(0, _translate("MainWindow", "None"))
        self.smoothingType.setItemText(1, _translate("MainWindow", "1/3 Octave"))
        self.smoothingType.setItemText(2, _translate("MainWindow", "1/6 Octave"))
        self.smoothingType.setItemText(3, _translate("MainWindow", "1/12 Octave"))
        self.smoothingType.setItemText(4, _translate("MainWindow", "CB Zwicker"))
        self.smoothingType.setItemText(5, _translate("MainWindow", "CB Moore"))
        self.smoothingType.setItemText(6, _translate("MainWindow", "Narrow"))
        self.label_3.setText(_translate("MainWindow", "Colour Scheme"))
        self.label_4.setText(_translate("MainWindow", "Y Range"))
        self.yAxisRange.setSuffix(_translate("MainWindow", " dB"))
        self.normaliseCheckBox.setText(_translate("MainWindow", "Normalise?"))
        self.label_15.setText(_translate("MainWindow", "Normalisation Angle"))
        self.normalisationAngle.setItemText(0, _translate("MainWindow", "0"))
        self.selectDirBtn.setText(_translate("MainWindow", "Load Measurements"))
        self.saveImageBtn.setText(_translate("MainWindow", "Save Image"))
        self.applyWindowBtn.setText(_translate("MainWindow", "Apply Window"))
        self.removeWindowBtn.setText(_translate("MainWindow", "Remove Window"))
        self.label.setText(_translate("MainWindow", "Left"))
        self.leftWindowType.setItemText(0, _translate("MainWindow", "Rectangle"))
        self.leftWindowType.setItemText(1, _translate("MainWindow", "Tukey"))
        self.leftWindowType.setItemText(2, _translate("MainWindow", "Hann"))
        self.leftWindowType.setItemText(3, _translate("MainWindow", "Hamming"))
        self.leftWindowType.setItemText(4, _translate("MainWindow", "Blackman-Harris"))
        self.leftWindowType.setItemText(5, _translate("MainWindow", "Nuttall"))
        self.leftWindowPercent.setSuffix(_translate("MainWindow", "%"))
        self.label_2.setText(_translate("MainWindow", "Right"))
        self.rightWindowType.setItemText(0, _translate("MainWindow", "Rectangle"))
        self.rightWindowType.setItemText(1, _translate("MainWindow", "Tukey"))
        self.rightWindowType.setItemText(2, _translate("MainWindow", "Hann"))
        self.rightWindowType.setItemText(3, _translate("MainWindow", "Hamming"))
        self.rightWindowType.setItemText(4, _translate("MainWindow", "Blackman-Harris"))
        self.rightWindowType.setItemText(5, _translate("MainWindow", "Nuttall"))
        self.rightWindowPercent.setSuffix(_translate("MainWindow", "%"))
        self.zoomInButton.setText(_translate("MainWindow", "Zoom To Gate"))
        self.zoomOutBtn.setText(_translate("MainWindow", "Zoom Out"))
        self.label_5.setText(_translate("MainWindow", "Measurement Distance (m)"))
        self.label_12.setText(_translate("MainWindow", "Box Radius (m)"))
        self.label_6.setText(_translate("MainWindow", "Driver Radius (cm)"))
        self.label_7.setText(_translate("MainWindow", "Modal Coefficients"))
        self.label_8.setText(_translate("MainWindow", "f0"))
        self.label_9.setText(_translate("MainWindow", "q0"))
        self.label_10.setText(_translate("MainWindow", "Transition Frequency (Hz)"))
        self.label_11.setText(_translate("MainWindow", "LF Gain (dB)"))
        self.refreshSpatialBtn.setText(_translate("MainWindow", "Update"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.impulseTab), _translate("MainWindow", "Impulse"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.measuredMagnitudeTab), _translate("MainWindow", "Measured - Magnitude"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.measuredPolarTab), _translate("MainWindow", "Measured - Polar"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.measuredMultiTab), _translate("MainWindow", "Measured - Multi"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.modalPolarTab), _translate("MainWindow", "Modal - Polar"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.modalMultiTab), _translate("MainWindow", "Modal - Multi"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Current_Image.setText(_translate("MainWindow", "Save Chart"))
        self.actionSave_Current_Image.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionShow_Logs.setText(_translate("MainWindow", "Show Logs"))
        self.actionShow_Logs.setShortcut(_translate("MainWindow", "Ctrl+L"))

from app import MplWidget
