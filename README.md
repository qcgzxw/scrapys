# 个人爬虫库
自用爬虫库
## 使用方式
* 安装requirements.txt
```python
pip install requirements.txt
```

* 使用scrapy命令

[https://docs.scrapy.org/en/latest/intro/tutorial.html](https://docs.scrapy.org/en/latest/intro/tutorial.html)
## scrapy project name
### biqudao
笔趣岛（已失效）
```python
scrapy crawl biqudao -o test.csv
```

爬取对应书籍
### ipipnet 
ipip.net

爬取IP段（例如Netflix Google Youtube）

```python
# 爬https://whois.ipip.net/search/GOOGLE%20LLC
scrapy crawl ipip.net -o test.json -a keyword=GOOGLE%20LLC
```