import pandas as pd
import json

def get_cardnamelist(type):
    filename = "./scraping/"
    if type == 0:
        filename += "mons.json"
    elif type == 1:
        filename += "magic.json"
    elif type == 2:
        filename += "trap.json"

    return pd.read_json(filename)

if __name__ == "__main__":
    n = get_cardnamelist(1)
    print(n)