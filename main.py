from Crawler import Crawler

if __name__ == "__main__" :

    currentList = '/Users/tatarurobert/PycharmProjects/WebCrawler/currentList'
    url = 'https://www.olx.ro/electronice-si-electrocasnice/telefoane-mobile/iphone/q-iphone-x/?search%5Bfilter_float_price%3Afrom%5D=1500&search%5Bfilter_float_price%3Ato%5D=3000&search%5Bdescription%5D=1&page='

    while True :
        crawler = Crawler()
        crawler.getData(1, url, currentList)
