from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QCheckBox, QFrame, QVBoxLayout

class DebugView(QFrame):
	'''
	Proxy View
	'''

	event_log_checkbox_changed = pyqtSignal(int)
	debug_mode_checkbox_changed = pyqtSignal(int)

	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.layout = QVBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(20)
		self.layout.setAlignment(Qt.AlignTop|Qt.AlignLeft)

		self.event_log_checkbox = QCheckBox(self)
		self.event_log_checkbox.setObjectName('CheckBox')
		self.event_log_checkbox.setText('Event Log')

		self.debug_mode_checkbox = QCheckBox(self)
		self.debug_mode_checkbox.setObjectName('CheckBox')
		self.debug_mode_checkbox.setText('Debug Mode')

		self.layout.addWidget(self.event_log_checkbox)
		self.layout.addWidget(self.debug_mode_checkbox)

	def enable_event_log(self, flag):

		self.event_log_checkbox.setChecked(flag)

	def event_log(self):

		return self.event_log_checkbox.isChecked()

	def enable_debug_mode(self, flag):

		self.debug_mode_checkbox.setChecked(flag)

	def debug_mode(self):

		return self.debug_mode_checkbox.isChecked()

if __name__ == '__main__':
	
	from PyQt5.QtWidgets import QWidget, QApplication
	import sys
	
	app = QApplication(sys.argv)

	window = QWidget()

	view = DebugView(window)
	view.setFixedSize(450, 480)

	window.show()

	sys.exit(app.exec())