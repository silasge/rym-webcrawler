import pandas as pd
from selenium.webdriver.common.by import By
from rym_webcrawler import utils

class RymCharts:
    def __init__(self, url, driver):
        if url[-1] != "/": url += "/"
        self.url = url
        self.driver = driver
        
        
    def top_charts(self, n, print_log=False):
        page = 1
        pos_id = 0
        
        self.chart_dict = {
            "position": [],
            "artist": [],
            "album": [],
            "release_date": [],
            "primary_genres": [],
            "secondary_genres": [],
            "descriptors": [],
            "number_ratings": [],
            "number_reviews": [],
            "avg_rating": [],
            "id_spotify": []
        }
        
        while pos_id <= n:
            website = self.url + str(page)
            self.driver.get(website)
            pos = self.driver.find_elements(By.XPATH, "//div[contains(@id, 'pos')]")
            for p in pos:
                pos_id = int(p.get_attribute("id").replace("pos", ""))
                if pos_id > n: break
                self.chart_dict["position"].append(pos_id)
                self.chart_dict["artist"].append(utils.get_artist(p))
                self.chart_dict["album"].append(utils.get_album(p))
                self.chart_dict["release_date"].append(utils.get_release_date(p))
                self.chart_dict["primary_genres"].append(utils.get_primary_genres(p))
                self.chart_dict["secondary_genres"].append(utils.get_secondary_genres(p))
                self.chart_dict["descriptors"].append(utils.get_descriptors(p))
                self.chart_dict["number_ratings"].append(utils.get_ratings(p)[0])
                self.chart_dict["number_reviews"].append(utils.get_ratings(p)[1])
                self.chart_dict["avg_rating"].append(utils.get_ratings(p)[2])
                self.chart_dict["id_spotify"].append(utils.get_spotify_id(p))
                if print_log is True: print(f"Position {pos_id} finished")
            page += 1
            
        return self
    
    
    def to_dict(self):
        return self.chart_dict
    
    
    def to_pandas(self):
        return pd.DataFrame(self.chart_dict)
            
        
        