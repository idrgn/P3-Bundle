# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 650)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayoutMain = QtWidgets.QHBoxLayout()
        self.gridLayoutMain.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayoutMain.setSpacing(6)
        self.gridLayoutMain.setObjectName("gridLayoutMain")
        self.treeWidget = QTreeWidgetBundle(self.centralwidget)
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeWidget.setToolTip("")
        self.treeWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "None")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.header().setVisible(True)
        self.gridLayoutMain.addWidget(self.treeWidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutMenu = QtWidgets.QGridLayout()
        self.gridLayoutMenu.setObjectName("gridLayoutMenu")
        self.l2 = QtWidgets.QFrame(self.frame)
        self.l2.setToolTip("")
        self.l2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.l2.setFrameShape(QtWidgets.QFrame.HLine)
        self.l2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l2.setObjectName("l2")
        self.gridLayoutMenu.addWidget(self.l2, 6, 0, 1, 1)
        self.pb_open = QtWidgets.QPushButton(self.frame)
        self.pb_open.setEnabled(False)
        self.pb_open.setToolTip("<html><head/><body><p>Open a bnd or gzipped file inside the current file</p></body></html>")
        self.pb_open.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_open.setCheckable(False)
        self.pb_open.setObjectName("pb_open")
        self.gridLayoutMenu.addWidget(self.pb_open, 7, 0, 1, 1)
        self.l3 = QtWidgets.QFrame(self.frame)
        self.l3.setToolTip("")
        self.l3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.l3.setFrameShape(QtWidgets.QFrame.HLine)
        self.l3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l3.setObjectName("l3")
        self.gridLayoutMenu.addWidget(self.l3, 9, 0, 1, 1)
        self.te_preview = QtWidgets.QTextEdit(self.frame)
        self.te_preview.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.te_preview.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.te_preview.setFont(font)
        self.te_preview.setAcceptDrops(False)
        self.te_preview.setToolTip("<html><head/><body><p>Files that start with <span style=\" font-weight:600;\">42 4E 44</span> are bnd files. Files that start with <span style=\" font-weight:600;\">1F 0B 08</span> are gzipped files.</p></body></html>")
        self.te_preview.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.te_preview.setUndoRedoEnabled(False)
        self.te_preview.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.te_preview.setReadOnly(True)
        self.te_preview.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.te_preview.setPlaceholderText("")
        self.te_preview.setObjectName("te_preview")
        self.gridLayoutMenu.addWidget(self.te_preview, 13, 0, 1, 1)
        self.pb_back = QtWidgets.QPushButton(self.frame)
        self.pb_back.setEnabled(False)
        self.pb_back.setToolTip("<html><head/><body><p>Return back to the previous file. Changes are only applied if the current file is saved.</p></body></html>")
        self.pb_back.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_back.setObjectName("pb_back")
        self.gridLayoutMenu.addWidget(self.pb_back, 8, 0, 1, 1)
        self.pb_delete_file = QtWidgets.QPushButton(self.frame)
        self.pb_delete_file.setEnabled(False)
        self.pb_delete_file.setToolTip("")
        self.pb_delete_file.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_delete_file.setObjectName("pb_delete_file")
        self.gridLayoutMenu.addWidget(self.pb_delete_file, 1, 0, 1, 1)
        self.l1 = QtWidgets.QFrame(self.frame)
        self.l1.setToolTip("")
        self.l1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.l1.setFrameShape(QtWidgets.QFrame.HLine)
        self.l1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l1.setObjectName("l1")
        self.gridLayoutMenu.addWidget(self.l1, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayoutMenu.addWidget(self.label_3, 12, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutMenu.addWidget(self.line, 11, 0, 1, 1)
        self.gridLayoutEncrypted = QtWidgets.QGridLayout()
        self.gridLayoutEncrypted.setObjectName("gridLayoutEncrypted")
        self.cb_gzipped = QtWidgets.QCheckBox(self.frame)
        self.cb_gzipped.setEnabled(False)
        self.cb_gzipped.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cb_gzipped.setObjectName("cb_gzipped")
        self.gridLayoutEncrypted.addWidget(self.cb_gzipped, 0, 1, 1, 1)
        self.cb_encrypted = QtWidgets.QCheckBox(self.frame)
        self.cb_encrypted.setEnabled(False)
        self.cb_encrypted.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_encrypted.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cb_encrypted.setObjectName("cb_encrypted")
        self.gridLayoutEncrypted.addWidget(self.cb_encrypted, 0, 0, 1, 1)
        self.cb_raw = QtWidgets.QCheckBox(self.frame)
        self.cb_raw.setEnabled(False)
        self.cb_raw.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cb_raw.setObjectName("cb_raw")
        self.gridLayoutEncrypted.addWidget(self.cb_raw, 0, 2, 1, 1)
        self.cb_modified = QtWidgets.QCheckBox(self.frame)
        self.cb_modified.setEnabled(False)
        self.cb_modified.setObjectName("cb_modified")
        self.gridLayoutEncrypted.addWidget(self.cb_modified, 0, 3, 1, 1)
        self.gridLayoutMenu.addLayout(self.gridLayoutEncrypted, 10, 0, 1, 1)
        self.gridLayoutAdd = QtWidgets.QGridLayout()
        self.gridLayoutAdd.setObjectName("gridLayoutAdd")
        self.pb_add_folder = QtWidgets.QPushButton(self.frame)
        self.pb_add_folder.setEnabled(False)
        self.pb_add_folder.setToolTip("")
        self.pb_add_folder.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_add_folder.setObjectName("pb_add_folder")
        self.gridLayoutAdd.addWidget(self.pb_add_folder, 0, 1, 1, 1)
        self.pb_add_file = QtWidgets.QPushButton(self.frame)
        self.pb_add_file.setEnabled(False)
        self.pb_add_file.setToolTip("")
        self.pb_add_file.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_add_file.setObjectName("pb_add_file")
        self.gridLayoutAdd.addWidget(self.pb_add_file, 0, 0, 1, 1)
        self.pb_add_bnd = QtWidgets.QPushButton(self.frame)
        self.pb_add_bnd.setEnabled(False)
        self.pb_add_bnd.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_add_bnd.setObjectName("pb_add_bnd")
        self.gridLayoutAdd.addWidget(self.pb_add_bnd, 0, 2, 1, 1)
        self.gridLayoutMenu.addLayout(self.gridLayoutAdd, 0, 0, 1, 1)
        self.gridLayoutExtractMove = QtWidgets.QGridLayout()
        self.gridLayoutExtractMove.setObjectName("gridLayoutExtractMove")
        self.pb_paste = QtWidgets.QPushButton(self.frame)
        self.pb_paste.setEnabled(False)
        self.pb_paste.setToolTip("")
        self.pb_paste.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_paste.setAutoRepeat(True)
        self.pb_paste.setObjectName("pb_paste")
        self.gridLayoutExtractMove.addWidget(self.pb_paste, 1, 1, 1, 1)
        self.pb_copy = QtWidgets.QPushButton(self.frame)
        self.pb_copy.setEnabled(False)
        self.pb_copy.setToolTip("")
        self.pb_copy.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_copy.setAutoRepeat(True)
        self.pb_copy.setObjectName("pb_copy")
        self.gridLayoutExtractMove.addWidget(self.pb_copy, 1, 0, 1, 1)
        self.pb_extract_file = QtWidgets.QPushButton(self.frame)
        self.pb_extract_file.setEnabled(False)
        self.pb_extract_file.setToolTip("")
        self.pb_extract_file.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_extract_file.setObjectName("pb_extract_file")
        self.gridLayoutExtractMove.addWidget(self.pb_extract_file, 0, 0, 1, 1)
        self.pb_replace_file = QtWidgets.QPushButton(self.frame)
        self.pb_replace_file.setEnabled(False)
        self.pb_replace_file.setToolTip("")
        self.pb_replace_file.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_replace_file.setObjectName("pb_replace_file")
        self.gridLayoutExtractMove.addWidget(self.pb_replace_file, 0, 1, 1, 1)
        self.gridLayoutMenu.addLayout(self.gridLayoutExtractMove, 2, 0, 1, 1)
        self.gridLayoutSizeCRC = QtWidgets.QGridLayout()
        self.gridLayoutSizeCRC.setObjectName("gridLayoutSizeCRC")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setObjectName("label")
        self.gridLayoutSizeCRC.addWidget(self.label, 0, 0, 1, 1)
        self.le_size = QtWidgets.QLineEdit(self.frame)
        self.le_size.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.le_size.setPalette(palette)
        self.le_size.setMouseTracking(False)
        self.le_size.setAcceptDrops(False)
        self.le_size.setToolTip("<html><head/><body><p>None</p></body></html>")
        self.le_size.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.le_size.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.le_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_size.setReadOnly(True)
        self.le_size.setObjectName("le_size")
        self.gridLayoutSizeCRC.addWidget(self.le_size, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName("label_2")
        self.gridLayoutSizeCRC.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_crc = QtWidgets.QLineEdit(self.frame)
        self.le_crc.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.le_crc.setPalette(palette)
        self.le_crc.setMouseTracking(False)
        self.le_crc.setAcceptDrops(False)
        self.le_crc.setToolTip("<html><head/><body><p>None</p></body></html>")
        self.le_crc.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.le_crc.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.le_crc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_crc.setReadOnly(True)
        self.le_crc.setObjectName("le_crc")
        self.gridLayoutSizeCRC.addWidget(self.le_crc, 1, 1, 1, 1)
        self.gridLayoutMenu.addLayout(self.gridLayoutSizeCRC, 5, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayoutMenu, 0, 0, 1, 1)
        self.gridLayoutMain.addWidget(self.frame)
        self.gridLayoutMain.setStretch(0, 5)
        self.gridLayoutMain.setStretch(1, 3)
        self.verticalLayout.addLayout(self.gridLayoutMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_load = QtWidgets.QAction(MainWindow)
        self.action_load.setObjectName("action_load")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_refresh = QtWidgets.QAction(MainWindow)
        self.action_refresh.setObjectName("action_refresh")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setEnabled(False)
        self.action_save_as.setObjectName("action_save_as")
        self.action_disable_filesystem_and_save = QtWidgets.QAction(MainWindow)
        self.action_disable_filesystem_and_save.setEnabled(False)
        self.action_disable_filesystem_and_save.setObjectName("action_disable_filesystem_and_save")
        self.action_overwrite_all_filenames = QtWidgets.QAction(MainWindow)
        self.action_overwrite_all_filenames.setEnabled(False)
        self.action_overwrite_all_filenames.setObjectName("action_overwrite_all_filenames")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.check_reload_on_save = QtWidgets.QAction(MainWindow)
        self.check_reload_on_save.setCheckable(True)
        self.check_reload_on_save.setObjectName("check_reload_on_save")
        self.check_extended_backup_files = QtWidgets.QAction(MainWindow)
        self.check_extended_backup_files.setCheckable(True)
        self.check_extended_backup_files.setObjectName("check_extended_backup_files")
        self.check_encryption_decryption = QtWidgets.QAction(MainWindow)
        self.check_encryption_decryption.setCheckable(False)
        self.check_encryption_decryption.setEnabled(False)
        self.check_encryption_decryption.setObjectName("check_encryption_decryption")
        self.check_external_header_file = QtWidgets.QAction(MainWindow)
        self.check_external_header_file.setCheckable(True)
        self.check_external_header_file.setEnabled(False)
        self.check_external_header_file.setObjectName("check_external_header_file")
        self.action_load_datams = QtWidgets.QAction(MainWindow)
        self.action_load_datams.setObjectName("action_load_datams")
        self.menuFile.addAction(self.action_load)
        self.menuFile.addAction(self.action_load_datams)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_save_as)
        self.menuFile.addAction(self.action_refresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)
        self.menuHelp.addAction(self.action_about)
        self.menuActions.addAction(self.action_disable_filesystem_and_save)
        self.menuActions.addAction(self.action_overwrite_all_filenames)
        self.menuSettings.addAction(self.check_reload_on_save)
        self.menuSettings.addAction(self.check_extended_backup_files)
        self.menuSettings.addAction(self.check_encryption_decryption)
        self.menuSettings.addAction(self.check_external_header_file)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patapon BND Editor"))
        self.treeWidget.setSortingEnabled(False)
        self.pb_open.setText(_translate("MainWindow", "Open local .BND file (→)"))
        self.pb_open.setShortcut(_translate("MainWindow", "Right"))
        self.te_preview.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Mono\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.pb_back.setText(_translate("MainWindow", "Back to previous file (←)"))
        self.pb_back.setShortcut(_translate("MainWindow", "Left"))
        self.pb_delete_file.setText(_translate("MainWindow", "Delete file(s)"))
        self.label_3.setText(_translate("MainWindow", "File data preview (first 0x70 bytes)"))
        self.cb_gzipped.setText(_translate("MainWindow", "Gzipped"))
        self.cb_encrypted.setText(_translate("MainWindow", "Encrypted"))
        self.cb_raw.setText(_translate("MainWindow", "Raw"))
        self.cb_modified.setText(_translate("MainWindow", "Modified"))
        self.pb_add_folder.setText(_translate("MainWindow", "Add folder"))
        self.pb_add_file.setText(_translate("MainWindow", "Add file(s)"))
        self.pb_add_bnd.setText(_translate("MainWindow", "Add BND"))
        self.pb_paste.setText(_translate("MainWindow", "Paste"))
        self.pb_copy.setText(_translate("MainWindow", "Copy"))
        self.pb_extract_file.setText(_translate("MainWindow", "Extract file(s)"))
        self.pb_replace_file.setText(_translate("MainWindow", "Replace file(s)"))
        self.label.setText(_translate("MainWindow", " Size"))
        self.le_size.setText(_translate("MainWindow", "Size "))
        self.label_2.setText(_translate("MainWindow", " CRC"))
        self.le_crc.setText(_translate("MainWindow", "CRC "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.action_load.setText(_translate("MainWindow", "Load BND"))
        self.action_load.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_refresh.setText(_translate("MainWindow", "Refresh"))
        self.action_refresh.setShortcut(_translate("MainWindow", "F5"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_save_as.setText(_translate("MainWindow", "Save as"))
        self.action_disable_filesystem_and_save.setText(_translate("MainWindow", "Disable filesystem and save"))
        self.action_overwrite_all_filenames.setText(_translate("MainWindow", "Overwrite all filenames"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.check_reload_on_save.setText(_translate("MainWindow", "Reload on save"))
        self.check_extended_backup_files.setText(_translate("MainWindow", "Disable backups"))
        self.check_encryption_decryption.setText(_translate("MainWindow", "Encryption / decryption"))
        self.check_external_header_file.setText(_translate("MainWindow", "External header file"))
        self.action_load_datams.setText(_translate("MainWindow", "Load DATAMS"))
from interface.tree_widget_bundle import QTreeWidgetBundle


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
