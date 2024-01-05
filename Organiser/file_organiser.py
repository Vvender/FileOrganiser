import os
import shutil
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog
from ExceptionHandler.exception_handler import CustomExceptionHandler


class FileOrganiser:
    def __init__(self, app, ui):
        self.app = app
        self.ui = ui

    def select_location(self):
        try:
            location = QFileDialog.getExistingDirectory(self.app.activeWindow(), "Select Directory")
            self.ui.lbl_file_location.setText(location)
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(
                f"An error occurred during selecting file location,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
            self.close_connection()

    def organise_files(self):
        try:
            location = self.ui.lbl_file_location.text()  # Get the selected location from the label
            file_types = {
                "Documents": [".docx", ".pdf", ".txt", ".pptx", ".xlsx", ".csv", ".html", ".rtf", ".doc"],
                "Images": [".jpg", ".JPG", ".jpeg", ".jfif", ".png", ".gif", ".bmp"],
                "Videos": [".mp4", ".avi", ".mov", ".mkv"],
                "Audios": [".mp3", ".wav", ".flac", ".aac"],
                "Compressed Files": [".zip", ".rar"],
                "Program Files": [".exe", ".dmg", ".msi"]
            }
            checkbox_mapping = {
                "Documents": self.ui.cb_documents,
                "Images": self.ui.cb_images,
                "Videos": self.ui.cb_videos,
                "Audios": self.ui.cb_audios,
                "Compressed Files": self.ui.cb_compressed_files,
                "Program Files": self.ui.cb_program_files
            }
            if location == "Select File Location" or location == "":
                self.ui.lbl_info_message.setText("Please select \na file location.")
                self.ui.lbl_icon_organised.setPixmap(QtGui.QPixmap(":/Icons/x-square.svg"))
                self.ui.pages.setCurrentIndex(1)
            elif not any(checkbox.isChecked() for checkbox in checkbox_mapping.values()):
                self.ui.lbl_info_message.setText("Please select \nthe file types \nyou want to organise.")
                self.ui.lbl_icon_organised.setPixmap(QtGui.QPixmap(":/Icons/x-square.svg"))
                self.ui.pages.setCurrentIndex(1)

            else:
                for category, extensions in file_types.items():
                    checkbox = checkbox_mapping[category]  # Get the checkbox for the current category
                    if checkbox.isChecked():  # Check if the checkbox is checked
                        category_folder = os.path.join(location, category)
                        os.makedirs(category_folder, exist_ok=True)  # Create the category folder if it doesn't exist
                        for ext in extensions:
                            files = [file for file in os.listdir(location) if file.endswith(ext)]
                            for file in files:
                                shutil.move(os.path.join(location, file),
                                            os.path.join(category_folder, file))  # Move the file to the category folder
                self.ui.lbl_info_message.setText("Your files have been \nsuccessfully organised.")
                self.ui.lbl_icon_organised.setPixmap(QtGui.QPixmap(":/Icons/check-circle .svg"))
                self.ui.pages.setCurrentIndex(1)

        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(
                f"An error occurred during organising files,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
            self.close_connection()
