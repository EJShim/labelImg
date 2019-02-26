from PyInstaller.utils.hooks import collect_data_files

hiddenimports = ['new']


itk_datas = collect_data_files('itk', include_py_files=True)

datas = [x for x in itk_datas if '__pycache__' not in x[0]]
print(datas)