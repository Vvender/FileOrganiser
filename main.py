import sys
from PyQt5.QtWidgets import QApplication, QWidget
from EventHandler.event_handler import EventHandler
from Organiser.file_organiser import FileOrganiser
from Gui.ui_file_organiser import Ui_OrganiserForm


class MainWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui_window = QWidget()
        self.ui = Ui_OrganiserForm()
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Create an instance of EventHandler and pass the app and ui objects
        self.event_handler = EventHandler(self.app, self.ui)
        self.file_organiser = FileOrganiser(self.app, self.ui)

        # Main Button Events
        self.ui.btn_github.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_linkedin.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_cv.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_email.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_info_return.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_close.clicked.connect(self.app.quit)

        # Organiser Button Event
        self.ui.btn_file_location.clicked.connect(self.file_organiser.select_location)
        self.ui.btn_organise_files.clicked.connect(self.file_organiser.organise_files)


if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
