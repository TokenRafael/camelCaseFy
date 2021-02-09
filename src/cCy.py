#!/usr/bin/python3
from sys import argv

import folderWalk

# Default value for path is calling directory
rootPath = '.'

if len(argv) == 2:
  rootPath = argv[1]
else:
  print("[ERROR]: There are too many or too little arguments beeing passed")
  exit(1)

print('[INFO] : Once the process has started, it will change the files and folders names\nand this proccess cannot be undone.')
response = input('Are you sure you want to continue? (y/yes/N/no): ')
if response in ['y', 'Y', 'yes', 'Yes', 'YES']:
  folderWalk.folderCamelCaseFy(rootPath)
  print(f'[INFO]: Folder {rootPath} entities have been renamed!')
print('Exiting...')