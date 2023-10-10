import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# print(soup.title)
# print(soup.title, type(soup.title.string))

# print(soup.div)  # isse hum phela div jo rahega wo dega 

# print(soup.find_all("div")) # isse humhe sab div milenge 

# print(soup.find_all("div")[0]) # ye inding ke hisb se show karega 

# print(type(soup.find_all("div")[0]))  # type se ye batayega <class 'bs4.element.Tag'>

# for link in soup.find_all("a"):
#     print(link) 

for link in soup.find_all("a"):
    print(link.get("href"))    # isse hum hink sirif milega
    print(link.get_text())


# s= soup.find(id="link3")  # isse humhe jo id hai usse content mil jayegi
# print(s.get("href"))

# print(soup.select("div.italic"))  # with help of css selector
# print(soup.select("span#italic")) 
# print(soup.span.get("Class"))

# print(soup.find(id="italic"))

# print(soup.find_all(class_="italic")) # python me class ek reserve keyword hai and find se ek milta hai element and find_all se sare 

# for child in soup.find(class_="container").children:
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent)

# i=0
# for parent in soup.find(class_="box").parents:
#     i+=1
#     print(parent)
#     if(i==2):
#         break

# count = soup.find(class_="container")
# count.name = "span"  # isse hum span tag ke uder kar kar hai and other feature ek new html file bhi bana sakte hai other fetaure se uodated dom ke sath
# count["class"]="myclass class 2" # isse hum class bhi change kar sakte hai 
# print(count)

# For inserting new thing int to the soup
# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)


# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag)
# with open("modified.html", "w") as f:
#     f.write(str(soup))


# count = soup.find(class_="container")
# print(count.has_attr("id"))  # we can find attribut in element ,checking id is available or not in terminal it will show False 
# print(count.has_attr("class")) 
# print(count.has_attr("contenteditable")) 

def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

# results = soup.find_all(has_class_but_not_id)
# print(results) 
# isse hume meta tags milege
def has_content(tag):
    return tag.has_attr("content")

# results = soup.find_all(has_class_but_not_id)
results = soup.find_all(has_content)  # abhi tab dekh that find a_all class_ leta hai ,id leta hai aur function bhi leta hai
for result in results:
    print(results,"\n\n") 
