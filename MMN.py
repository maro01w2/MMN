import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QMessageBox


class CustomerDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Customer Details')
        self.setGeometry(100, 100, 500, 600)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        self.input_bedrooms = QLineEdit(self)
        self.input_bedrooms.setPlaceholderText('Number of bedrooms')
        grid_layout.addWidget(self.input_bedrooms, 0, 1)

        self.input_bathrooms = QLineEdit(self)
        self.input_bathrooms.setPlaceholderText('Number of bathrooms')
        grid_layout.addWidget(self.input_bathrooms, 1, 1)

        self.input_kitchen = QLineEdit(self)
        self.input_kitchen.setPlaceholderText('Kitchen condition (original/good/recently renovated)')
        grid_layout.addWidget(self.input_kitchen, 2, 1)

        self.input_roof = QLineEdit(self)
        self.input_roof.setPlaceholderText('Roof condition (original/good/recently renovated)')
        grid_layout.addWidget(self.input_roof, 3, 1)

        self.input_foundation = QLineEdit(self)
        self.input_foundation.setPlaceholderText('Foundation condition (original/good/recently renovated)')
        grid_layout.addWidget(self.input_foundation, 4, 1)

        self.input_bathroom_repair = QLineEdit(self)
        self.input_bathroom_repair.setPlaceholderText('Bathroom repair status (original/good/recently renovated)')
        grid_layout.addWidget(self.input_bathroom_repair, 5, 1)

        self.input_furnace = QLineEdit(self)
        self.input_furnace.setPlaceholderText('Furnace condition (original/good/recently renovated)')
        grid_layout.addWidget(self.input_furnace, 6, 1)

        self.input_hvac = QLineEdit(self)
        self.input_hvac.setPlaceholderText('HVAC condition (original/good/recently renovated)')
        grid_layout.addWidget(self.input_hvac, 7, 1)

        self.input_living_status = QLineEdit(self)
        self.input_living_status.setPlaceholderText('Living status (owner/tenant)')
        grid_layout.addWidget(self.input_living_status, 8, 1)

        self.input_rental_period = QLineEdit(self)
        self.input_rental_period.setPlaceholderText('Rental period (monthly/annually)')
        grid_layout.addWidget(self.input_rental_period, 9, 1)

        self.input_sale_reason = QLineEdit(self)
        self.input_sale_reason.setPlaceholderText('Reason for sale')
        grid_layout.addWidget(self.input_sale_reason, 10, 1)

        self.input_market_price = QLineEdit(self)
        self.input_market_price.setPlaceholderText('Market price')
        grid_layout.addWidget(self.input_market_price, 11, 1)

        self.input_agreed_price = QLineEdit(self)
        self.input_agreed_price.setPlaceholderText('Agreed price')
        grid_layout.addWidget(self.input_agreed_price, 12, 1)

        self.input_full_name = QLineEdit(self)
        self.input_full_name.setPlaceholderText('Full name')
        grid_layout.addWidget(self.input_full_name, 13, 1)

        self.input_address = QLineEdit(self)
        self.input_address.setPlaceholderText('Address')
        grid_layout.addWidget(self.input_address, 14, 1)

        self.input_zip_code = QLineEdit(self)
        self.input_zip_code.setPlaceholderText('ZIP code')
        grid_layout.addWidget(self.input_zip_code, 15, 1)

        self.input_phone_number = QLineEdit(self)
        self.input_phone_number.setPlaceholderText('Preferred contact number')
        grid_layout.addWidget(self.input_phone_number, 16, 1)

        self.save_button = QPushButton('Save', self)
        self.save_button.clicked.connect(self.save_customer_details)
        grid_layout.addWidget(self.save_button, 17, 0, 1, 2)

        self.note_label = QLabel('Note: If any information is not provided, replace it with a hyphen ("-").', self)
        grid_layout.addWidget(self.note_label, 18, 0, 1, 2)

        self.info_button = QPushButton('About', self)
        self.info_button.clicked.connect(self.show_info_message)
        grid_layout.addWidget(self.info_button, 19, 0, 1, 2)

        vbox = QVBoxLayout()
        vbox.addLayout(grid_layout)
        self.setLayout(vbox)

    def save_customer_details(self):
        # التحقق من إدخال بيانات
        if (self.input_bedrooms.text() or
                self.input_bathrooms.text() or
                self.input_kitchen.text() or
                self.input_roof.text() or
                self.input_foundation.text() or
                self.input_bathroom_repair.text() or
                self.input_furnace.text() or
                self.input_hvac.text() or
                self.input_living_status.text() or
                self.input_rental_period.text() or
                self.input_sale_reason.text() or
                self.input_market_price.text() or
                self.input_agreed_price.text() or
                self.input_full_name.text() or
                self.input_address.text() or
                self.input_zip_code.text() or
                self.input_phone_number.text()):
            with open("customers.txt", "a") as file:
                file.write("Customer Details:\n")
                file.write(f"Bedrooms: {self.input_bedrooms.text()}\n")
                file.write(f"Bathrooms: {self.input_bathrooms.text()}\n")
                file.write(f"Kitchen condition: {self.input_kitchen.text()}\n")
                file.write(f"Roof condition: {self.input_roof.text()}\n")
                file.write(f"Foundation condition: {self.input_foundation.text()}\n")
                file.write(f"Bathroom repair status: {self.input_bathroom_repair.text()}\n")
                file.write(f"Furnace condition: {self.input_furnace.text()}\n")
                file.write(f"HVAC condition: {self.input_hvac.text()}\n")
                file.write(f"Living status: {self.input_living_status.text()}\n")
                file.write(f"Rental period: {self.input_rental_period.text()}\n")
                file.write(f"Sale reason: {self.input_sale_reason.text()}\n")
                file.write(f"Market price: {self.input_market_price.text()}\n")
                file.write(f"Agreed price: {self.input_agreed_price.text()}\n")
                file.write(f"Full name: {self.input_full_name.text()}\n")
                file.write(f"Address: {self.input_address.text()}\n")
                file.write(f"ZIP code: {self.input_zip_code.text()}\n")
                file.write(f"Preferred contact number: {self.input_phone_number.text()}\n\n")
            # بعد الحفظ، قم بمسح محتوى الحقول النصية
            self.input_bedrooms.clear()
            self.input_bathrooms.clear()
            self.input_kitchen.clear()
            self.input_roof.clear()
            self.input_foundation.clear()
            self.input_bathroom_repair.clear()
            self.input_furnace.clear()
            self.input_hvac.clear()
            self.input_living_status.clear()
            self.input_rental_period.clear()
            self.input_sale_reason.clear()
            self.input_market_price.clear()
            self.input_agreed_price.clear()
            self.input_full_name.clear()
            self.input_address.clear()
            self.input_zip_code.clear()
            self.input_phone_number.clear()
        else:
            # إذا لم يتم إدخال أي بيانات، عرض رسالة خطأ
            QMessageBox.warning(self, 'Warning', 'Please enter at least some information.')

    def show_info_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("About")
        msg_box.setText(
            "This program is developed by Marwan Mohamed.\n\n"
            "Any violation or theft of content or code may subject you to legal consequences."
        )
        msg_box.exec()


def main():
    app = QApplication(sys.argv)
    window = CustomerDetails()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
