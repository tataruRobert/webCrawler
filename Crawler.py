import requests
from bs4 import BeautifulSoup, ResultSet


class Crawler():

    def getData(self, nrPages, url, currentList,):
        page = 1

        finalList = []
        while page <= nrPages:
            sourceCode = requests.get(url + str(page))
            soup = BeautifulSoup(sourceCode.text, "html.parser")
            soupContainer = soup.findAll('a',{'class' : 'marginright5 link linkWithHash detailsLink'})

            for link in soupContainer:
                href = link.get('href')
                title = str(link)
                begin = title.find('<strong>')
                finn = title.find('</strong>')
                title = title [begin + 8 : finn]
                print(title)
                finalList.append(href)

            page += 1


        with open(currentList, 'r') as file:
            list = [line[:-1] for line in file]

        with open(currentList, 'a') as myFile:
            for item in finalList:
                if not item in list:
                    list.append(item)
                    write(item)



