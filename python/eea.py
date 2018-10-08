from lxml import html
import requests
from bs4 import BeautifulSoup
response = requests.get('https://entethalliance.org/members-directory/', headers={'User-Agent': 'Mozilla/5.0'})
tree = html.fromstring(response.content)
html_soup = BeautifulSoup(response.text, 'html.parser')
print(html_soup)
prime_categories = html_soup.find_all('div', class_ = 'entry')
i=0
for main_categories in prime_categories:
    i+=1
    print(i,main_categories.text)
# 	print('INSERT INTO PRIMARY_PROD_CATEGORY(CATEGORY_NAME) VALUES(\''+main_categories.a.text+'\');')	
    
	# un_list = main_categories.div.div.find_all('ul', class_ = 'desktop-navBlock')
	# # print(un_list)
	
	# for item in un_list:	
	# 	print ('INSERT INTO SECONDARY_PROD_CATEGORY(CATEGORY_NAME,PRIMARY_CATEGORY_ID) VALUES(\''+item.li.a.text+'\','+'(select ID from PRIMARY_PROD_CATEGORY where CATEGORY_NAME=\''+main_categories.a.text+'\'));');	
	# 	ter_categories = item.find_all('a',class_ = 'desktop-categoryLink')
	# 	for ter_category in ter_categories:
	# 			if(item.li.a.text == 'Brands'):
	# 				print('INSERT INTO TERTIARY_PROD_CATEGORY(CATEGORY_NAME,SECONDARY_CATEGORY_ID) VALUES(\''+ter_category.text+'\',(select ID from SECONDARY_PROD_CATEGORY where CATEGORY_NAME=\''+item.li.a.text+'\' and primary_category_id =(select id from primary_prod_category where category_name=\''+main_categories.a.text+'\' ) ));')
	# 			else:
	# 			  		 print('INSERT INTO TERTIARY_PROD_CATEGORY(CATEGORY_NAME,SECONDARY_CATEGORY_ID) VALUES(\''+ter_category.text+'\','+'(select ID from SECONDARY_PROD_CATEGORY where CATEGORY_NAME=\''+item.li.a.text+'\'));');		
					