import stringcomp
import re
def refactor_name(str, namelist):
    result_score = 0.0
    result_word = "Nothing"

    for n in namelist[0]:
        t = stringcomp.string_comp(str, n)
        if t > result_score:
            result_score = t
            result_word = n

    return result_word, result_score

def refactor_num(array):
    ret_array = []
    for s in array:
        if len(s) > 3 and not re.search('[0-9]', s):
            ret_array.append(s)
        elif len(s) == 1:
            ret_array.append(int(s))
        else:
            chars = list(s)
            for char in chars:
                if char.isdigit():
                    ret_array.append(int(char))

    return ret_array

if __name__ == "__main__":
    sample = ['「ドラゴンメイドのお心づくし', 'リボルブート・セクター', 'コズミック・サイクロン', 'クイック・リボルブ', '禁じられた一滴', '1', '1', '3', '23']
    ret = refactor_num(sample)
    print(ret)

    import get_cardnamelist
    namelist = get_cardnamelist.getCardNameList(1)
    sample = ['「ドラゴンメイドのお心づくし', 'リボルブート・セクター', 'コズミック・サイクロン', 'クイック・リボルブ', '禁じられた一滴']
    for s in sample:
        word, score = refactor_name(s, namelist)        
        print(word)

