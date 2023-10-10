import requests
from bs4 import BeautifulSoup

# step 1: get the Html

url = "https://codewithharry.com"
# r = requests.get(url)		# r variable has all the HTML code
# htmlContent = r.content	# r returns response so if we want the code we write r.content
# print(htmlContent)

# htmlText = r.text
# print(htmlText)

# step 2 parse the HTML

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


# step 3 : Html Tree traversal

title = soup.title
print(title)

# comanly used types of object :
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2.Navigablestring
# print(type(soup)) # 3.BeautifulSoup
# # 4. comment
# below example for comment:-

# markup = "<p><!--  this is coment  --></P>"
# soup2 = BeautifulSoup(markup)
# # print(soup2.p)
# print(type(soup2.p.string))
# exit()

# get the title of the Html page
title = soup.title

# Get All the paragraphds from the page 

paras = soup.find_all('p')
# print(paras)

# Get All the Anchors from the page 
anchors = soup.find_all('a')
# print(anchors)

# Get the fisrt element of the page 
# print(soup.find('p'))

# get classses of anyelemnt i tne Html page
# print(soup.find('p')['class'])

# find all the elemnts with class lead 
# print(soup.find_all("p", class_="lead"))

# Getting text from tags(text/get_text()):

# print(soup.find('p').text)
# OR
# print(soup.find('p').get_text())

# Get all the links on the page:

# for link in anchors:
#     print(link.get('href'))

# anchors = soup.find_all('a')
# all_links = set()
# for link in anchors:
#     if(link.get('href') !='#'):
#         linkText = "https://codewithharry.com" + link.get('href')
#         all_links.add(link)
#         print(linkText)

# Contents: for all content of ul and li

# ul = soup.find("ul")
# print(ul.contents)

# 1. Children:
# ul = soup.find("ul")
# for i in ul.children:
# 	print(i)
     
# 2. Parent:

# ul = soup.find("ul")
# print(ul.parent)

# 3. next_sibling and previous_siblings:
# Like parent we can go to next sibling and then next sibling like this:

# ul = soup.find(id="li")
# print(ul.next_sibling.next_sibling)
# We can also get all siblings by next_siblings() function. This functions gives a generator because of which we have to iterate it, which means code would be like:

# ul = soup.find(id="li")

# for j in ul.next_siblings:
#     print(j)
# There is also a function named previous_siblings() to get previous siblings. Code is like this:

# for i in ul.previous_siblings:
#     print(i)
# Like next_sibling, we can also use previous_sibling() function and code is similar like earlier:

# print(ul.previous_sibling.previous_sibling)

# css selector in jquery

# elem = soup.select('# loginModal')
# print(elem)

# elem = soup.select('.model-footer')
# print(elem)  




# Writing data in CSV:

# f = open("file.csv", "w")
# f.write("Every,word,will,go,in,separate,column\n")
# f.write("This,will,go,in,next,row")
# f.close()

# with open("file.csv", "w") as f:
#     f.write("Every,word,will,go,in,separate,column\n")
#     f.write("This,will,go,in,next,row")


# python -i filename.py    # write file name with format(.py)