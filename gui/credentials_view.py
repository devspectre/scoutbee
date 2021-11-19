from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel, QLineEdit, QCheckBox, QHBoxLayout, QVBoxLayout

class CredentialsView(QFrame):
	'''
	Enrichment Credentials View
	'''

	remote_wmi_validate_clicked = pyqtSignal()
	xendesktop_validate_clicked = pyqtSignal()
	remote_wmi_checkbox_changed = pyqtSignal(int)
	xendesktop_checkbox_changed = pyqtSignal(int)

	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.remote_wmi_title = QLabel(self)
		self.remote_wmi_title.setObjectName('ParagraphTitle')
		self.remote_wmi_title.setText('Remote WMI')

		self.remote_wmi_checkbox = QCheckBox(self)
		self.remote_wmi_checkbox.setObjectName('CheckBox')
		self.remote_wmi_checkbox.setText('Enable')

		self.remote_wmi_title_layout = QHBoxLayout()
		self.remote_wmi_title_layout.setContentsMargins(0, 10, 0, 10)
		self.remote_wmi_title_layout.setSpacing(5)

		self.remote_wmi_title_layout.addWidget(self.remote_wmi_title, 2)
		self.remote_wmi_title_layout.addWidget(self.remote_wmi_checkbox, 1)
		self.remote_wmi_title_layout.addWidget(QFrame(), 3)

		self.remote_wmi_username_label = QLabel(self)
		self.remote_wmi_username_label.setObjectName('NormalLabel')
		self.remote_wmi_username_label.setText('Username')

		self.remote_wmi_username_edit = QLineEdit(self)
		self.remote_wmi_username_edit.setObjectName('TextEdit')
		self.remote_wmi_username_edit.setPlaceholderText('Domain\\Username')
		self.remote_wmi_username_edit.setFixedSize(176, 21)
		self.remote_wmi_username_edit.setEnabled(False)

		self.remote_wmi_password_label = QLabel(self)
		self.remote_wmi_password_label.setObjectName('NormalLabel')
		self.remote_wmi_password_label.setText('Password')

		self.remote_wmi_password_edit = QLineEdit(self)
		self.remote_wmi_password_edit.setObjectName('TextEdit')
		self.remote_wmi_password_edit.setPlaceholderText('Password')
		self.remote_wmi_password_edit.setEchoMode(QLineEdit.Password)
		self.remote_wmi_password_edit.setFixedSize(176, 21)
		self.remote_wmi_password_edit.setEnabled(False)

		self.remote_wmi_validate_button = QPushButton(self)
		self.remote_wmi_validate_button.setObjectName('ValidateButton')
		self.remote_wmi_validate_button.setFixedSize(65, 21)
		self.remote_wmi_validate_button.setText('Validate')
		self.remote_wmi_validate_button.setEnabled(False)

		self.remote_wmi_bottom_layout = QHBoxLayout()
		self.remote_wmi_bottom_layout.setContentsMargins(0, 0, 0, 0)
		self.remote_wmi_bottom_layout.setSpacing(23)
		self.remote_wmi_bottom_layout.addWidget(self.remote_wmi_password_edit, 3)
		self.remote_wmi_bottom_layout.addWidget(self.remote_wmi_validate_button, 1)
		self.remote_wmi_bottom_layout.addWidget(QFrame(), 2)

		self.remote_wmi_layout = QVBoxLayout()
		self.remote_wmi_layout.setContentsMargins(0, 0, 0, 20)
		self.remote_wmi_layout.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
		self.remote_wmi_layout.setSpacing(5)
		self.remote_wmi_layout.addLayout(self.remote_wmi_title_layout)
		self.remote_wmi_layout.addWidget(self.remote_wmi_username_label)
		self.remote_wmi_layout.addWidget(self.remote_wmi_username_edit)
		self.remote_wmi_layout.addWidget(self.remote_wmi_password_label)
		self.remote_wmi_layout.addLayout(self.remote_wmi_bottom_layout)

		self.xendesktop_title = QLabel(self)
		self.xendesktop_title.setObjectName('ParagraphTitle')
		self.xendesktop_title.setText('XenDesktop')

		self.xendesktop_checkbox = QCheckBox(self)
		self.xendesktop_checkbox.setObjectName('CheckBox')
		self.xendesktop_checkbox.setText('Enable')

		self.xendesktop_same_as_wmi_checkbox = QCheckBox(self)
		self.xendesktop_same_as_wmi_checkbox.setObjectName('CheckBox')
		self.xendesktop_same_as_wmi_checkbox.setText('Same as WMI')

		self.xendesktop_title_layout = QHBoxLayout()
		self.xendesktop_title_layout.setContentsMargins(0, 10, 0, 10)
		self.xendesktop_title_layout.setSpacing(5)
		self.xendesktop_title_layout.addWidget(self.xendesktop_title, 4)
		self.xendesktop_title_layout.addWidget(self.xendesktop_checkbox, 2)
		self.xendesktop_title_layout.addWidget(self.xendesktop_same_as_wmi_checkbox, 3)
		self.xendesktop_title_layout.addWidget(QFrame(), 3)

		self.xendesktop_username_label = QLabel(self)
		self.xendesktop_username_label.setObjectName('NormalLabel')
		self.xendesktop_username_label.setText('Username')

		self.xendesktop_username_edit = QLineEdit(self)
		self.xendesktop_username_edit.setObjectName('TextEdit')
		self.xendesktop_username_edit.setPlaceholderText('Domain\\Username')
		self.xendesktop_username_edit.setFixedSize(176, 21)
		self.xendesktop_username_edit.setEnabled(False)

		self.xendesktop_password_label = QLabel(self)
		self.xendesktop_password_label.setObjectName('NormalLabel')
		self.xendesktop_password_label.setText('Password')

		self.xendesktop_password_edit = QLineEdit(self)
		self.xendesktop_password_edit.setObjectName('TextEdit')
		self.xendesktop_password_edit.setPlaceholderText('Password')
		self.xendesktop_password_edit.setEchoMode(QLineEdit.Password)
		self.xendesktop_password_edit.setFixedSize(176, 21)
		self.xendesktop_password_edit.setEnabled(False)

		self.xendesktop_validate_button = QPushButton(self)
		self.xendesktop_validate_button.setObjectName('ValidateButton')
		self.xendesktop_validate_button.setFixedSize(65, 21)
		self.xendesktop_validate_button.setText('Validate')
		self.xendesktop_validate_button.setEnabled(False)

		self.xendesktop_bottom_layout = QHBoxLayout()
		self.xendesktop_bottom_layout.setContentsMargins(0, 0, 0, 0)
		self.xendesktop_bottom_layout.setSpacing(23)
		self.xendesktop_bottom_layout.addWidget(self.xendesktop_password_edit, 3)
		self.xendesktop_bottom_layout.addWidget(self.xendesktop_validate_button, 1)
		self.xendesktop_bottom_layout.addWidget(QFrame(), 2)

		self.xendesktop_layout = QVBoxLayout()
		self.xendesktop_layout.setContentsMargins(0, 0, 0, 0)
		self.xendesktop_layout.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
		self.xendesktop_layout.setSpacing(5)
		self.xendesktop_layout.addLayout(self.xendesktop_title_layout)
		self.xendesktop_layout.addWidget(self.xendesktop_username_label)
		self.xendesktop_layout.addWidget(self.xendesktop_username_edit)
		self.xendesktop_layout.addWidget(self.xendesktop_password_label)
		self.xendesktop_layout.addLayout(self.xendesktop_bottom_layout)

		self.layout = QVBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(10)
		self.layout.setAlignment(Qt.AlignTop|Qt.AlignLeft)
		self.layout.addLayout(self.remote_wmi_layout)
		self.layout.addLayout(self.xendesktop_layout)

		self.remote_wmi_checkbox.stateChanged.connect(self.remote_wmi_checkbox_changed)
		self.remote_wmi_checkbox.stateChanged.connect(self.enable_remote_wmi)
		self.xendesktop_checkbox.stateChanged.connect(self.xendesktop_checkbox_changed)
		self.xendesktop_checkbox.stateChanged.connect(self.enable_xendesktop)
		self.xendesktop_same_as_wmi_checkbox.stateChanged.connect(self.set_same_as_wmi)
		self.remote_wmi_validate_button.clicked.connect(self.remote_wmi_validate_clicked)
		self.xendesktop_validate_button.clicked.connect(self.xendesktop_validate_clicked)

	def set_remote_wmi_username(self, name):

		if len(name) != 0:
			self.remote_wmi_checkbox.setCheckState(2)
		self.remote_wmi_username_edit.setText(name)

	def remote_wmi_username(self):

		if not self.remote_wmi_username_edit.isEnabled():
			return ''
		return self.remote_wmi_username_edit.text()

	def set_remote_wmi_password(self, passwd):

		if len(passwd) != 0:
			self.remote_wmi_checkbox.setCheckState(2)
		self.remote_wmi_password_edit.setText(passwd)

	def remote_wmi_password(self):

		if not self.remote_wmi_password_edit.isEnabled():
			return ''
		return self.remote_wmi_password_edit.text()

	def set_xendesktop_username(self, name):

		if len(name) != 0:
			self.xendesktop_checkbox.setCheckState(2)
		self.xendesktop_username_edit.setText(name)

	def xendesktop_username(self):

		if not self.xendesktop_username_edit.isEnabled():
			return ''
		return self.xendesktop_username_edit.text()

	def set_xendesktop_password(self, passwd):

		if len(passwd) != 0:
			self.xendesktop_checkbox.setCheckState(2)
		self.xendesktop_password_edit.setText(passwd)

	def xendesktop_password(self):

		if not self.xendesktop_password_edit.isEnabled():
			return ''
		return self.xendesktop_password_edit.text()

	def set_msg_text(self, msg):

		self.label_msg.setText(msg)

	@pyqtSlot(int)
	def enable_remote_wmi(self, state):

		flag = True if state == 2 else False

		self.remote_wmi_username_edit.setEnabled(flag)
		self.remote_wmi_password_edit.setEnabled(flag)
		# self.remote_wmi_validate_button.setEnabled(flag)

	@pyqtSlot(int)
	def enable_xendesktop(self, state):

		if self.xendesktop_same_as_wmi_checkbox.checkState() == 2:
			return

		flag = True if state == 2 else False

		self.xendesktop_username_edit.setEnabled(flag)
		self.xendesktop_password_edit.setEnabled(flag)
		# self.xendesktop_validate_button.setEnabled(flag)

	@pyqtSlot(int)
	def set_same_as_wmi(self, state):

		flag = True if state != 2 and self.xendesktop_checkbox.checkState() == 2 else False

		self.xendesktop_username_edit.setEnabled(flag)
		self.xendesktop_password_edit.setEnabled(flag)
		self.xendesktop_validate_button.setEnabled(flag)

if __name__ == '__main__':
	
	from PyQt5.QtWidgets import QWidget, QApplication
	import sys
	
	app = QApplication(sys.argv)

	window = QWidget()

	view = CredentialsView(window)
	view.setFixedSize(450, 480)

	window.show()

	sys.exit(app.exec())