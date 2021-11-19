from PyQt5.QtCore import Qt, QRegExp, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QFont, QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QFrame, QPushButton, QCheckBox, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout

class ProxyView(QFrame):
	'''
	Proxy View
	'''

	proxy_checkbox_changed = pyqtSignal(int)

	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.layout = QVBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(20)
		self.layout.setAlignment(Qt.AlignTop|Qt.AlignLeft)

		self.use_proxy_checkbox = QCheckBox(self)
		self.use_proxy_checkbox.setObjectName('CheckBoxBig')
		self.use_proxy_checkbox.setText('Use Proxy')

		self.address_label = QLabel(self)
		self.address_label.setObjectName('NormalLabel')
		self.address_label.setText('Address')

		self.address_edit = QLineEdit(self)
		self.address_edit.setObjectName('TextEdit')
		self.address_edit.setFixedSize(165, 23)
		self.address_edit.setEnabled(False)
		self.address_edit.setInputMask('000.000.000.000;_')

		# ip_range = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
		# ip_regexp = QRegExp("((1{0,1}[0-9]{0,2}|2[0-4]{1,1}[0-9]{1,1}|25[0-5]{1,1}).){3,3}(1{0,1}[0-9]{0,2}|2[0-4]{1,1}[0-9]{1,1}|25[0-5]{1,1})")
		# ip_validator = QRegExpValidator(ip_regexp, self.address_edit)
		# self.address_edit.setValidator(ip_validator)

		self.port_label = QLabel(self)
		self.port_label.setObjectName('NormalLabel')
		self.port_label.setText('Port')

		self.port_edit = QLineEdit(self)
		self.port_edit.setObjectName('TextEdit')
		self.port_edit.setValidator(QIntValidator(0, 65536, self.port_edit))
		self.port_edit.setFixedSize(74, 23)
		self.port_edit.setEnabled(False)

		self.edit_layout = QGridLayout()
		self.edit_layout.setContentsMargins(0, 0, 0, 0)
		self.edit_layout.setSpacing(10)
		self.edit_layout.addWidget(self.address_label, 0, 0, Qt.AlignLeft)
		self.edit_layout.addWidget(self.address_edit, 1, 0, Qt.AlignLeft)
		self.edit_layout.addWidget(self.port_label, 0, 1, Qt.AlignLeft)
		self.edit_layout.addWidget(self.port_edit, 1, 1, Qt.AlignLeft)
		self.edit_layout.setColumnStretch(0, 1)
		self.edit_layout.setColumnStretch(1, 1)

		self.layout.addWidget(self.use_proxy_checkbox)
		self.layout.addLayout(self.edit_layout)

		self.use_proxy_checkbox.stateChanged.connect(self.proxy_checkbox_changed)
		self.use_proxy_checkbox.stateChanged.connect(self.on_proxy_checkbox_changed)

	def set_msg_text(self, msg):

		self.msg_label.setText(msg)

	def set_address(self, addr):

		if len(addr) != 0:
			self.use_proxy_checkbox.setCheckState(2)
		self.address_edit.setText(addr)

	def address(self):

		if not self.address_edit.isEnabled():
			return ''

		addr = self.address_edit.text()
		if addr == '...':
			return ''
		return addr

	def set_port(self, port):

		port_str = ''
		if isinstance(port, int):
			port_str = str(port)
		elif isinstance(port, str):
			port_str = port
		else:
			raise TypeError

		self.port_edit.setText(port_str)

	def port(self):

		if not self.port_edit.isEnabled():
			return ''

		port_str = self.port_edit.text()
		if len(port_str) == 0:
			return 0
		else:
			return int(port_str)

	def validate(self):

		if self.address() == '...' or self.port() == -1:
			self.set_msg_text('Both fields are required!')
			return -1
		else:
			for part in self.address().split('.'):
				if not (int(part) >= 0 and int(part) <= 255):
					self.set_msg_text('Invalid Address!')
					return 0

			return 1

	@pyqtSlot(int)
	def on_proxy_checkbox_changed(self, state):

		flag = True if state == 2 else False

		self.address_edit.setEnabled(flag)
		self.port_edit.setEnabled(flag)

if __name__ == '__main__':
	
	from PyQt5.QtWidgets import QWidget, QApplication
	import sys
	
	app = QApplication(sys.argv)

	window = QWidget()

	view = ProxyView(window)
	view.setFixedSize(450, 480)
	view.set_port(2345)

	window.show()

	sys.exit(app.exec())