## Introduction

This package serves as a scrapper to the famous social music website [Rate Your Music](https://rateyourmusic.com/). You can grab the top charts from any category in the site, and it returns information like: name of the artist, name of the album, date of release, primary and secondary genres and album descriptors.

## How to install it

## Option 1: Cloning this repository

You just need to clone this repository and install the wheel (it's inside the dist folder) in your python's virtual environment.

```
pip install rym_webcrawler-0.1.0-py3-none-any.whl
```


Also, you'll need a selenium's webdriver configured. This repository comes with the edge webdriver. You can find other webdrivers in Selenium's [website](https://selenium-python.readthedocs.io/installation.html).



## How to use it

You'll need two things to initiate the scrapper: an url to the RYM's chart of interest and a selenium driver.

For example, if you want the top 100 albums of all time in RYM's website, you can do the following.

``` py
from selenium.webdriver import Edge
from rym_webcrawler import RymCharts

driver = Edge(executable_path="./webdrivers/msedgedriver.exe")
chart_url = "https://rateyourmusic.com/charts/top/album/all-time/deweight:live,archival,soundtrack/"

## Initiate the RymChart class
rym = RymCharts(url=chart_url, driver=driver)

# top 100 albums of all time in RYM
rym.top_charts(n=100)

# If you need to have it in a Pandas DataFrame
rym_df = rym.to_pandas()
```