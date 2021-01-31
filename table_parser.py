import pandas as pd

from urllib.request import Request, urlopen
from config import config

P2P_ANLAGE_URL = config["P2P_ANLAGE_URL"]
P2P_EXPLORE_URL = config["P2P_EXPLORE_URL"]

def get_p2p_anlage_ratings():
    req = Request(P2P_ANLAGE_URL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    tables = pd.read_html(webpage) 
 
    rating_grades = [int(i.split(' ')[0]) for i in tables[3].Gesamtbewertung.array]

    list_rated_los = ['Esto', 'Placet Group', 'Credissimo', 'Credius', 'Creamfinance', 'DelfinGroup', 'Creditstar',
                      'IuteCredit', 'Mogo', 'Everest Finanse', 'Finitera', 'Kredit Pintar', 'Mikro Kapital Belarus', 
                      'TASCredit', 'Pinjam Yuk', 'Wowwo', 'ID Finance', 'Revo', 'Sun Finance', 'Kviku', 'IDF Eurasia', 
                      'Zenka', 'Dozarplati']

    ratings = {}
    for lo, rating in zip(list_rated_los, rating_grades):
        ratings[lo] = rating

    return ratings


def get_p2p_explore_ratings():
    req = Request(P2P_EXPLORE_URL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    tables = pd.read_html(webpage)  # Returns list of all tables on page
    los_table = tables[1]  # Select table of interest

    lo_scores = {}
    for lo in los_table.values:
        lo_name = lo[0]
        lo_score = lo[7]
        lo_scores[lo_name] = lo_score
        print("P2P Explore Rating for {}: {}".format(lo_name, lo_score))
    return lo_scores
