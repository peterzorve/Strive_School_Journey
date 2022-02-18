import requests 
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup

######################################################################################################################

url1 = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&view=advanced'
page1 = requests.get(url1)
soup1 = BeautifulSoup(page1.content, 'html.parser')
genreList_1st_50 = []
starList_1st_50 = []
dateList_1st_50 = []

########################################################################################################################

url2 = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&start=51&ref_=adv_nxt'
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content, 'html.parser')
genreList_2nd_50 = []
starList_2nd_50 = []
dateList_2nd_50 = []

###########################################################################################################################

genres_1st_50 = soup1.find_all('span', class_="genre")
for genre_1st_50 in genres_1st_50:
    genreName_1st_50 = genre_1st_50.text
    genreName_1st_50 = genreName_1st_50.strip()
    genreList_1st_50.append(genreName_1st_50)


genres_2nd_50 = soup2.find_all('span', class_="genre")
for genre_2nd_50 in genres_2nd_50:
    genreName_2nd_50 = genre_2nd_50.text
    genreName_2nd_50 = genreName_2nd_50.strip()
    genreList_2nd_50.append(genreName_2nd_50)


##########################################################################################################################

stars_1st_50 = soup1.find_all('p', class_="")
for star1 in stars_1st_50:
    starsName1 = star1
    starsName1 = starsName1.text
    starsName1 = starsName1.strip()
    starsName1 = starsName1.replace('\n', '')
    starsName1 = starsName1.split('Stars:')[1]
    starList_1st_50.append(starsName1)


stars_2nd_50 = soup2.find_all('p', class_="")
for star2 in stars_2nd_50:
    starsName2 = star2
    starsName2 = starsName2.text
    starsName2 = starsName2.strip()
    starsName2 = starsName2.replace('\n', '')
    starsName2 = starsName2.split('Stars:')[1]
    starList_1st_50.append(starsName2)

##########################################################################################################################

genreListFinal = genreList_1st_50 + genreList_2nd_50
starListFinal = starList_1st_50 + starList_2nd_50

##########################################################################################################################




page = requests.get("https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&ref_=adv_prv")
#print(page)
soup = BeautifulSoup(page.content,'html.parser')
#print(soup)

#Scraping Director name.-page-1

m_name = soup.find_all('div', class_ = "lister-item-content")
movie_name = []
for name in m_name:
    mo_name = name.a.text
    movie_name.append(mo_name)
#print(movie_name)

# Description
des = soup.find_all('p',class_ = "text-muted")

description = []
for i in des:
    m_des = i.text.strip()
    description.append(m_des) 
only_description = description[1::2]
#print(only_description)

# 

# description = []
# # for i in des:
# #     des1 = i.text.strip()
# #     description.append(des1)
# # print(description)


# Duration of the movie.-page-1
# def film_duration():
#     d_time = soup.find_all('span', class_ = "runtime")
#     duration = []
#     for dt in d_time:
#         dur = dt.text
#         duration.append(dur)
#     return duration
# f_d = film_duration()
# print(f_d)
# print(film_duration())
# print(duration)

# # Rating - Imdb
# imdb_r = soup.find_all('div', class_ = "inline-block ratings-imdb-rating")
# imdb_rating = []
# for ir in imdb_r:
#     r_stars = ir.strong.text
#     imdb_rating.append(r_stars)
# #print(imdb_rating)

# #Rating - Metascore-page-1
# meta_r = soup.find_all('div', class_ = "inline-block ratings-metascore")
# meta_rating =[]
# for mr in meta_r:
#     meta_score = mr.span.text.strip()
#     meta_rating.append(meta_score)
# #print(len(meta_rating))

# # director-name-page1
# d_name = soup.find_all('p', class_ = "")
# director_name =[]
# for dn in d_name:
#     dir_name = dn.a.text.strip()
#     director_name.append(dir_name)
# #print(director_name)

# # page-2
# page2 = requests.get("https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&start=51&ref_=adv_nxt")
# soup2 = BeautifulSoup(page2.content, 'html.parser')

# # Duration of the movie.-page-2
# d_time2 = soup2.find_all('span', class_ = "runtime")
# duration2 = []
# for dt in d_time2:
#     dur = dt.text
#     duration2.append(dur)
# #print(duration2)

# # Rating - Imdb-page2
# imdb_r2 = soup2.find_all('div', class_ = "inline-block ratings-imdb-rating")
# imdb_rating2 = []
# for ir in imdb_r2:
#     r_stars = ir.strong.text
#     imdb_rating2.append(r_stars)
# #print(imdb_rating2)

# #Rating - Metascore-page-2
# meta_r2 = soup2.find_all('div', class_ = "inline-block ratings-metascore")
# meta_rating2 =[]
# for mr in meta_r2:
#     meta_score = mr.span.text.strip()
#     meta_rating2.append(meta_score)
# #print(len(meta_rating2))

# # director-name-page2
# d_name2 = soup2.find_all('p', class_ = "")
# director_name2 =[]
# for dn in d_name2:
#     dir_name = dn.a.text.strip()
#     director_name2.append(dir_name)
# #print(director_name2)

# # Intersection of two lists.

# director = director_name+director_name2
# imdbrating = imdb_rating+imdb_rating2
# metarating = meta_rating+meta_rating2
# film_duration = duration+duration2

# print(director[51])
# print(len(director))
# print(len(imdbrating))
# print(len(metarating)) # There was no meta score for pushpa movie.
# print(len(film_duration))

# pandas data frame.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action'
url2 = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&start=51&ref_=adv_nxt'

# page2 = requests.get(url2)
# print(page2)


# action2 = BeautifulSoup(page2.content, 'html.parser')

# title100 = action2.find_all('div', class_= "lister-item-content")
# movie_title = []

# for i in title100:
#     mo_title = i.a.text
#     movie_title.append(mo_title)


# print(movie_title)



def url_getter(url):
    page_all = requests.get(url)
    action = BeautifulSoup(page_all.content, "html.parser")
    return action
    

page2 = url_getter(url2)
page1 = url_getter(url)
#print(t1)


def title(action):
    title100 = action.find_all('div', class_= "lister-item-content")
    movie_title = []

    for i in title100:
        mo_title = i.a.text
        movie_title.append(mo_title)
    return movie_title




def description(action):
    desc100 = action.find_all('p', class_= "text-muted")
    des1 = desc100
    movies_desc = []

    for i in desc100:
        mo_desc = i.text.replace('\n', " ")                   #strip()                          
        movies_desc.append(mo_desc)
    return movies_desc



def release_date(action): 
    rdate100 = action.find_all('span', class_= "lister-item-year text-muted unbold")
    r_date = []
    
    for i in rdate100:
        r_dt = i.text
        r_date.append(r_dt)
    return r_date

first_50_titles = title(page1)
#print(first_50_titles)
second_50_titles = title(page2)
#print(second_50_titles)
all_titles = first_50_titles + second_50_titles
print(all_titles)

# first_50_description = description(page1)
# print(first_50_description)
# second_50_description = description(page2)
# print(second_50_description)

# first_50_reldate = release_date(page1)
# #print(first_50_reldate)
# second_50_reldate = release_date(page2)
# #print(second_50_reldate)

# all_release_date = first_50_reldate + second_50_reldate
# print(all_release_date)









data = {'DIRECTOR': director, GENRE' : genreListFinal, 'STARS' : starListFinal}


table = pd.DataFrame(data)
print(table)






