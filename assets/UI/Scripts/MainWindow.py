# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\assets\UI\Layout\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SQLMANAGER(object):
    def setupUi(self, SQLMANAGER):
        SQLMANAGER.setObjectName("SQLMANAGER")
        SQLMANAGER.setWindowModality(QtCore.Qt.ApplicationModal)
        SQLMANAGER.resize(1054, 786)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SQLMANAGER.sizePolicy().hasHeightForWidth())
        SQLMANAGER.setSizePolicy(sizePolicy)
        SQLMANAGER.setMinimumSize(QtCore.QSize(1054, 786))
        SQLMANAGER.setMaximumSize(QtCore.QSize(1054, 786))
        SQLMANAGER.setWindowOpacity(1.0)
        SQLMANAGER.setAutoFillBackground(False)
        SQLMANAGER.setWindowFilePath("")
        SQLMANAGER.setInputMethodHints(QtCore.Qt.ImhNone)
        SQLMANAGER.setIconSize(QtCore.QSize(24, 24))
        SQLMANAGER.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        SQLMANAGER.setAnimated(True)
        SQLMANAGER.setDocumentMode(False)
        SQLMANAGER.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SQLMANAGER)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(278, 9, 767, 636))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setSizeIncrement(QtCore.QSize(9, 18))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tabs.setFont(font)
        self.tabs.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabs.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs.setIconSize(QtCore.QSize(24, 24))
        self.tabs.setElideMode(QtCore.Qt.ElideNone)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(False)
        self.tabs.setTabBarAutoHide(False)
        self.tabs.setObjectName("tabs")
        self._data = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._data.sizePolicy().hasHeightForWidth())
        self._data.setSizePolicy(sizePolicy)
        self._data.setObjectName("_data")
        self.data_result = QtWidgets.QTableWidget(self._data)
        self.data_result.setGeometry(QtCore.QRect(0, 0, 761, 611))
        self.data_result.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.data_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.data_result.setFrameShadow(QtWidgets.QFrame.Plain)
        self.data_result.setLineWidth(1)
        self.data_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.data_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.data_result.setTabKeyNavigation(False)
        self.data_result.setProperty("showDropIndicator", False)
        self.data_result.setDragDropOverwriteMode(False)
        self.data_result.setAlternatingRowColors(True)
        self.data_result.setShowGrid(True)
        self.data_result.setGridStyle(QtCore.Qt.SolidLine)
        self.data_result.setWordWrap(True)
        self.data_result.setCornerButtonEnabled(True)
        self.data_result.setRowCount(0)
        self.data_result.setColumnCount(0)
        self.data_result.setObjectName("data_result")
        self.tabs.addTab(self._data, "")
        self._desc = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._desc.sizePolicy().hasHeightForWidth())
        self._desc.setSizePolicy(sizePolicy)
        self._desc.setObjectName("_desc")
        self.desc_result = QtWidgets.QTableWidget(self._desc)
        self.desc_result.setGeometry(QtCore.QRect(0, 310, 760, 300))
        self.desc_result.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.desc_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.desc_result.setFrameShadow(QtWidgets.QFrame.Plain)
        self.desc_result.setLineWidth(1)
        self.desc_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.desc_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.desc_result.setTabKeyNavigation(False)
        self.desc_result.setProperty("showDropIndicator", False)
        self.desc_result.setDragDropOverwriteMode(False)
        self.desc_result.setAlternatingRowColors(True)
        self.desc_result.setShowGrid(True)
        self.desc_result.setGridStyle(QtCore.Qt.SolidLine)
        self.desc_result.setWordWrap(True)
        self.desc_result.setCornerButtonEnabled(True)
        self.desc_result.setRowCount(0)
        self.desc_result.setColumnCount(0)
        self.desc_result.setObjectName("desc_result")
        self.create_in = QtWidgets.QPlainTextEdit(self._desc)
        self.create_in.setGeometry(QtCore.QRect(0, 0, 760, 303))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(11)
        self.create_in.setFont(font)
        self.create_in.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.create_in.setFrameShadow(QtWidgets.QFrame.Plain)
        self.create_in.setLineWidth(1)
        self.create_in.setMidLineWidth(0)
        self.create_in.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.create_in.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.create_in.setUndoRedoEnabled(False)
        self.create_in.setReadOnly(True)
        self.create_in.setPlainText("")
        self.create_in.setBackgroundVisible(False)
        self.create_in.setCenterOnScroll(False)
        self.create_in.setPlaceholderText("")
        self.create_in.setObjectName("create_in")
        self.separator = QtWidgets.QFrame(self._desc)
        self.separator.setGeometry(QtCore.QRect(-10, 300, 780, 10))
        self.separator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.separator.setLineWidth(4)
        self.separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator.setObjectName("separator")
        self.tabs.addTab(self._desc, "")
        self._query = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._query.sizePolicy().hasHeightForWidth())
        self._query.setSizePolicy(sizePolicy)
        self._query.setObjectName("_query")
        self.result_out = QtWidgets.QTableWidget(self._query)
        self.result_out.setGeometry(QtCore.QRect(0, 310, 760, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_out.sizePolicy().hasHeightForWidth())
        self.result_out.setSizePolicy(sizePolicy)
        self.result_out.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.result_out.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.result_out.setFrameShadow(QtWidgets.QFrame.Plain)
        self.result_out.setLineWidth(1)
        self.result_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.result_out.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.result_out.setTabKeyNavigation(False)
        self.result_out.setProperty("showDropIndicator", False)
        self.result_out.setDragDropOverwriteMode(False)
        self.result_out.setAlternatingRowColors(True)
        self.result_out.setShowGrid(True)
        self.result_out.setGridStyle(QtCore.Qt.SolidLine)
        self.result_out.setWordWrap(True)
        self.result_out.setCornerButtonEnabled(False)
        self.result_out.setRowCount(0)
        self.result_out.setColumnCount(0)
        self.result_out.setObjectName("result_out")
        self.query_in = QtWidgets.QPlainTextEdit(self._query)
        self.query_in.setGeometry(QtCore.QRect(0, 0, 760, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query_in.sizePolicy().hasHeightForWidth())
        self.query_in.setSizePolicy(sizePolicy)
        self.query_in.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.query_in.setFont(font)
        self.query_in.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.query_in.setMouseTracking(False)
        self.query_in.setAutoFillBackground(False)
        self.query_in.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhExclusiveInputMask|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoEditMenu|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhNoTextHandles|QtCore.Qt.ImhPreferLatin|QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhSensitiveData|QtCore.Qt.ImhTime|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.query_in.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.query_in.setFrameShadow(QtWidgets.QFrame.Plain)
        self.query_in.setLineWidth(1)
        self.query_in.setMidLineWidth(0)
        self.query_in.setPlainText("")
        self.query_in.setBackgroundVisible(False)
        self.query_in.setCenterOnScroll(False)
        self.query_in.setObjectName("query_in")
        self.separrator = QtWidgets.QFrame(self._query)
        self.separrator.setGeometry(QtCore.QRect(-10, 295, 780, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.separrator.sizePolicy().hasHeightForWidth())
        self.separrator.setSizePolicy(sizePolicy)
        self.separrator.setStyleSheet("")
        self.separrator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.separrator.setLineWidth(4)
        self.separrator.setMidLineWidth(0)
        self.separrator.setFrameShape(QtWidgets.QFrame.HLine)
        self.separrator.setObjectName("separrator")
        self.tabs.addTab(self._query, "")
        self.tables_out = QtWidgets.QTreeWidget(self.centralwidget)
        self.tables_out.setGeometry(QtCore.QRect(9, 9, 260, 630))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.tables_out.setFont(font)
        self.tables_out.setAutoFillBackground(False)
        self.tables_out.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tables_out.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tables_out.setLineWidth(0)
        self.tables_out.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tables_out.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tables_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tables_out.setColumnCount(1)
        self.tables_out.setObjectName("tables_out")
        self.tables_out.header().setVisible(False)
        self.tables_out.header().setCascadingSectionResizes(True)
        self.tables_out.header().setHighlightSections(True)
        self.console_out = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.console_out.setGeometry(QtCore.QRect(10, 650, 1000, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.console_out.setFont(font)
        self.console_out.setFrameShape(QtWidgets.QFrame.Box)
        self.console_out.setFrameShadow(QtWidgets.QFrame.Plain)
        self.console_out.setLineWidth(1)
        self.console_out.setMidLineWidth(0)
        self.console_out.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.console_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.console_out.setUndoRedoEnabled(False)
        self.console_out.setReadOnly(True)
        self.console_out.setPlainText("")
        self.console_out.setBackgroundVisible(False)
        self.console_out.setCenterOnScroll(False)
        self.console_out.setObjectName("console_out")
        self.openConsole = QtWidgets.QPushButton(self.centralwidget)
        self.openConsole.setGeometry(QtCore.QRect(1010, 650, 30, 80))
        font = QtGui.QFont()
        font.setKerning(True)
        self.openConsole.setFont(font)
        self.openConsole.setStyleSheet("border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.openConsole.setObjectName("openConsole")
        self.tabs.raise_()
        self.tables_out.raise_()
        self.openConsole.raise_()
        self.console_out.raise_()
        SQLMANAGER.setCentralWidget(self.centralwidget)
        self.actionImport_Query = QtWidgets.QAction(SQLMANAGER)
        self.actionImport_Query.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        self.actionImport_Query.setObjectName("actionImport_Query")
        self.actionExport_Query = QtWidgets.QAction(SQLMANAGER)
        self.actionExport_Query.setObjectName("actionExport_Query")
        self.actionCompile = QtWidgets.QAction(SQLMANAGER)
        self.actionCompile.setObjectName("actionCompile")
        self.actionExecute_Selected = QtWidgets.QAction(SQLMANAGER)
        self.actionExecute_Selected.setObjectName("actionExecute_Selected")
        self.actionAbout = QtWidgets.QAction(SQLMANAGER)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDocuments = QtWidgets.QAction(SQLMANAGER)
        self.actionDocuments.setObjectName("actionDocuments")
        self.actionCopy = QtWidgets.QAction(SQLMANAGER)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(SQLMANAGER)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCrop = QtWidgets.QAction(SQLMANAGER)
        self.actionCrop.setObjectName("actionCrop")
        self.actionSelect_All = QtWidgets.QAction(SQLMANAGER)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionInvert_Selection = QtWidgets.QAction(SQLMANAGER)
        self.actionInvert_Selection.setObjectName("actionInvert_Selection")
        self.actionExit = QtWidgets.QAction(SQLMANAGER)
        self.actionExit.setObjectName("actionExit")
        self.actionRefresh_Database = QtWidgets.QAction(SQLMANAGER)
        self.actionRefresh_Database.setObjectName("actionRefresh_Database")

        self.retranslateUi(SQLMANAGER)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SQLMANAGER)
        SQLMANAGER.setTabOrder(self.tabs, self.query_in)
        SQLMANAGER.setTabOrder(self.query_in, self.result_out)
        SQLMANAGER.setTabOrder(self.result_out, self.console_out)
        SQLMANAGER.setTabOrder(self.console_out, self.desc_result)
        SQLMANAGER.setTabOrder(self.desc_result, self.data_result)
        SQLMANAGER.setTabOrder(self.data_result, self.tables_out)

    def retranslateUi(self, SQLMANAGER):
        _translate = QtCore.QCoreApplication.translate
        SQLMANAGER.setWindowTitle(_translate("SQLMANAGER", "SQL Manager [0.1a]"))
        self.data_result.setSortingEnabled(False)
        self.tabs.setTabText(self.tabs.indexOf(self._data), _translate("SQLMANAGER", "Data"))
        self.desc_result.setSortingEnabled(False)
        self.tabs.setTabText(self.tabs.indexOf(self._desc), _translate("SQLMANAGER", "Fields"))
        self.result_out.setSortingEnabled(False)
        self.tabs.setTabText(self.tabs.indexOf(self._query), _translate("SQLMANAGER", "Query"))
        self.tables_out.headerItem().setText(0, _translate("SQLMANAGER", "CONNECTION"))
        self.openConsole.setText(_translate("SQLMANAGER", "O\n"
"P\n"
"E\n"
"N"))
        self.actionImport_Query.setText(_translate("SQLMANAGER", "Load SQL File"))
        self.actionImport_Query.setShortcut(_translate("SQLMANAGER", "Ctrl+W"))
        self.actionExport_Query.setText(_translate("SQLMANAGER", "Execute SQL File"))
        self.actionExport_Query.setShortcut(_translate("SQLMANAGER", "Ctrl+E"))
        self.actionCompile.setText(_translate("SQLMANAGER", "Execute Query"))
        self.actionCompile.setShortcut(_translate("SQLMANAGER", "Ctrl+Return"))
        self.actionExecute_Selected.setText(_translate("SQLMANAGER", "Execute Selected"))
        self.actionExecute_Selected.setShortcut(_translate("SQLMANAGER", "Ctrl+Shift+Return"))
        self.actionAbout.setText(_translate("SQLMANAGER", "About"))
        self.actionDocuments.setText(_translate("SQLMANAGER", "Documents"))
        self.actionCopy.setText(_translate("SQLMANAGER", "Copy"))
        self.actionCopy.setShortcut(_translate("SQLMANAGER", "Ctrl+C"))
        self.actionPaste.setText(_translate("SQLMANAGER", "Paste"))
        self.actionPaste.setShortcut(_translate("SQLMANAGER", "Ctrl+V"))
        self.actionCrop.setText(_translate("SQLMANAGER", "Crop"))
        self.actionCrop.setShortcut(_translate("SQLMANAGER", "Ctrl+X"))
        self.actionSelect_All.setText(_translate("SQLMANAGER", "Select All"))
        self.actionSelect_All.setShortcut(_translate("SQLMANAGER", "Ctrl+A"))
        self.actionInvert_Selection.setText(_translate("SQLMANAGER", "Invert Selection"))
        self.actionInvert_Selection.setShortcut(_translate("SQLMANAGER", "Ctrl+Shift+A"))
        self.actionExit.setText(_translate("SQLMANAGER", "Exit"))
        self.actionRefresh_Database.setText(_translate("SQLMANAGER", "Refresh Database"))
        self.actionRefresh_Database.setShortcut(_translate("SQLMANAGER", "Ctrl+R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SQLMANAGER = QtWidgets.QMainWindow()
    ui = Ui_SQLMANAGER()
    ui.setupUi(SQLMANAGER)
    SQLMANAGER.show()
    sys.exit(app.exec_())
