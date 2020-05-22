import ssl
import json
import sqlite3
import requests
import subprocess
import os
import sys
import ctypes
import win32serviceutil

from Crypto.Cipher import AES
from binascii import a2b_hex
from base64 import b64encode, b64decode
from time import sleep, time
from string import hexdigits
from sbgui import SBGui
from PyQt5.QtWidgets import QMessageBox

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not(is_admin()):
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv[1:] if sys.argv[0] == sys.executable else sys.argv), None, 1)
    sys.exit()

try:
    os.chdir(os.path.dirname(sys.executable) if getattr(sys, 'frozen', False)  else sys.path[0])
except:
    print('failed to chdir')

KEY_LEN = 256 / 8
SERVICE_URL = 'https://dev.scoutbees.io'
DB_FILE = 'ls.db'

old_prem_id = None
old_data = None
prem_id = None
api_key = None
wmi_user = None
wmi_pass = None
proxy_host = None
proxy_port = None
proxy_user = None
proxy_pass = None
old_options = {}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

app = None
conn = None
cursor = None

def checkKey(key):
    if proxy_host is not None and proxy_host != '':
        proxy = "%s:%s" % (proxy_host, proxy_port)
        proxies = {
            "https": 'https://' + proxy,
            "http": 'http://' + proxy
        }
    else:
        proxies = None
    print(proxies)
    resp = requests.post(SERVICE_URL + '/premises/install', json=dict(key=key), proxies=proxies, headers=headers)
    data = resp.json()
    # print(resp.status_code)
    # print(data)
    if resp.status_code == 200 and 'id' in data and data['id'] > 0:
        return int(data['id'])
    return False

# install
def install():
    global api_key, prem_id, wmi_user, wmi_pass, proxy_host, proxy_port, proxy_user, proxy_pass

    try:
        api_key = gui.api_key()
        wmi_user = gui.wmi_username()
        wmi_pass = gui.wmi_password()
        proxy_host = gui.proxy_address()
        proxy_port = gui.proxy_port()
        proxy_user = ''#app.getEntry("Proxy Username")
        proxy_pass = ''#app.getEntry("Proxy Password")
        
        options = old_options
        options['eventLog'] ='Y' if gui.event_log() else ''
        options['debug'] ='Y' if gui.debug_mode() else ''

        if len(api_key) != KEY_LEN * 2 or not all(c in hexdigits for c in api_key):
            gui.set_msg('Invalid key')
            return False

        prem_id = checkKey(api_key)

        if not(prem_id > 0):
            gui.set_msg('API key not found')
            return False

        #if prem_id != old_prem_id:
        #print("removing old jobs")
        #cursor.execute('DROP TABLE IF EXISTS jobs')
        cursor.execute(('CREATE TABLE IF NOT EXISTS jobs ('
            'id INTEGER PRIMARY KEY, userid INTEGER, address TEXT, job_user TEXT,'
            'job_pass TEXT, job_resource TEXT, prem_id INTEGER, last_run INTEGER,'
            'job_schedule TEXT, platform TEXT, job_type TEXT, run_every INTEGER,'
            'domain TEXT, job_creation_time INTEGER, job_name TEXT'
            ')'))

        cursor.execute('DROP TABLE IF EXISTS settings')
        cursor.execute('CREATE TABLE settings (prem_id INTEGER PRIMARY KEY, api_key TEXT, wmi_user TEXT, wmi_pass TEXT, proxy_host TEXT, proxy_port INTEGER, proxy_user TEXT, proxy_pass TEXT)')
        cursor.execute("INSERT INTO settings (prem_id, api_key, wmi_user, wmi_pass, proxy_host, proxy_port, proxy_user, proxy_pass) VALUES (?,?,?,?,?,?,?,?)", (prem_id, api_key, wmi_user, encrypt(wmi_pass), proxy_host, proxy_port, proxy_user, encrypt(proxy_pass),))

        cursor.execute('DROP TABLE IF EXISTS options')
        cursor.execute('CREATE TABLE options (prem_id INTEGER, option_key TEXT, option_value TEXT, PRIMARY KEY(prem_id, option_key))')
        for key, value in options.items():
            cursor.execute("INSERT INTO options (prem_id, option_key, option_value) VALUES (?,?,?)", (prem_id, key, value,))

        conn.commit()

        return True

    except Exception as e:
        # app.errorBox("Error", "Something went wrong.. please try again")
        gui.set_msg('Cannot connect to control plane')

        print(e)

    return False

