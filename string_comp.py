import difflib
def string_comp(str1, str2):
    rate = difflib.SequenceMatcher(None, str1, str2).ratio()
    return rate

def string_comp_l(str1, str2):
    import Levenshtein
    lev_dist = Levenshtein.distance(str1, str2)
    devider = len(str2)
    if len(str1) > len(str2):
        devider = len(str1)
    lev_dist = lev_dist / devider
    lev_dist = 1 - lev_dist
    return lev_dist