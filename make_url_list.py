
import urllib.request
from bs4 import BeautifulSoup
import lxml.html
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
}
data_col = ["date","title", "url"]

#url = 'http://blog.nogizaka46.com/third/2018/02/043335.php' #最新
#url = 'http://blog.nogizaka46.com/third/2017/02/036909.php' #なぜか途切れているやつ
url = 'http://blog.nogizaka46.com/minami.umezawa/2019/10/053026.php' #ume
while True:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("span", class_="entrytitle").text
    yearmoth = soup.find("span", class_="yearmonth").text
    dd1 = soup.find("span", class_="dd1").text
    date = yearmoth.replace('/','-') + '-' + dd1
    s = pd.Series([date, title, url], index=data_col)
    df = pd.DataFrame(columns=data_col)
    df = df.append(s, ignore_index=True)
    df.to_csv('ume_blogList.csv', mode="a", header=False, index=False)
    url = soup.find_all("div", class_="relnavi")[0].a.attrs['href']
    time.sleep(5)

