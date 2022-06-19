# -*- coding: utf-8 -*-
import pandas as pd

books = pd.read_csv('test.csv')
book_name = 'test.md'

current_chapter = ''
first_volume_name = '第1章'
current_volume = 1

with open(book_name, 'a') as txt:
    for index in range(0, len(books)):
        title = books['title'][index].replace('\xa0', '').replace(' (第一页)', '').replace(' (第二页)', '').replace(' (第三页)', '')
        content = books['content'][index].replace('\xa0', '').replace('<br>', '\r\n').replace(',', '\r\n')

        if not current_chapter == title:
            current_chapter = title
            if first_volume_name in title:
                txt.write('\r\n\r\n## ' + '第' + str(current_volume) + '卷' + '\r\n')
                current_volume += 1
            txt.write('\r\n### ' + title + '\r\n')
        txt.write(content + '\r\n')
    txt.close()
