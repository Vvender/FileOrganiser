from PyQt5 import QtCore, QtGui, QtWidgets
import Gui.Icons.organiser_rc as organiser_rc


class Ui_OrganiserForm(object):
    def setupUi(self, OrganiserForm):
        OrganiserForm.setObjectName("OrganiserForm")
        OrganiserForm.resize(500, 350)
        OrganiserForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        OrganiserForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        OrganiserForm.setMinimumSize(QtCore.QSize(500, 350))
        OrganiserForm.setMaximumSize(QtCore.QSize(500, 350))
        OrganiserForm.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(OrganiserForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frm_outer = QtWidgets.QFrame(OrganiserForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_outer.sizePolicy().hasHeightForWidth())
        self.frm_outer.setSizePolicy(sizePolicy)
        self.frm_outer.setMaximumSize(QtCore.QSize(800, 600))
        self.frm_outer.setStyleSheet("background-color:#2596be;\n"
                                     "border-radius:20px;\n"
                                     "")
        self.frm_outer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_outer.setObjectName("frm_outer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frm_outer)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frm_middle = QtWidgets.QFrame(self.frm_outer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_middle.sizePolicy().hasHeightForWidth())
        self.frm_middle.setSizePolicy(sizePolicy)
        self.frm_middle.setStyleSheet(
            "background-color:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:0.715909,stop:0 rgba(0,0,0,9), stop:0.375 rgba(0,0,0,50),stop:0.835227 rgba(0,0,0,75));\n"
            "border-radius:20px;\n"
            "")
        self.frm_middle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_middle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_middle.setObjectName("frm_middle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frm_middle)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frm_inside = QtWidgets.QFrame(self.frm_middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_inside.sizePolicy().hasHeightForWidth())
        self.frm_inside.setSizePolicy(sizePolicy)
        self.frm_inside.setStyleSheet("background-color:rgba(0,0,0,100);\n"
                                      "border-radius:15px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.frm_inside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_inside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_inside.setObjectName("frm_inside")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frm_inside)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frm_header = QtWidgets.QFrame(self.frm_inside)
        self.frm_header.setMinimumSize(QtCore.QSize(0, 50))
        self.frm_header.setStyleSheet("background-color:#0b1e3b;\n"
                                      "border-radius:15px;\n"
                                      "")
        self.frm_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_header.setObjectName("frm_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frm_contact_info = QtWidgets.QFrame(self.frm_header)
        self.frm_contact_info.setStyleSheet("QPushButton{\n"
                                            "    background-color: transparent;\n"
                                            "    color:rgba(255, 255, 255, 210);\n"
                                            "    border-radius:5px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "    padding-left:5px;\n"
                                            "    padding-top:5px;\n"
                                            "    background-color:rgba(105, 118, 132, 200);\n"
                                            "}")
        self.frm_contact_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_contact_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_contact_info.setObjectName("frm_contact_info")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frm_contact_info)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_github = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_github.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_github.setIcon(icon)
        self.btn_github.setIconSize(QtCore.QSize(40, 40))
        self.btn_github.setObjectName("btn_github")
        self.horizontalLayout_3.addWidget(self.btn_github)
        self.btn_linkedin = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_linkedin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_linkedin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/linkedin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_linkedin.setIcon(icon1)
        self.btn_linkedin.setIconSize(QtCore.QSize(40, 40))
        self.btn_linkedin.setObjectName("btn_linkedin")
        self.horizontalLayout_3.addWidget(self.btn_linkedin)
        self.btn_cv = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_cv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cv.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/paperclip.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cv.setIcon(icon2)
        self.btn_cv.setIconSize(QtCore.QSize(40, 40))
        self.btn_cv.setObjectName("btn_cv")
        self.horizontalLayout_3.addWidget(self.btn_cv)
        self.btn_email = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_email.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/mail.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_email.setIcon(icon3)
        self.btn_email.setIconSize(QtCore.QSize(40, 40))
        self.btn_email.setObjectName("btn_email")
        self.horizontalLayout_3.addWidget(self.btn_email)
        self.horizontalLayout.addWidget(self.frm_contact_info, 0, QtCore.Qt.AlignLeft)
        self.frm_top_right = QtWidgets.QFrame(self.frm_header)
        self.frm_top_right.setStyleSheet("QPushButton{\n"
                                         "    background-color: transparent;\n"
                                         "    color:rgba(255, 255, 255, 210);\n"
                                         "    border-radius:5px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    padding-left:5px;\n"
                                         "    padding-top:5px;\n"
                                         "    background-color:rgba(105, 118, 132, 200);\n"
                                         "}")
        self.frm_top_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_top_right.setObjectName("frm_top_right")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frm_top_right)
        self.horizontalLayout_2.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_minimize = QtWidgets.QPushButton(self.frm_top_right)
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon4)
        self.btn_minimize.setIconSize(QtCore.QSize(40, 40))
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_2.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frm_top_right)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QtCore.QSize(40, 40))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frm_top_right, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frm_header)
        self.pages = QtWidgets.QStackedWidget(self.frm_inside)
        self.pages.setStyleSheet("background-color: transparent;\n"
                                 "border-radius:15px;")
        self.pages.setObjectName("pages")
        self.page_organise = QtWidgets.QWidget()
        self.page_organise.setObjectName("page_organise")
        self.lbl_file_location = QtWidgets.QLabel(self.page_organise)
        self.lbl_file_location.setGeometry(QtCore.QRect(20, 20, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_file_location.setFont(font)
        self.lbl_file_location.setStyleSheet("background-color:transparent;\n"
                                             "color: #2586be;\n"
                                             "border-radius:15px;\n"
                                             "border:2px solid #2586be;")
        self.lbl_file_location.setWordWrap(False)
        self.lbl_file_location.setObjectName("lbl_file_location")
        self.btn_file_location = QtWidgets.QPushButton(self.page_organise)
        self.btn_file_location.setGeometry(QtCore.QRect(385, 14, 50, 50))
        self.btn_file_location.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_file_location.setStyleSheet("QPushButton{\n"
                                             "    background-color: transparent;\n"
                                             "    color:rgba(255, 255, 255, 210);\n"
                                             "    border-radius:5px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "    padding-left:5px;\n"
                                             "    padding-top:5px;\n"
                                             "    background-color:rgba(105, 118, 132, 200);\n"
                                             "}")
        self.btn_file_location.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_file_location.setIcon(icon6)
        self.btn_file_location.setIconSize(QtCore.QSize(50, 50))
        self.btn_file_location.setObjectName("btn_file_location")
        self.frm_checkbox = QtWidgets.QFrame(self.page_organise)
        self.frm_checkbox.setGeometry(QtCore.QRect(20, 70, 191, 161))
        self.frm_checkbox.setStyleSheet("background-color:transparent;\n"
                                        "color: #2586be;\n"
                                        "border-radius:15px;")
        self.frm_checkbox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_checkbox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_checkbox.setObjectName("frm_checkbox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frm_checkbox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cb_documents = QtWidgets.QCheckBox(self.frm_checkbox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_documents.setFont(font)
        self.cb_documents.setObjectName("cb_documents")
        self.verticalLayout_5.addWidget(self.cb_documents)
        self.cb_images = QtWidgets.QCheckBox(self.frm_checkbox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_images.setFont(font)
        self.cb_images.setObjectName("cb_images")
        self.verticalLayout_5.addWidget(self.cb_images)
        self.cb_videos = QtWidgets.QCheckBox(self.frm_checkbox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_videos.setFont(font)
        self.cb_videos.setObjectName("cb_videos")
        self.verticalLayout_5.addWidget(self.cb_videos)
        self.cb_audios = QtWidgets.QCheckBox(self.frm_checkbox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_audios.setFont(font)
        self.cb_audios.setObjectName("cb_audios")
        self.verticalLayout_5.addWidget(self.cb_audios)
        self.cb_compressed_files = QtWidgets.QCheckBox(self.frm_checkbox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_compressed_files.setFont(font)
        self.cb_compressed_files.setObjectName("cb_compressed")
        self.verticalLayout_5.addWidget(self.cb_compressed_files)
        self.cb_program_files = QtWidgets.QCheckBox(self.frm_checkbox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_program_files.setFont(font)
        self.cb_program_files.setObjectName("cb_program")
        self.verticalLayout_5.addWidget(self.cb_program_files)
        self.btn_organise_files = QtWidgets.QPushButton(self.page_organise)
        self.btn_organise_files.setGeometry(QtCore.QRect(260, 120, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_organise_files.setFont(font)
        self.btn_organise_files.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_organise_files.setStyleSheet("QPushButton#btn_organise_files{\n"
                                              "    background-color: #0b1e3b;\n"
                                              "    color: #2596be;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 8px 10px; /* Adjust the padding for the pop-up effect */\n"
                                              "    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Add a box shadow for the pop-up effect */\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton#btn_organise_files:hover{\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 150, 190, 200), stop:1 rgba(85, 98, 112, 226));\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton#btn_organise_files:pressed{\n"
                                              "    padding-left: 8px;\n"
                                              "    padding-top: 10px;\n"
                                              "    background-color: rgba(105, 118, 132, 200);\n"
                                              "    box-shadow: none; /* Remove the box shadow when pressed */\n"
                                              "}")
        self.btn_organise_files.setObjectName("btn_organise_files")
        self.pages.addWidget(self.page_organise)
        self.page_info = QtWidgets.QWidget()
        self.page_info.setObjectName("page_info")
        self.lbl_info_message = QtWidgets.QLabel(self.page_info)
        self.lbl_info_message.setGeometry(QtCore.QRect(90, 90, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_info_message.setFont(font)
        self.lbl_info_message.setStyleSheet("background-color:transparent;\n"
                                            "color: #2586be;\n"
                                            "border-radius:15px;\n"
                                            "\n"
                                            "")
        self.lbl_info_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info_message.setWordWrap(True)
        self.lbl_info_message.setObjectName("lbl_info_message")
        self.btn_info_return = QtWidgets.QPushButton(self.page_info)
        self.btn_info_return.setGeometry(QtCore.QRect(150, 170, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_info_return.setFont(font)
        self.btn_info_return.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_info_return.setStyleSheet("QPushButton#btn_info_return{\n"
                                           "    background-color: #0b1e3b;\n"
                                           "    color:#2596be;\n"
                                           "    border-radius:5px;\n"
                                           "}\n"
                                           "QPushButton#btn_info_return:hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 150, 190 200), stop:1 rgba(85, 98, 112, 226));\n"
                                           "}\n"
                                           "QPushButton#btn_info_return:pressed{\n"
                                           "    padding-left:5px;\n"
                                           "    padding-top:5px;\n"
                                           "    background-color:rgba(85, 98, 112, 226);\n"
                                           "}")
        self.btn_info_return.setObjectName("btn_info_return")
        self.lbl_icon_organised = QtWidgets.QLabel(self.page_info)
        self.lbl_icon_organised.setGeometry(QtCore.QRect(185, 10, 71, 71))
        self.lbl_icon_organised.setText("")
        self.lbl_icon_organised.setPixmap(QtGui.QPixmap(":/Icons/check-circle .svg"))
        self.lbl_icon_organised.setScaledContents(True)
        self.lbl_icon_organised.setObjectName("lbl_icon_organised")
        self.pages.addWidget(self.page_info)
        self.verticalLayout_4.addWidget(self.pages)
        self.verticalLayout_2.addWidget(self.frm_inside)
        self.verticalLayout_3.addWidget(self.frm_middle)
        self.verticalLayout.addWidget(self.frm_outer)

        self.retranslateUi(OrganiserForm)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OrganiserForm)
        OrganiserForm.setTabOrder(self.btn_github, self.btn_linkedin)
        OrganiserForm.setTabOrder(self.btn_linkedin, self.btn_cv)
        OrganiserForm.setTabOrder(self.btn_cv, self.btn_email)
        OrganiserForm.setTabOrder(self.btn_email, self.btn_minimize)
        OrganiserForm.setTabOrder(self.btn_minimize, self.btn_close)
        OrganiserForm.setTabOrder(self.btn_close, self.btn_file_location)
        OrganiserForm.setTabOrder(self.btn_file_location, self.cb_documents)
        OrganiserForm.setTabOrder(self.cb_documents, self.cb_images)
        OrganiserForm.setTabOrder(self.cb_images, self.cb_videos)
        OrganiserForm.setTabOrder(self.cb_videos, self.cb_audios)
        OrganiserForm.setTabOrder(self.cb_audios, self.cb_compressed_files)
        OrganiserForm.setTabOrder(self.cb_compressed_files, self.cb_program_files)
        OrganiserForm.setTabOrder(self.cb_program_files, self.btn_organise_files)
        OrganiserForm.setTabOrder(self.btn_organise_files, self.btn_info_return)

    def retranslateUi(self, OrganiserForm):
        _translate = QtCore.QCoreApplication.translate
        OrganiserForm.setWindowTitle(_translate("OrganiserForm", "File Organiser"))
        self.lbl_file_location.setText(_translate("OrganiserForm", "Select File Location"))
        self.cb_documents.setText(_translate("OrganiserForm", "Documents"))
        self.cb_images.setText(_translate("OrganiserForm", "Images"))
        self.cb_videos.setText(_translate("OrganiserForm", "Videos"))
        self.cb_audios.setText(_translate("OrganiserForm", "Audios"))
        self.cb_compressed_files.setText(_translate("OrganiserForm", "Compressed Files"))
        self.cb_program_files.setText(_translate("OrganiserForm", "Program Files"))
        self.btn_organise_files.setText(_translate("OrganiserForm", "ORGANISE"))
        self.btn_info_return.setText(_translate("OrganiserForm", "RETURN"))
        self.lbl_info_message.setText(_translate("OrganiserForm",
                                                 "Your files have been \nsuccesfully organised."))

