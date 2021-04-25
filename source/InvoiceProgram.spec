# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['InvoiceProgram.py'],
             pathex=['C:\\Users\\mdmcb\\OneDrive\\Desktop\\Programming\\Python Invoice GUI\\src'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('icon.ico', 'C:\\Users\\mdmcb\\OneDrive\\Desktop\\Programming\\Python Invoice GUI\\src\\icon.ico', 'DATA'),('guide.txt', 'C:\\Users\\mdmcb\\OneDrive\\Desktop\\Programming\\Python Invoice GUI\\src\\guide.txt', 'DATA1'), ('Invoice_Form.docx','C:\\Users\\mdmcb\\OneDrive\\Desktop\\Programming\\Python Invoice GUI\\src\\Invoice_Form.docx', 'DATA2')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Invoice Program',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon = 'C:\\Users\\mdmcb\\OneDrive\\Desktop\\Programming\\Python Invoice GUI\\src\\icon.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Invoice Program')