def encrypt(msg):
    secret = api_key
    if len(secret) == KEY_LEN * 2:
        secret = a2b_hex(secret)
    aesCipher = AES.new(secret, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(bytes(msg, 'utf8'))
    return str(b64encode(ciphertext), 'utf8') + ',' + str(b64encode(aesCipher.nonce), 'utf8') + ',' + str(b64encode(authTag), 'utf8')

def decrypt(encryptedMsg):
    secret = api_key
    if len(secret) == KEY_LEN * 2:
        secret = a2b_hex(secret)
    ciphertext, nonce, authTag = [b64decode(e) for e in encryptedMsg.split(',')]
    aesCipher = AES.new(secret, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return str(plaintext, 'utf8')

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    
def set_data():

    if old_data and 'api_key' in old_data:
        gui.set_api_key(old_data['api_key'])
    if old_data and 'wmi_user' in old_data:
        gui.set_wmi_username(old_data['wmi_user'])
    if old_data and 'wmi_pass' in old_data:
        gui.set_wmi_password(decrypt(old_data['wmi_pass']))
    if old_data and 'proxy_host' in old_data:
        gui.set_proxy_address(old_data['proxy_host'])
    if old_data and 'proxy_port' in old_data:
        gui.set_proxy_port(old_data['proxy_port'])
    if old_options and 'eventLog' in old_options:
        gui.enable_event_log(old_options['eventLog'] == 'Y')
    if old_options and 'debug' in old_options:
        gui.enable_debug_mode(old_options['debug'] == 'Y')

def save():
    
    if len(gui.api_key()) == 0:
        gui.set_msg('You must enter API key')
        return

    if install():
        try: 
            win32serviceutil.QueryServiceStatus('ScoutbeesHive')
        except:
            try:
                subprocess.run(['sb-hive.exe', '--startup=auto', 'install'])
                subprocess.run(['sb-hive.exe', 'start'])
            except Exception as e:
                QMessageBox.critical(gui, "Error", "Failed to run sb-hive.exe. Perhaps file not exists.")
                return
        else:
            try:
                subprocess.run(['sb-hive.exe', 'restart'])
            except Exception as e:
                QMessageBox.critical(gui, "Error", "Failed to run sb-hive.exe. Perhaps file not exists.")
                return

        QMessageBox.information(gui, "Success", "Settings saved successfully!")
        sys.exit(0)

if __name__ == "__main__":

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM settings LIMIT 1")
        data = cursor.fetchone()

        if not data or 'prem_id' not in data or not(data['prem_id'] > 0) or len( data['api_key']) != KEY_LEN * 2:
            raise Exception("missing api key")

        #if checkKey(data['api_key']) != data['prem_id']:
        #    raise Exception()

        old_data = data
        old_prem_id = int(data['prem_id'])
        api_key = data['api_key']

    except:
        print("no old data")

    if old_prem_id is not None and old_prem_id > 0:
        try:
            cursor.execute("SELECT * FROM options WHERE prem_id=?", (old_prem_id,))
            options = cursor.fetchall()

            if not options or not(len(options) > 0):
                raise Exception("no options")

            for o in options:
                old_options[o['option_key']] = o['option_value']

        except:
            print("no old options")

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    global gui
    gui = SBGui()
    gui.show()
    set_data()
    gui.cancel_clicked.connect(sys.exit)
    gui.save_clicked.connect(save)

    sys.exit(app.exec())
    #install()
