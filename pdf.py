import pdfkit
import pandas as pd
import time


options = {
    'page-size': 'A4',
    'margin-top': '0.1in',
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
    'encoding': "UTF-8",
    'no-outline': None,
}



df = pd.read_csv('ume_blogList.csv',names=('Date','Title','url'))
fdir = "ume"
for row in df.itertuples():
    filename = fdir + '/' + str(row.Date) + '_' + row.Title + '.pdf'
    # WebページをPDF出力
    print(filename)
    print(row.url)
    print('#################################')
    try:
        pdfkit.from_url(row.url, filename, options=options)
    except Exception as e:
        #Googleのなんかが読み込めないとｴﾗｰで終了するため、passで続行させる
        pass
    time.sleep(5)




