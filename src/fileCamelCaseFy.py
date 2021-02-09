from os import path
import re

def divideFilePath(filepath):
  head, base = path.split(filepath)
  ext = ''
  while '.' in base:
    base, moreExt = path.splitext(base)
    ext = moreExt + ext
  return head, base, ext

def camelCaseFyName(str):
  noDashStr = re.sub(r'[_\-]', ' ', str)
  pascalStr = re.sub(r' ([a-zA-Z])', lambda x: x.group().upper(), noDashStr)
  pascalStr = ''.join(x for x in pascalStr if not x.isspace())
  # pascalStr = ''.join(x for x in noDashStr.title() if not x.isspace())
  camelStr = pascalStr[0].lower() + pascalStr[1:]
  return camelStr