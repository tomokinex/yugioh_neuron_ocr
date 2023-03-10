from PIL import Image
import get_cardnamelist
import refactor
import google_api

def image2text(img, size, index):
    img_mons = img.crop(size)
    img_mons.save("temp.jpg")
    result = google_api.detect_text('temp.jpg')
    if not result:
        return [], [] 

    result = refactor.refactor_num(result)
    if len(result) % 2 != 0 : 
        # result.pop()
        # TODO error 条件が緩すぎる & error メッセージの整備
        print("ERROR")
        print(result)
        exit()
    half_length = len(result)//2
    result_name = result[:half_length]
    result_num = result[half_length:]

    namelist = get_cardnamelist.get_cardnamelist(index)
    result_name_fix = []
    for s in result_name:
        word, score = refactor.refactor_name(s, namelist)        
        result_name_fix.append(word)
    return result_name_fix, result_num

if __name__ == "__main__":
    base_width = 1785
    base_height = 2526
    img = Image.open('textDeckImage_sample.jpg')
    img = img.resize((base_width, base_height))
    mons_names, mons_nums = image2text(img, (206,412, 714,1671), 0)
    magic_names, magic_nums = image2text(img, (715,412, 1225,1671), 1)
    trap_names, trap_nums = image2text(img, (1226,412, 1736,1671), 2)
    exmons_names, exmons_nums = image2text(img, (206,1790, 714, 2420), 0)

    result_name = []
    result_num = []
    result_name.extend(mons_names)
    result_name.extend(magic_names)
    result_name.extend(trap_names)
    result_name.extend(exmons_names)
    result_num.extend(mons_nums)
    result_num.extend(magic_nums)
    result_num.extend(trap_nums)
    result_num.extend(exmons_nums)

    result_file = open("result.csv", mode='w', encoding='utf-8')
    for s, n in zip(result_name, result_num):
        result_file.write(''+ s + ',' + str(n) + '\n')
    result_file.close()

