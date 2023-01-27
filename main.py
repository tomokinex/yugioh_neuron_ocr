from PIL import Image
import get_cardnamelist
import refactor
import google_api

def image2text(img, size, index):
    img_mons = img.crop(size)
    img_mons.save("temp.jpg")
    result = google_api.detect_text('temp.jpg')
    namelist = get_cardnamelist.get_cardnamelist(index)
    result = refactor.refactor_num(result)
    if len(result) % 2 != 0 : 
        print("ERROR")
        print(result)
        exit()
    half_length = len(result)//2
    result_name = result[:half_length]
    result_num = result[half_length:]

    result_name_fix = []
    for s in result_name:
        word, score = refactor.refactor_name(s, namelist)        
        result_name_fix.append(word)
    return result_name_fix, result_num

if __name__ == "__main__":
    img = Image.open('textDeckImage_sample.jpg') 
    mons_names, mons_nums = image2text(img, (206,412, 714,1671), 0)
    magic_names, magic_nums = image2text(img, (715,412, 1225,1671), 1)
    trap_names, trap_nums = image2text(img, (1226,412, 1736,1671), 2)

    result_name = []
    result_num = []
    result_name.extend(mons_names)
    result_name.extend(magic_names)
    result_name.extend(trap_names)
    result_num.extend(mons_nums)
    result_num.extend(magic_nums)
    result_num.extend(trap_nums)

    result_file = open("result.csv", mode='w', encoding='utf-8')
    for s, n in zip(result_name, result_num):
        result_file.write(''+ s + ',' + str(n) + '\n')
    result_file.close()

