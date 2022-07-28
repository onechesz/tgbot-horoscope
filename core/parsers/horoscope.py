import requests

from bs4 import BeautifulSoup


def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        zodiac_signs = dict()
        page = BeautifulSoup(response.text, 'html.parser')

        section = page.find(name='section', attrs={'class': 'IjM3t'})
        articles = section.find_all(name='article')

        for article in articles:
            zodiac_signs[article.find(name='h3').text] = article.find(name='div', attrs={'class': 'BDPZt KUbeq'}).text

        return zodiac_signs


horoscope_daily = get_content(url='https://74.ru/horoscope/daily/')
horoscope_tomorrow = get_content(url='https://74.ru/horoscope/tomorrow/')
horoscope_weekly = get_content(url='https://74.ru/horoscope/weekly/')

horoscope = {
    'На сегодня': horoscope_daily,
    'На завтра': horoscope_tomorrow,
    'На неделю': horoscope_weekly
}
