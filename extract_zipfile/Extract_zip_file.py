import zipfile

print('unzip started..')
unzip_files=zipfile.ZipFile('FileZip.zip' , 'r')
unzip_files.extractall('Files')
print('unzip completed...')

