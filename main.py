import requests
import os
from bs4 import BeautifulSoup

def main():
  STATIC_PATH = './static'

  if not os.path.exists(STATIC_PATH):
    os.mkdir('./static')

  url = input('url here: ')
  if url[:8] != 'https://':
    url = f'https://{url}'

  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'xml')
  bookTitle = soup.find('div', 'mt-4').find_next().get_text()

  with open(f'./static/{bookTitle}.html', 'w') as file:
    soup.find('title').string = bookTitle
    
    soup.select('.navbar')[0].decompose()
    soup.find(class_ = 'modal fade').decompose()
    soup.find(class_= 'text-center page-header').decompose()
    soup.find(class_='mt-2 text-center').decompose()
    
    for script in soup.find_all('script'):
      script.decompose()
    
    for link in soup.find_all('link'):
      link.decompose()
    
    for meta in soup.find_all('meta')[3:]:
      meta.decompose()
      
    for hr in soup.find_all('hr'):
      hr.decompose()
    
    for footer in soup.select('div.mt-2'):
      footer.decompose()
      
    ads = soup.find_all('a', class_=False)
    for ad in ads:
      ad.decompose()
      
    
    linkTag = soup.new_tag('link', rel='stylesheet', href='https://securestuff.net/Content/css?v=xqt6HNMc5Wg3i_dETDG3pSjJqZ2biRuCeySE1FYZN7Q1')
    linkTag2 = soup.new_tag('link', rel='stylesheet', href='../style.css')

    soup.find('head').append(linkTag)
    soup.find('head').append(linkTag2)
    
    file.write(soup.prettify())
    
    print('Done.')

if __name__ == '__main__':
  try:
    main()
  except:
    print('An error occured.')