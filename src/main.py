import re         
import os
import sys
reload(sys)
import request
import requests  
from bs4 import BeautifulSoup 
sys.setdefaultencoding('utf-8')



def main():
 lyrics=list()

 def print_lines():                                    #printing dotted lines
  print(("-"*68))


 def screen_clear():                                   #clearing terminal screen
  if os.name == 'nt':
   os.system('cls')
  else:
   os.system('clear')


 def intro():
  print("\t\t\t\t\t-----Lyrics Downloader------")
  box_msg(''' Created by Gautham Prakash @: gauthamp10@gmail.com''')


 def box_msg(msg):                                     #for printing text in a box
  row = len(msg)
  h = ''.join(['+'] + ['-' *row] + ['+'])
  result= h + '\n'"|"+msg+"|"'\n' + h
  print(result)


 def save_file(filename,content):                      #for writing the ouput file. 
  cwd = os.getcwd()
  with open('%s'%filename,'wb') as f:
   for row in content:
    f.write(str(row).encode())
  print_lines()
  print(("Lyrics saved at: "+cwd+"/"+filename))
  print_lines()


 def find_lyrics_page():                               #for finding lyrics page
  query=raw_input("Enter the song : ").lower()
  song=query.replace(' ','+')
  try:
   html_page = requests.get("https://www.google.com/search?q="+song+"+lyrics")
   print("\n--------------------------------------------------------")
   print("Sit tight! while we are fetching lyrics for '"+query+"'.........")
  except:
   print("\nNetwork Error!!...Please retry!")
   sys.exit(1)
  try:
   soup = BeautifulSoup(html_page.text,'html.parser')
   links = re.findall("https:\/\/www\.azlyrics\.com\/lyrics\/.+html", str(soup))
   links=str(links)[2:].split('&')
   scrape_url=links[0]
  except:
   print("\nNo lyrics found!!..Try again with artist name.")
   sys.exit(1)
  return scrape_url


 def find_lyrics(scrape_url):                          #for finding the lyrics itself
  try:	
   data=requests.get(scrape_url)     
   soup = BeautifulSoup(data.text,'html.parser') 
   title=soup.find('title')
   title=title.text.split('|')
   title=title[0]
   divs=soup.findAll('div',attrs={'class':None})
   for div in divs:
    lyrics.append(div.text)
  except:
    print("No lyrics found!!..")
    sys.exit(1)
  return(title,lyrics)


 def display_lyrics(title,lyrics):                     #to display lyrics in terminal
  print((lyrics[1]))
  print_lines()
  ch=raw_input("Do you want to save the lyrics?..(y/n): ")
  if ch == 'yes' or ch == 'Yes' or ch == 'y' or ch == 'Y':
   print_lines()
   save_file((title+".txt"),lyrics)
   print_lines()


 screen_clear()
 intro()
 scrape_url=find_lyrics_page()
 title,lyrics=find_lyrics(scrape_url)
 print_lines()
 print("\nFound match: ")
 print((title+"\n"))
 print_lines()
 ch=raw_input("Do you want to display the lyrics?..(y/n): ")
 if ch == 'yes' or ch == 'Yes' or ch == 'y' or ch == 'Y':
  display_lyrics(title,lyrics)
  print("\n")
 else:
  print_lines() 
  ch=raw_input("Do you want to save the lyrics?..(y/n): ")
  if ch == 'yes' or ch == 'Yes' or ch == 'y' or ch == 'Y':
  	save_file((title+".txt"),lyrics)


if __name__ == '__main__':                                       #Calling main(), the actual entry point for the scraper
    main()  
    exit(0)
 
