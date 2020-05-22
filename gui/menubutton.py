import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import pyqtSignal

class MenuButton(QLabel):
	'''
	Clickable buton with colored text
	'''
	clicked = pyqtSignal(str)

	def __init__(self, text = "", parent = None):
		QLabel.__init__(self, text, parent)

		self.pressed = False
		self.is_selected = False
		self.style_normal = """#OBJECT_NAME{color: rgba(51, 51, 51, 0.7); font-family: 'Roboto'; font-size: 14px; padding-left: 14px;}
							#OBJECT_NAME:hover{background-color: rgba(196, 196, 196, 0.6); font-weight: bold}"""

		self.style_selected = """#OBJECT_NAME{color: rgba(51, 51, 51, 0.7); font-family: 'Roboto'; font-size: 14px; font-weight: bold; padding-left: 14px;
							background-color: rgba(49, 111, 204, 0.5)}
							#OBJECT_NAME:hover{background-color: rgba(49, 111, 204, 0.3)}"""
		self.setObjectName('MenuButton')
		self.update_stylesheet()

	def set_selected(self, selected):

		if selected != self.is_selected:
			self.is_selected = selected
			self.update_stylesheet()

	def set_style_normal(self, style):

		self.style_normal = style
		self.update_stylesheet()

	def set_style_selected(self, style):

		self.style_selected = style
		self.update_stylesheet()

	def update_stylesheet(self):

		style = self.style_normal
		if self.is_selected:
			style = self.style_selected

		self.setStyleSheet(style.replace('OBJECT_NAME', self.objectName()))

	def setObjectName(self, name):

		QLabel.setObjectName(self, name)
		self.update_stylesheet()

	def mousePressEvent(self, event):
		QLabel.mousePressEvent(self, event)
		self.pressed = True

	def mouseReleaseEvent(self, event):
		QLabel.mouseReleaseEvent(self, event)
		if self.pressed:
			self.clicked.emit(self.objectName())

if __name__ == '__main__':

	from PyQt5.QtWidgets import QWidget, QApplication
	
	app = QApplication(sys.argv)

	window = QWidget()

	button = MenuButton('API Key', window)
	button.setFixedSize(240, 40)

	window.show()

	sys.exit(app.exec())