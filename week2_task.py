import sys
from PyQt5.QtWidgets import *
import qt_material

class User_Regist(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Week 2: Layout - User Registration Form")
        self.setFixedSize(500, 650)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.identitas_section())
        main_layout.addWidget(self.navigation_section())
        main_layout.addWidget(self.registration_section())
        main_layout.addWidget(self.actions_section())

        self.setLayout(main_layout)

    def identitas_section(self):
        identitas_box = QGroupBox("Identitas")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama\t:    Dhinda Tsamara Shalsabilla"))
        identitas_layout.addWidget(QLabel("Nim\t:    F1D022005"))
        identitas_layout.addWidget(QLabel("Kelas\t:    C"))
        identitas_box.setLayout(identitas_layout)
        return identitas_box

    def navigation_section(self):
        navigation_box = QGroupBox("Navigation")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        navigation_box.setLayout(nav_layout)
        return navigation_box

    def registration_section(self):
        registration_box = QGroupBox("User Registration")
        outer_layout = QVBoxLayout() 
        center_layout = QHBoxLayout()
        form_layout = QFormLayout()

        full_name_input = QLineEdit()
        email_input = QLineEdit()
        phone_input = QLineEdit()

        gender_layout = QHBoxLayout()
        male_radio = QRadioButton("Male")
        female_radio = QRadioButton("Female")
        gender_layout.addWidget(male_radio)
        gender_layout.addWidget(female_radio)

        country_dropdown = QComboBox()  
        country_dropdown.addItems(["Select Country","Indonesia", "Other"])

        form_layout.addRow("Full Name:", full_name_input)
        form_layout.addRow("Email:", email_input)
        form_layout.addRow("Phone:", phone_input)
        form_layout.addRow("Gender:", gender_layout)
        form_layout.addRow("Country:", country_dropdown)

        center_layout.addStretch()  
        center_layout.addLayout(form_layout)
        center_layout.addStretch()

        outer_layout.addLayout(center_layout)
        registration_box.setLayout(outer_layout)

        return registration_box

    def actions_section(self):
        actions_box = QGroupBox("Actions")
        actions_layout = QHBoxLayout()

        submit_btn = QPushButton("Submit")
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(QApplication.instance().quit)

        actions_layout.addWidget(submit_btn)
        actions_layout.addWidget(cancel_btn)
        actions_box.setLayout(actions_layout)

        return actions_box

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qt_material.apply_stylesheet(app, theme="light_blue.xml")
    window = User_Regist()
    window.show()
    sys.exit(app.exec_())