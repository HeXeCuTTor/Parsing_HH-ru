import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
import json
from pprint import pprint 

HOST = 'https://spb.hh.ru/search/vacancy?text=python&salary=&area=1&area=2&ored_clusters=true&enable_snippets=true'
headers = Headers(browser = 'chrome', os = 'win').generate()

r = requests.get(HOST, headers=headers).text
# pprint(r)
soup = BeautifulSoup(r, features = 'lxml')
banner_class = soup.find('div', id = "a11y-main-content")
# pprint(banner_class)

def parsing_HeadHunter():
    data_list = []
    for articles in banner_class:
        article_main = articles.find('div', class_ = 'g-user-content')
        if article_main != None:
            tutorials = article_main.text
            if "Django" in tutorials or 'django' in tutorials or 'Flask' in tutorials or 'flask' in tutorials:
                article_1 = articles.find('div', class_ = 'vacancy-serp-item-body__main-info')
                if article_1 != None:
                    # pprint(article_1)
                    main_info = article_1.find('a', class_ = 'serp-item__title')
                    name = main_info.text
                    # pprint(name)
                    link = main_info.get("href")
                    # pprint(link)
                article_2 = articles.find('span', class_ = 'bloko-header-section-3')
                if article_2 != None:
                    salary = ((article_2.text).replace('\u202f', ''))
                    # pprint(salary)
                article_3 = articles.find('a', class_ = 'bloko-link bloko-link_kind-tertiary')
                if article_3 != None:
                    company = ((article_3.text).replace('\xa0', ' '))
                    # pprint(company)
                article_4 = articles.find('div', class_ = 'vacancy-serp-item__info')
                if article_4 != None:
                    place = (article_4.text).replace((article_3.text),'').replace('\xa0', ' ')
                    # pprint(place)
                data_list.append({
                    "Название вакансии": name,
                    "Компания": company,
                    "Зарплатная вилка": salary,
                    "Расположение": place,
                    "Ссылка": link
                })
                with open ('data.json','w', encoding = 'utf=8') as f:
                    json.dump(data_list, f, sort_keys = False, ensure_ascii = False, indent = 2)
    if data_list == []:
        return pprint("Таких вакансий нет")
    else:
        return pprint("Список сформирован")

def parsing_HeadHunter_dollars():
    data_list = []
    for articles in banner_class:
        article_main = articles.find('div', class_ = 'g-user-content')
        if article_main != None:
            tutorials = article_main.text
            if "Django" in tutorials or 'django' in tutorials or 'Flask' in tutorials or 'flask' in tutorials:
                article_salary = articles.find('span', class_ = 'bloko-header-section-3')
                if article_salary != None:
                    salary = ((article_salary.text).replace('\u202f', ''))
                    # pprint(salary)
                    if 'USD' in salary:
                        article_1 = articles.find('div', class_ = 'vacancy-serp-item-body__main-info')
                        if article_1 != None:
                            # pprint(article_1)
                            main_info = article_1.find('a', class_ = 'serp-item__title')
                            name = main_info.text
                            # pprint(name)
                            link = main_info.get("href")
                            # pprint(link)
                        article_3 = articles.find('a', class_ = 'bloko-link bloko-link_kind-tertiary')
                        if article_3 != None:
                            company = ((article_3.text).replace('\xa0', ' '))
                            # pprint(company)
                        article_4 = articles.find('div', class_ = 'vacancy-serp-item__info')
                        if article_4 != None:
                            place = (article_4.text).replace((article_3.text),'').replace('\xa0', ' ')
                            # pprint(place)
                        data_list.append({
                            "Название вакансии": name,
                            "Компания": company,
                            "Зарплатная вилка": salary,
                            "Расположение": place,
                            "Ссылка": link
                        })
                        with open ('data.json','w', encoding = 'utf=8') as f:
                            json.dump(data_list, f, sort_keys = False, ensure_ascii = False, indent = 2)
    if data_list == []:
        return pprint("Таких вакансий нет")
    else:
        return pprint("Список сформирован")

if __name__ == '__main__':
    parsing_HeadHunter() 
    # parsing_HeadHunter_dollars()
    