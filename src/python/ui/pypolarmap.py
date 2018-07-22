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
        MainWindow.resize(2234, 1162)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 1091))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.measurementSelectLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.measurementSelectLayout.setContentsMargins(0, 0, 0, 0)
        self.measurementSelectLayout.setObjectName("measurementSelectLayout")
        self.selectDirBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.selectDirBtn.setObjectName("selectDirBtn")
        self.measurementSelectLayout.addWidget(self.selectDirBtn, 0, 0, 1, 1)
        self.measurementView = QtWidgets.QTreeView(self.gridLayoutWidget)
        self.measurementView.setObjectName("measurementView")
        self.measurementSelectLayout.addWidget(self.measurementView, 2, 0, 1, 2)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.fs = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.fs.setEnabled(False)
        self.fs.setMinimum(44100)
        self.fs.setMaximum(384000)
        self.fs.setSingleStep(100)
        self.fs.setProperty("value", 48000)
        self.fs.setDisplayIntegerBase(10)
        self.fs.setObjectName("fs")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fs)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.measurementDistance = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.measurementDistance.setMinimum(0.1)
        self.measurementDistance.setMaximum(10.0)
        self.measurementDistance.setSingleStep(0.01)
        self.measurementDistance.setProperty("value", 1.0)
        self.measurementDistance.setObjectName("measurementDistance")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.measurementDistance)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.boxRadius = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.boxRadius.setMinimum(0.01)
        self.boxRadius.setMaximum(3.0)
        self.boxRadius.setSingleStep(0.01)
        self.boxRadius.setProperty("value", 0.25)
        self.boxRadius.setObjectName("boxRadius")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.boxRadius)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.driverRadius = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.driverRadius.setDecimals(1)
        self.driverRadius.setMinimum(1.0)
        self.driverRadius.setMaximum(40.0)
        self.driverRadius.setSingleStep(0.1)
        self.driverRadius.setProperty("value", 15.0)
        self.driverRadius.setObjectName("driverRadius")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.driverRadius)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.modalCoeffs = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.modalCoeffs.setMinimum(5)
        self.modalCoeffs.setMaximum(14)
        self.modalCoeffs.setProperty("value", 14)
        self.modalCoeffs.setObjectName("modalCoeffs")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.modalCoeffs)
        self.f0 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.f0.setMinimum(1)
        self.f0.setMaximum(200)
        self.f0.setProperty("value", 70)
        self.f0.setObjectName("f0")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.f0)
        self.q0 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.q0.setDecimals(3)
        self.q0.setMinimum(0.2)
        self.q0.setMaximum(1.5)
        self.q0.setSingleStep(0.001)
        self.q0.setProperty("value", 0.7)
        self.q0.setObjectName("q0")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.q0)
        self.transFreq = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.transFreq.setMinimum(1)
        self.transFreq.setMaximum(1000)
        self.transFreq.setProperty("value", 200)
        self.transFreq.setObjectName("transFreq")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.transFreq)
        self.lfGain = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.lfGain.setDecimals(1)
        self.lfGain.setMinimum(-10.0)
        self.lfGain.setMaximum(10.0)
        self.lfGain.setSingleStep(0.1)
        self.lfGain.setObjectName("lfGain")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lfGain)
        self.smoothingType = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.smoothingType.setObjectName("smoothingType")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.smoothingType)
        self.colourMapSelector = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.colourMapSelector.setObjectName("colourMapSelector")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.colourMapSelector)
        self.refreshSpatialBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.refreshSpatialBtn.setObjectName("refreshSpatialBtn")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.refreshSpatialBtn)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.yAxisRange = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.yAxisRange.setMinimum(10)
        self.yAxisRange.setMaximum(120)
        self.yAxisRange.setProperty("value", 60)
        self.yAxisRange.setObjectName("yAxisRange")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.yAxisRange)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.measurementSelectLayout.addLayout(self.formLayout_4, 3, 0, 2, 2)
        self.dataPath = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dataPath.setObjectName("dataPath")
        self.measurementSelectLayout.addWidget(self.dataPath, 1, 0, 1, 1)
        self.graphTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.graphTabs.setGeometry(QtCore.QRect(380, 10, 1831, 1101))
        self.graphTabs.setObjectName("graphTabs")
        self.impulseTab = QtWidgets.QWidget()
        self.impulseTab.setObjectName("impulseTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.impulseTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1902, 1061))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.graphLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.graphLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.graphLayout.setContentsMargins(0, 0, 0, 0)
        self.graphLayout.setObjectName("graphLayout")
        self.impulseGraph = MplWidget(self.gridLayoutWidget_2)
        self.impulseGraph.setMinimumSize(QtCore.QSize(1600, 0))
        self.impulseGraph.setObjectName("impulseGraph")
        self.graphLayout.addWidget(self.impulseGraph, 0, 1, 1, 8)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout_3.setObjectName("formLayout_3")
        self.applyWindowBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.applyWindowBtn.setEnabled(False)
        self.applyWindowBtn.setObjectName("applyWindowBtn")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.applyWindowBtn)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leftWindowType = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.leftWindowType.setObjectName("leftWindowType")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.leftWindowType.addItem("")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.leftWindowType)
        self.leftWindowPercent = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.leftWindowPercent.setMinimum(12)
        self.leftWindowPercent.setMaximum(75)
        self.leftWindowPercent.setProperty("value", 50)
        self.leftWindowPercent.setObjectName("leftWindowPercent")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.leftWindowPercent)
        self.leftWindowSample = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.leftWindowSample.setObjectName("leftWindowSample")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.leftWindowSample)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.rightWindowType = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.rightWindowType.setObjectName("rightWindowType")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.rightWindowType.addItem("")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.rightWindowType)
        self.rightWindowPercent = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.rightWindowPercent.setMinimum(12)
        self.rightWindowPercent.setMaximum(75)
        self.rightWindowPercent.setProperty("value", 50)
        self.rightWindowPercent.setObjectName("rightWindowPercent")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.rightWindowPercent)
        self.rightWindowSample = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.rightWindowSample.setObjectName("rightWindowSample")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.rightWindowSample)
        self.zoomInButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.zoomInButton.setEnabled(False)
        self.zoomInButton.setObjectName("zoomInButton")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.zoomInButton)
        self.zoomOutBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.zoomOutBtn.setEnabled(False)
        self.zoomOutBtn.setObjectName("zoomOutBtn")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.zoomOutBtn)
        self.removeWindowBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.removeWindowBtn.setEnabled(False)
        self.removeWindowBtn.setCheckable(True)
        self.removeWindowBtn.setFlat(False)
        self.removeWindowBtn.setObjectName("removeWindowBtn")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.removeWindowBtn)
        self.graphLayout.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.graphTabs.addTab(self.impulseTab, "")
        self.measuredMagnitudeTab = QtWidgets.QWidget()
        self.measuredMagnitudeTab.setObjectName("measuredMagnitudeTab")
        self.measuredMagnitudeGraph = MplWidget(self.measuredMagnitudeTab)
        self.measuredMagnitudeGraph.setGeometry(QtCore.QRect(0, 0, 1821, 1061))
        self.measuredMagnitudeGraph.setObjectName("measuredMagnitudeGraph")
        self.graphTabs.addTab(self.measuredMagnitudeTab, "")
        self.measuredPolarTab = QtWidgets.QWidget()
        self.measuredPolarTab.setObjectName("measuredPolarTab")
        self.measuredPolarGraph = MplWidget(self.measuredPolarTab)
        self.measuredPolarGraph.setGeometry(QtCore.QRect(0, 0, 1821, 1061))
        self.measuredPolarGraph.setObjectName("measuredPolarGraph")
        self.graphTabs.addTab(self.measuredPolarTab, "")
        self.measuredMultiTab = QtWidgets.QWidget()
        self.measuredMultiTab.setObjectName("measuredMultiTab")
        self.measuredMultiGraph = MplWidget(self.measuredMultiTab)
        self.measuredMultiGraph.setGeometry(QtCore.QRect(0, 0, 1821, 1061))
        self.measuredMultiGraph.setObjectName("measuredMultiGraph")
        self.graphTabs.addTab(self.measuredMultiTab, "")
        self.modalPolarTab = QtWidgets.QWidget()
        self.modalPolarTab.setObjectName("modalPolarTab")
        self.modalPolarGraph = MplWidget(self.modalPolarTab)
        self.modalPolarGraph.setGeometry(QtCore.QRect(0, 0, 1821, 1061))
        self.modalPolarGraph.setObjectName("modalPolarGraph")
        self.graphTabs.addTab(self.modalPolarTab, "")
        self.modalMultiTab = QtWidgets.QWidget()
        self.modalMultiTab.setObjectName("modalMultiTab")
        self.modalMultiGraph = MplWidget(self.modalMultiTab)
        self.modalMultiGraph.setGeometry(QtCore.QRect(0, 0, 1821, 1061))
        self.modalMultiGraph.setObjectName("modalMultiGraph")
        self.graphTabs.addTab(self.modalMultiTab, "")
        self.graphTabs.raise_()
        self.gridLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2234, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        self.rightWindowSample.editingFinished.connect(MainWindow.updateRightWindowPosition)
        self.leftWindowSample.editingFinished.connect(MainWindow.updateLeftWindowPosition)
        self.leftWindowPercent.editingFinished.connect(MainWindow.updateLeftWindowPercentage)
        self.leftWindowType.currentTextChanged['QString'].connect(MainWindow.updateLeftWindowType)
        self.rightWindowType.currentTextChanged['QString'].connect(MainWindow.updateRightWindowType)
        self.rightWindowPercent.editingFinished.connect(MainWindow.updateRightWindowPercentage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pypolarmap"))
        self.selectDirBtn.setText(_translate("MainWindow", "Load Measurements"))
        self.label_13.setText(_translate("MainWindow", "Fs"))
        self.fs.setSuffix(_translate("MainWindow", " Hz"))
        self.label_5.setText(_translate("MainWindow", "Measurement Distance (m)"))
        self.label_12.setText(_translate("MainWindow", "Box Radius (m)"))
        self.label_6.setText(_translate("MainWindow", "Driver Radius (cm)"))
        self.label_7.setText(_translate("MainWindow", "Modal Coefficients"))
        self.smoothingType.setItemText(0, _translate("MainWindow", "None"))
        self.smoothingType.setItemText(1, _translate("MainWindow", "1/3 Octave"))
        self.smoothingType.setItemText(2, _translate("MainWindow", "1/6 Octave"))
        self.smoothingType.setItemText(3, _translate("MainWindow", "1/12 Octave"))
        self.smoothingType.setItemText(4, _translate("MainWindow", "CB Zwicker"))
        self.smoothingType.setItemText(5, _translate("MainWindow", "CB Moore"))
        self.smoothingType.setItemText(6, _translate("MainWindow", "Narrow"))
        self.refreshSpatialBtn.setText(_translate("MainWindow", "Update"))
        self.label_8.setText(_translate("MainWindow", "f0"))
        self.label_9.setText(_translate("MainWindow", "q0"))
        self.label_10.setText(_translate("MainWindow", "Transition Frequency (Hz)"))
        self.label_11.setText(_translate("MainWindow", "LF Gain (dB)"))
        self.label_14.setText(_translate("MainWindow", "Smoothing"))
        self.label_3.setText(_translate("MainWindow", "Colour Map"))
        self.yAxisRange.setSuffix(_translate("MainWindow", " dB"))
        self.label_4.setText(_translate("MainWindow", "Y Range"))
        self.applyWindowBtn.setText(_translate("MainWindow", "Apply Window"))
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
        self.removeWindowBtn.setText(_translate("MainWindow", "Remove Window"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.impulseTab), _translate("MainWindow", "Impulse"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.measuredMagnitudeTab), _translate("MainWindow", "Measured - Magnitude"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.measuredPolarTab), _translate("MainWindow", "Measured - Polar"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.measuredMultiTab), _translate("MainWindow", "Measured - Multi"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.modalPolarTab), _translate("MainWindow", "Modal - Polar"))
        self.graphTabs.setTabText(self.graphTabs.indexOf(self.modalMultiTab), _translate("MainWindow", "Modal - Multi"))

from app import MplWidget
