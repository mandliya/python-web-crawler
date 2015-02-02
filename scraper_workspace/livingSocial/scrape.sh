#!/usr/bin/Env bash

# be sure to change both virtualenv directory and scrape/living_social
# directory to where your venv and code is.
source $WORKON_HOME/scrape/bin/activate
cd /Users/mandliya/practice/python-web-crawler/scraper_workspace/livingSocial/scraper_app/
scrapy crawl livingsocial
