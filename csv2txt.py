# -*- coding: utf-8 -*-
import pandas as pd

books = pd.read_csv('book/test.csv')
folder = '我的老千生涯'
for index in range(0, len(books)):
    title = books['title'][index].replace('\xa0', '')
    content = books['content'][index].replace('<br>', '\r\n').replace('\u3000', ' ').replace('\xa0', '')
    with open(folder + '/' + str(index) + title + '.txt.', 'w+') as txt:
        txt.write(title + '\r\n')
        txt.write(content)
        txt.close()
