from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import random

def scrape():
    browser_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **browser_path)

    mars = {}

    # NASA Mars News
    browser.visit('https://mars.nasa.gov/news/')
    html=browser.html
    soup = bs(html, 'html.parser')
    latest_news=soup.find('div',class_='image_and_description_container')
    mars["news_title"]=latest_news.find('a').get_text()
    mars["news_desc"]=latest_news.find('h3').get_text()

    # JPL Mars Space Images - Featured Image
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    html=browser.html
    soup = bs(html, 'html.parser')
    img_grid=soup.find('ul',class_='articles').find_all('li', class_='slide')
    img_url=[]

    for href in img_grid:
        url=href.find('a')
        img_url.append('https://www.jpl.nasa.gov'+url['data-fancybox-href'])
    
    mars["mars_image"]=random.choice(img_url)
    
    # Mars Weather
    browser.visit('https://twitter.com/marswxreport?lang=en')
    html=browser.html
    soup = bs(html, 'html.parser')
    mars["weather"]=soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"}).find('p', 'tweet-text').get_text()

    # Mars Facts
    df=pd.read_html('http://space-facts.com/mars/')[0]
    df.columns=['description', 'value']
    df.set_index('description', inplace=True)

    table = df.to_html()
    table=table.replace('\n','')

    mars["facts"]=table
    
    # Mars Hemisperes
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    items = len(browser.find_by_css("div.description a.itemLink"))

    hemisphere_image_urls = []

    for i in range(items):
        hemisphere = {}
        browser.find_by_css("div.description a.itemLink")[i].click()
        sample = browser.find_link_by_text('Sample').first
        hemisphere['title'] = browser.find_by_css("h2.title").text
        hemisphere['img_url'] = sample['href']
        hemisphere_image_urls.append(hemisphere)
        browser.back()

    mars["hemispheres"]=hemisphere_image_urls

    browser.quit()

    return mars