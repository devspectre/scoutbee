import sys
import os
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QStackedWidget
from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QVBoxLayout
from gui.menubutton import MenuButton
from gui.api_view import APIView
from gui.credentials_view import CredentialsView
from gui.proxy_view import ProxyView
from gui.debug_view import DebugView

left_bar_width = 200

class SBGui(QMainWindow):

	cancel_clicked = pyqtSignal()
	save_clicked = pyqtSignal()

	def __init__(self):
		super(SBGui, self).__init__()

		self.setObjectName('MainWindow')
		self.setWindowTitle('Scoutbees OnPremise')
		self.setWindowFlags(Qt.Window|Qt.WindowTitleHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
		self.setAutoFillBackground(True)
		self.setWindowIcon(QIcon(resource_path('favicon.ico')))
		self.setFixedSize(653, 480)

		self.checkmark_path = resource_path('checkmark.png')

		self.central_widget = QWidget(self)
		self.central_widget.setObjectName('CentralWidget')

		self.main_layout = QHBoxLayout(self.central_widget)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.main_layout.setSpacing(0)
		self.main_layout.setAlignment(Qt.AlignLeft)

		self.navigation_frame = QFrame(self.central_widget)
		self.navigation_frame.setObjectName('Navigation')
		self.navigation_frame.setFixedWidth(left_bar_width)
		self.navigation_frame.setAutoFillBackground(True)

		self.left_layout = QVBoxLayout(self.navigation_frame)
		self.left_layout.setContentsMargins(0, 0, 0, 0)
		self.left_layout.setSpacing(0)

		self.navigation_layout = QVBoxLayout()
		self.navigation_layout.setContentsMargins(0, 0, 0, 0)
		self.navigation_layout.setSpacing(7)
		self.navigation_layout.setAlignment(Qt.AlignTop)

		self.logo_frame = QFrame(self.navigation_frame)
		self.logo_frame.setFixedSize(left_bar_width, 68)
		self.logo_frame.setObjectName('LogoFrame')

		self.logo = QLabel(self.logo_frame)
		self.logo.setFixedSize(123, 25)
		self.logo.setScaledContents(True)
		
		logo_pixmap = QPixmap(resource_path('logo.png'))
		
		self.logo.setPixmap(logo_pixmap)
		self.logo.setGeometry(14, 29, self.logo.width(), self.logo.height())

		self.button_api = MenuButton('API Key', self.navigation_frame)
		self.button_api.setObjectName('API')
		self.button_api.setFixedSize(left_bar_width, 26)
		self.button_api.set_selected(False)

		self.button_credentials = MenuButton('Enrichment Credentials', self.navigation_frame)
		self.button_credentials.setObjectName('Credentials')
		self.button_credentials.setFixedSize(left_bar_width, 26)

		self.button_proxy = MenuButton('Proxy', self.navigation_frame)
		self.button_proxy.setObjectName('Proxy')
		self.button_proxy.setFixedSize(left_bar_width, 26)

		self.button_debug = MenuButton('Debug', self.navigation_frame)
		self.button_debug.setObjectName('Debug')
		self.button_debug.setFixedSize(left_bar_width, 26)

		self.button_group = []
		self.button_group.append(self.button_api)
		self.button_group.append(self.button_credentials)
		self.button_group.append(self.button_proxy)
		self.button_group.append(self.button_debug)

		self.left_layout.addWidget(self.logo_frame)
		for button in self.button_group:
			self.navigation_layout.addWidget(button)
			button.clicked.connect(self.on_page_change_requested)

		self.left_layout.addLayout(self.navigation_layout)

		self.msg_label = QLabel(self)
		self.msg_label.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
		self.msg_label.setObjectName('WarningLabel')

		self.cancel_button = QPushButton(self)
		self.cancel_button.setText('Cancel')
		self.cancel_button.setObjectName('CancelButton')
		self.cancel_button.setFixedSize(52, 21)

		self.save_button = QPushButton(self)
		self.save_button.setText('Save')
		self.save_button.setObjectName('SaveButton')
		self.save_button.setFixedSize(52, 21)

		self.top_layout = QHBoxLayout()
		self.top_layout.setContentsMargins(0, 0, 0, 0)
		self.top_layout.setAlignment(Qt.AlignRight)
		self.top_layout.setSpacing(8)

		self.top_layout.addWidget(self.msg_label, 10)
		self.top_layout.addWidget(self.cancel_button)
		self.top_layout.addWidget(self.save_button)

		self.content_layout = QVBoxLayout()
		self.content_layout.setContentsMargins(38, 26, 38, 26)
		self.content_layout.setSpacing(10)

		self.content = QStackedWidget(self.central_widget)
		self.content.setObjectName('Content')
		self.content.setAutoFillBackground(True)

		self.content_layout.addLayout(self.top_layout)
		self.content_layout.addWidget(self.content)

		self.api_view = APIView(self.content)

		self.credentials_view = CredentialsView(self.content)

		self.proxy_view = ProxyView(self.content)

		self.debug_view = DebugView(self.content)

		self.content.addWidget(self.api_view)
		self.content.addWidget(self.credentials_view)
		self.content.addWidget(self.proxy_view)
		self.content.addWidget(self.debug_view)

		self.main_layout.addWidget(self.navigation_frame)
		self.main_layout.addLayout(self.content_layout)

		self.setCentralWidget(self.central_widget)
		self.set_custom_style()
		self.set_current_index_menu(0)

		self.cancel_button.clicked.connect(self.cancel_clicked)
		self.save_button.clicked.connect(self.save_clicked)

	def set_custom_style(self):
		""" set global stylesheet """

		style = """#MainWindow{ background-color: white}
			#Navigation{background-color: rgba(196, 196, 196, 0.3)}

			#WarningLabel{color: #C71818; font-family: 'Open Sans'; font-size: 12px;}

			#CancelButton{font-family: 'Open Sans'; font-size: 12px; color: #393A4E; border: 0px solid white;}
			#CancelButton:hover{color: white; background-color: #797A8E; border: 1px solid white; border-radius: 4px}
			#CancelButton:pressed{color: white; background-color: #393A4E; border: 1px solid white; border-radius: 4px}

			#SaveButton{font-family: 'Open Sans'; font-size: 12px; color: white; background-color: #0276D8; 
			border: 1px solid #CCCCCC; border-radius: 4px}
			#SaveButton:hover{color: white; background-color: #32A6F8; border: 1px solid #CCCCCC; border-radius: 4px}
			#SaveButton:pressed{color: white; background-color: #0276FF; border: 1px solid white; border-radius: 4px}

			#Content{background-color: white}

			#ParagraphTitle{color: #858796; font: 750 14px 'Open Sans'}

			#NormalLabel{color: #858796; font: 500 12px 'Open Sans'}

			#CheckBox{ color: #999999}
			#CheckBox:indicator{ width: 12px; height: 12px; color: white; background: white; border: 1px solid rgba(0, 0, 0, 0.5); border-radius: 2px }
			#CheckBox:indicator:checked{ color: white; background: #0683F9; image: url(CHECKMARK_PATH)}

			#CheckBoxBig{ color: #999999; width: 15px; height: 15px; font: 500 14px 'Open Sans' }
			#CheckBoxBig:indicator{ width: 15px; height: 15px; color: white; background: white; border: 1px solid rgba(0, 0, 0, 0.5); border-radius: 2px }
			#CheckBoxBig:indicator:checked{ color: white; background: #0683F9; image: url(CHECKMARK_PATH)}

			#TextEdit{background-color: white; border: 1px solid #D1D3E2; border-radius: 4px; padding: 3px}
			#TextEdit:disabled{background-color: #DBD8D8; color: #999999;}

			#ValidateButton{background-color: rgba(230, 230, 230, 0.6); color: #28313B; border: 1px solid #CCCCCC;
				border-radius: 4px; font: 500 12px 'Open Sans'}
			#ValidateButton:hover{background-color: #CCCCCC}
			#ValidateButton:pressed{background-color: #9A9A9A}
			#ValidateButton:disabled{color: #DBD8D8}
			"""

		self.checkmark_path = self.checkmark_path.replace("\\", "/")
		self.setStyleSheet(style.replace("CHECKMARK_PATH", self.checkmark_path))

	def resizeEvent(self, event):

		super().resizeEvent(event)
		self.navigation_frame.setGeometry(0, 0, self.navigation_frame.width(), self.height())
		self.content.setGeometry(self.navigation_frame.width(), 0, self.width() - self.navigation_frame.width(), self.height())

	def set_msg(self, msg):

		self.msg_label.setText(msg)

	@pyqtSlot(str)
	def on_page_change_requested(self, page_name):

		index_ = 0
		for button in self.button_group:
			if button.objectName() == page_name:
				button.set_selected(True)
				self.content.setCurrentIndex(index_)
			else:
				button.set_selected(False)

			index_ = index_ + 1

	@pyqtSlot(int)
	def set_current_index_menu(self, index):

		index_ = 0
		for button in self.button_group:
			if index_ == index:
				button.set_selected(True)
			else:
				button.set_selected(False)

			index_ = index_ + 1

	def set_api_key(self, key):

		self.api_view.set_api_key(key)

	def api_key(self):

		return self.api_view.api_key()

	def set_wmi_username(self, name):

		self.credentials_view.set_remote_wmi_username(name)

	def wmi_username(self):

		return self.credentials_view.remote_wmi_username()

	def set_wmi_password(self, passwd):

		self.credentials_view.set_remote_wmi_password(passwd)

	def wmi_password(self):

		return self.credentials_view.remote_wmi_password()

	def set_xendesktop_username(self, name):

		self.credentials_view.set_xendesktop_username(name)

	def xendesktop_username(self):

		return self.credentials_view.xendesktop_username()

	def set_xendesktop_password(self, passwd):

		self.credentials_view.set_xendesktop_password(passwd)

	def xendesktop_password(self):

		return self.credentials_view.xendesktop_password()

	def set_proxy_address(self, addr):

		self.proxy_view.set_address(addr)

	def proxy_address(self):

		return self.proxy_view.address()

	def set_proxy_port(self, port):

		self.proxy_view.set_port(port)

	def proxy_port(self):

		return self.proxy_view.port()

	def enable_event_log(self, flag):

		self.debug_view.enable_event_log(flag)

	def event_log(self):

		return self.debug_view.event_log()

	def enable_debug_mode(self, flag):

		self.debug_view.enable_debug_mode(flag)

	def debug_mode(self):

		return self.debug_view.debug_mode()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
	
	app = QApplication(sys.argv)

	window = SBGui()
	window.show()

	sys.exit(app.exec())