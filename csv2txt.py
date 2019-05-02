# -*- coding: utf-8 -*-
import pandas as pd

books = pd.read_csv('book/test.csv')
folder = '我的老千生涯'
for index in range(0, len(books)):
    title = books['title'][index] + '.txt.'
    content = books['content'][index].replace('<br>', '\r\n').replace('\u3000', ' ')
    with open(folder + '/' + title, 'w+') as txt:
        txt.write(books['title'][index] + '\r\n')
        txt.write(content)
        txt.close()
