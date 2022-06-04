import re 
import pandas as pd
from selenium.webdriver.common.by import By


def get_artist(pos_id):
    artist = (pos_id
              .find_element(By.CLASS_NAME, "page_charts_section_charts_item_credited_links_primary")
              .find_elements(By.CLASS_NAME, "artist"))
    artist = " ".join(a.text for a in artist)
    return artist


def get_album(pos_id):
    return pos_id.find_element(By.CLASS_NAME, "page_charts_section_charts_item_link").text


def get_release_date(pos_id):
    return pos_id.find_element(By.CLASS_NAME, "page_charts_section_charts_item_date").text


def get_primary_genres(pos_id):
    prim_gen = (pos_id
                .find_element(By.CLASS_NAME, "page_charts_section_charts_item_genres_primary")
                .find_elements(By.CLASS_NAME, "comma_separated"))
    prim_gen = ", ".join(pg.text for pg in prim_gen)
    return prim_gen


def get_secondary_genres(pos_id):
    try:
        sec_gen = (pos_id
                   .find_element(By.CLASS_NAME, "page_charts_section_charts_item_genres_secondary")
                   .find_elements(By.CLASS_NAME, "comma_separated"))
        sec_gen = ", ".join(sg.text for sg in sec_gen)
        
        return sec_gen
    except:
        return None


def get_descriptors(pos_id):
    try:
        descriptors = (pos_id
                       .find_element(By.CLASS_NAME, "page_charts_section_charts_item_genre_descriptors")
                       .find_elements(By.CLASS_NAME, "comma_separated"))
        descriptors = ", ".join(dsc.text for dsc in descriptors)
        
        return descriptors
    except:
        return None


def get_ratings(pos_id):
    ratings = pos_id.find_element(By.CLASS_NAME, "page_charts_section_charts_item_stats")
    n_ratings = (ratings
                 .find_element(By.CLASS_NAME, "page_charts_section_charts_item_details_ratings")
                 .find_element(By.CLASS_NAME, "full")
                 .text)
    n_reviews = (ratings
                 .find_element(By.CLASS_NAME, "page_charts_section_charts_item_details_reviews")
                 .find_element(By.CLASS_NAME, "full")
                 .text)
    avg_rating  = ratings.find_element(By.CLASS_NAME, "page_charts_section_charts_item_details_average_num").text
    return n_ratings, n_reviews, avg_rating


def get_spotify_id(pos_id):
    data_links = (pos_id
                  .find_element(By.CLASS_NAME, "page_charts_section_charts_item_media_links")
                  .find_element(By.XPATH, ".//*")
                  .get_attribute("data-links"))
    
    spotify_id_pattern = re.compile("([A-Za-z0-9]{22})")
    
    spotify_ids = spotify_id_pattern.findall(data_links)
    
    if len(spotify_ids) > 0:
        return spotify_ids[0]
    else:
        return None

