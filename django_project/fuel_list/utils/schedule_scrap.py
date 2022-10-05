import schedule
import time
from django_project.fuel_list.fuel_parser.fuel_parser.spiders.prices import main as parser
from scrapy.crawler import CrawlerProcess


def main():
    parser()
    print('Spider working now')


# schedule.every().day.at("14:00").do(main)
schedule.every(1).minutes.do(main)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(60)

