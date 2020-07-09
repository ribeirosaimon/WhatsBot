def list_stock():
    list_stock = []
    r = requests.get('https://www.fundamentus.com.br/resultado.php')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    soup = soup.find_all('span',{'class':'tips'})
    for x in soup:
        list_stock.append(x.text)
    return list_stock
