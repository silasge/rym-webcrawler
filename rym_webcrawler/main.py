import argparse
from rym_webcrawler import RymCharts
from selenium.webdriver import Edge

def rymcharts(url, n, exec_path):
    driver = Edge(executable_path=exec_path)
    rym = RymCharts(url, driver)
    rym.top_charts(n = n, print_log=True)
    rym_df = rym.to_pandas()
    rym_df.to_csv(f"rym_top{n}_chart.csv", index=False)
    

def run():
    parser = argparse.ArgumentParser(description="Get a csv from the RYM's top charts")
    parser.add_argument("url", type=str, help="An url to a RYM's chart page")
    parser.add_argument("--n", dest="n", type=int, default=100, help="An integer representing the top albums")
    parser.add_argument("--exec", dest="exec_path", type=str, default="msedgedriver.exe")
    
    args = parser.parse_args()
    rymcharts(url=args.url, n=args.n, exec_path=args.exec_path)