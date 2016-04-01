import mechanize
from bs4 import BeautifulSoup
import re
import sys
#Browser
br = mechanize.Browser()
#Encoding for writing in File
reload(sys)
sys.setdefaultencoding('utf-8')


#Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

pg=br.open('http://websismit.manipal.edu/')
print("Page Opened")
response1=br.response()
br.select_form(name='loginform')
regno="xxxxxxxxx"
bd="xxxx-xx-xx"
FileName="Data.txt"


regno=raw_input("Regno")
bd=raw_input("bd in yyyy-mm-dd")
FileName=regno
FileName+="'s Data.txt"

try:
	#user Credentials
	br.form['idValue']=regno
	br.form['birthDate_i18n']=bd
	br.form['birthDate']=bd
	br.submit()
	br.find_link(text='Academic Status')
	req = br.click_link(text='Academic Status')
except:
	print("WRONG (Reg_no OR Birtday) or poor internet Connection")
	sys.exit()
	
print( "Logged In")
br.open(req)
print("Academic Status")
req=br.click_link(text='JAN-MAY 2016')
br.open(req)
print "JAN-MAY"

raw_data=br.response().read()
a=re.sub('<.+?>', '', raw_data)
f=open("raw_data",'w')
f.write(a)

console=sys.stdout
fulldata=" "

#Reaad Data
soup = BeautifulSoup(raw_data)
soup.prettify()
tables = soup.find_all('table')
f=open("Tables.txt","w")
print("Tabling in 3 2 1...")

#Writing to File
sys.stdout=open(FileName,"w")
for table in tables:
  tr_tags = table.find_all('tr')

  for tr in tr_tags:
    td_tags = tr.find_all('td')

    for td in td_tags:
      text = td.text  
      print(text)
      fulldata+=text         


sys.stdout=console

test1=open("Most_Recent.txt","w")
fulldata=fulldata.strip()
fulldata=fulldata.replace('\n',"   ")
test1.write(fulldata)
print(br.title())
print "<----------DONE--------> Check your File!"