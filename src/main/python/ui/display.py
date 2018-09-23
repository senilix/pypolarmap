# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_displayControlsDialog(object):
    def setupUi(self, displayControlsDialog):
        displayControlsDialog.setObjectName("displayControlsDialog")
        displayControlsDialog.resize(302, 230)
        self.gridLayout = QtWidgets.QGridLayout(displayControlsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_14 = QtWidgets.QLabel(displayControlsDialog)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.smoothingType = QtWidgets.QComboBox(displayControlsDialog)
        self.smoothingType.setObjectName("smoothingType")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.smoothingType.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.smoothingType)
        self.label_3 = QtWidgets.QLabel(displayControlsDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.colourMapSelector = QtWidgets.QComboBox(displayControlsDialog)
        self.colourMapSelector.setObjectName("colourMapSelector")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.colourMapSelector)
        self.label_4 = QtWidgets.QLabel(displayControlsDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.yAxisRange = QtWidgets.QSpinBox(displayControlsDialog)
        self.yAxisRange.setMinimum(10)
        self.yAxisRange.setMaximum(120)
        self.yAxisRange.setSingleStep(5)
        self.yAxisRange.setProperty("value", 60)
        self.yAxisRange.setObjectName("yAxisRange")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yAxisRange)
        self.normaliseCheckBox = QtWidgets.QCheckBox(displayControlsDialog)
        self.normaliseCheckBox.setObjectName("normaliseCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.normaliseCheckBox)
        self.label_15 = QtWidgets.QLabel(displayControlsDialog)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.normalisationAngle = QtWidgets.QComboBox(displayControlsDialog)
        self.normalisationAngle.setObjectName("normalisationAngle")
        self.normalisationAngle.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.normalisationAngle)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(displayControlsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(displayControlsDialog)
        self.buttonBox.accepted.connect(displayControlsDialog.accept)
        self.buttonBox.rejected.connect(displayControlsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(displayControlsDialog)

    def retranslateUi(self, displayControlsDialog):
        _translate = QtCore.QCoreApplication.translate
        displayControlsDialog.setWindowTitle(_translate("displayControlsDialog", "Display"))
        self.label_14.setText(_translate("displayControlsDialog", "Smoothing"))
        self.smoothingType.setItemText(0, _translate("displayControlsDialog", "None"))
        self.smoothingType.setItemText(1, _translate("displayControlsDialog", "1/3 Octave"))
        self.smoothingType.setItemText(2, _translate("displayControlsDialog", "1/6 Octave"))
        self.smoothingType.setItemText(3, _translate("displayControlsDialog", "1/12 Octave"))
        self.smoothingType.setItemText(4, _translate("displayControlsDialog", "CB Zwicker"))
        self.smoothingType.setItemText(5, _translate("displayControlsDialog", "CB Moore"))
        self.smoothingType.setItemText(6, _translate("displayControlsDialog", "Narrow"))
        self.label_3.setText(_translate("displayControlsDialog", "Colour Scheme"))
        self.label_4.setText(_translate("displayControlsDialog", "Y Range"))
        self.yAxisRange.setSuffix(_translate("displayControlsDialog", "dB"))
        self.normaliseCheckBox.setText(_translate("displayControlsDialog", "Normalise?"))
        self.label_15.setText(_translate("displayControlsDialog", "Normalisation Angle"))
        self.normalisationAngle.setItemText(0, _translate("displayControlsDialog", "0"))

