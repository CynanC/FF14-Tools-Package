# -*- mode: python -*-

block_cipher = None


a = Analysis(['boxing.py'],
             pathex=['C:\\Users\\arris\\Desktop\\ff14Tools'],
             binaries=[],
             datas=[('C:\\Users\\arris\\Desktop\\ff14Tools\\lib\\start.mp3',''),('C:\\Users\\arris\\Desktop\\ff14Tools\\lib\\end.mp3','')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='boxing',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='fav.ico')
