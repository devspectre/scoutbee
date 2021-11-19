from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout

class APIView(QFrame):
	'''
	API Hive View
	'''

	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.layout = QVBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(10)
		self.layout.setAlignment(Qt.AlignTop|Qt.AlignLeft)

		self.api_key_label = QLabel(self)
		self.api_key_label.setText('Hive API Key')
		self.api_key_label.setObjectName('LabelBig')
		self.api_key_label.setAlignment(Qt.AlignLeft)

		self.api_key_edit = QLineEdit(self)
		self.api_key_edit.setAlignment(Qt.AlignLeft)
		self.api_key_edit.setObjectName('TextEditBig')
		self.api_key_edit.setFont(QFont('Open Sans', 14, QFont.DemiBold))
		self.api_key_edit.setFixedSize(362, 34)

		self.layout.addWidget(self.api_key_label)
		self.layout.addWidget(self.api_key_edit)

		self.setStyleSheet("""#LabelBig{font-family: 'Open Sans'; font-size: 14px; color: #858796}

			#TextEditBig{background-color: white; border: 1px solid #D1D3E2; border-radius: 5px; padding: 5px;
				font: 750 14px 'Open Sans'}""")

	def set_api_key(self, key):

		self.api_key_edit.setText(key)

	def api_key(self):

		return self.api_key_edit.text()

if __name__ == '__main__':
	
	from PyQt5.QtWidgets import QWidget, QApplication
	import sys
	
	app = QApplication(sys.argv)

	window = QWidget()

	view = APIView(window)
	view.setFixedSize(450, 480)

	window.show()

	sys.exit(app.exec())