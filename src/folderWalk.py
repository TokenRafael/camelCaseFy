import fileCamelCaseFy as fCCy
from os import walk, rename, path

def renameEntity(root, entityPath):
  head, name, ext = fCCy.divideFilePath(entityPath)
  newName = fCCy.camelCaseFyName(name)
  if name != newName:
    rename(path.join(root, head, name + ext), path.join(root, head, newName + ext))
    print(path.join(root, head, name + ext), '->', path.join(root, head, newName + ext))

def folderCamelCaseFy(rootPath):
  for root, folders, _ in walk(rootPath):
    for folder in folders:
      renameEntity(root, folder)
  for root, _, files in walk(rootPath):
    for file in files:
      renameEntity(root, file)
