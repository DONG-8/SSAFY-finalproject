import requests
import csv
import ssl
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


code = 210000

def start(code):
    global total
    while code > 180000:
        url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=" + str(code)
        response = requests.get(url)
        try:
            crowling(response)

        except Exception as ex:
            pass
        code -= 1
    print('완료')


def crowling(response):
    global total

    data = []

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a').contents[0]
        data.append(title)

        if soup.select_one('#actualPointPersentBasic > div > span > span'):
            vote = soup.select_one('#actualPointPersentBasic > div > span > span').contents[0]
            data.append(vote)
        else:
            return


        genre_all = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)').find_all()
        genre = []
        for i in range(len(genre_all)):
            genre.extend(genre_all[i].contents)
        data.append(genre)

        if genre == ['멜로/로맨스']:
            return
        elif genre == ['에로']:
            return
        elif genre == ['에로', '멜로/로맨스']:
            return
        elif genre == ['멜로/로멘스', '에로']:
            return

        country = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a').contents[0]
        data.append(country)

        time = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)').contents
        data.append(time[0].strip())

        if soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)'):
            year = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4) > a:nth-child(1)').contents[0].strip()
            date = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4) > a:nth-child(2)').contents[0].strip()
            open_date = year+date
        else:
            open_date = ['미상']
        data.append(open_date)

        actor_all = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p').find_all()
        actor = []
        for i in range(len(actor_all)):
            actor.extend(actor_all[i].contents)
        data.append(actor)

        if soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p > a'):
            grade = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p > a').contents[0]
        else:
            grade = ['전체 관람가']
        data.append(grade)

        poster_path = soup.select_one('#content > div.article > div.mv_info_area > div.poster > a > img').get("src")
        data.append(poster_path)
        if 'ssl.pstatic.net' in poster_path[0]:
            return

        if soup.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p'):
            content = soup.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p').contents
        else:
            content = []
        # print(content)
        data.append(content)
        total.append(data)

        f = open('./data/movie.csv', 'w', encoding='utf-8', newline='')
        csvfile = csv.writer(f)
        for row in total:
            csvfile.writerow(row)
        f.close()


    else :
        # print(response.status_code)
        pass

total = []
start(code)
print(total)