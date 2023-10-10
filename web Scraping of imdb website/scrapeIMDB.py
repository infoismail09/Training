from bs4 import BeautifulSoup
import requests

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }

    source = requests.get("https://www.imdb.com/chart/top/", headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    # print(soup)

    movies = soup.find('ul')#, class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base").find_all('li')
    # print(len(movies))

    for movie in movies:

        name =movie.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-4dcdad14-9 dZscOy cli-title").h3.text
        print(name)

        rank = movie.find('h3',class_="ipc-title__text").get_text(strip=True).split('.')[0]

        year = movie.find('div', class_="sc-4dcdad14-7 enzKXX cli-title-metadata")#.span.text.strip('()')

        rating = movie.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")#.strong.text

        print(rank,name,year,rating)
        break

except Exception as e:
    print(e)
