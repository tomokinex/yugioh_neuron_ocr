def detect_text(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if not texts:
        return []
    else:
        return texts[0].description.split("\n")

if __name__ == "__main__":
    from PIL import Image
    img = Image.open('textDeckImage.jpg')
    img_mons = img.crop((206,412, 714, 1671))
    img_mons.save("temp.jpg")

    result = detect_text('temp.jpg')
    print(result)
