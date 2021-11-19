# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['sb-config.py'],
             pathex=[''],
             binaries=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('logo.png', './images/logo.png', 'DATA'), ('checkmark.png', './images/checkmark.png', 'DATA'), ('favicon.ico', 'favicon.ico', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

import sys

if sys.platform == 'win32' or sys.platform == 'win64' or sys.platform == 'linux':
  exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Scoutbees',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='favicon.ico' )
