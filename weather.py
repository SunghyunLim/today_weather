import requests
from bs4 import BeautifulSoup
def 예보얻기():
    url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1171068000'
    html = requests.get(url)
    bs_html = BeautifulSoup(html.content, 'html.parser')

    pubdate = bs_html.find('pubdate').text.split('(')

    hour = bs_html.find('hour').text
    day = bs_html.find('day').text
    temperature = bs_html.find('temp').text

    if day == '0': #다음날이면 그냥 찍지 않는다. 날짜 계산이 귀찮다.
        temperature_str =  pubdate[0] + hour + '시 예보 : ' + temperature + '도'
        출력하기(temperature_str, pubdate[0].rstrip())

def 출력하기(temperature_str, date):
    f = open('weather/'+date+'.txt', 'a')
    f.write(temperature_str+'\n')
    f.close()

if __name__ == "__main__":
    예보얻기()

