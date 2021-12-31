#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
#url = 'https://redplanetscience.com/'
#browser.visit(url)

# Optional delay for loading the page
#browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
#html = browser.html
#news_soup = soup(html, 'html.parser')

#slide_elem = news_soup.select_one('div.list_text')


# In[5]:


#slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first a tag and save it as `news_title`
#news_title = slide_elem.find('div', class_='content_title').get_text()
#news_title


# In[7]:


# Use the parent element to find the paragraph text
#news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
#news_p


# ### JPL Space Images Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[14]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[16]:


# 1. Use browser to visit the URL 
# My computer is a company-owned computer, and I cannot access the provided website due to corporate security policy.  
#      I am using the below website as a surrogate for the provided wesbsite.
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[17]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the full-resolution image URL and title for each hemisphere image. 
#    The full-resolution image will have the .jpg extension. 

#    Loop through the full-resolution image URL, click the link, find the Sample image anchor tag, and get the href.  

#    Save the full-resolution image URL string as the value for the img_url key that will be stored in the dictionary 
#    you created from the Hint.

#    Save the hemisphere image title as the value for the title key that will be stored in the dictionary you 
#    created from the Hint.  

#    Before getting the next image URL and title, add the dictionary with the image URL 
#    string and the hemisphere image title to the list you created in Step 2.

# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')
items = html_soup.find_all('div', class_='item')

# Scrape the 4 images

for x in items: 
        hemisphere_images = {}  
        hemispheres = {} 
        
        # Store title
        title = x.find('h3').text
        print(title)
        
        img_url = x.find('a', class_='itemLink product-item')['href']
        print(img_url)

        # Use the base url to create an absolute url
        complete_url = f'https://astrogeology.usgs.gov/{img_url}'
        print(complete_url)
        
        # Find and click the full image button
        browser.visit(complete_url)
        element = browser.find_link_by_text('Sample').first
        full_url = element['href']
        print(full_url)
        
        # Create dictionaries 
        hemispheres["full_url"] = full_url
        hemispheres["title"] = title
        hemisphere_image_urls.append(hemispheres)
        browser.back()


# In[18]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[19]:


# 5. Quit the browser
browser.quit()

