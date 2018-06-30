import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

import pyperclip
import re

cv = pyperclip.paste()

nomes = re.findall(r'[a-zA-Z].*', cv, re.MULTILINE)

telefones = re.findall(r'''
\(?\d\d\)? #ddd
\s #separador
\d{4,5} #primeira parte telefone
[\s|\-] #separador do meio
\d{4} #final do telefone
''', cv, re.MULTILINE | re.VERBOSE )

fusao = dict(zip(nomes, telefones))

df = pd.Series(fusao).to_frame()

writer = ExcelWriter('hey-boss.xlsx')

df.to_excel(writer,'boss')
writer.save()
