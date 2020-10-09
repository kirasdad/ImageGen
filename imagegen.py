from PIL import Image, ImageDraw

# Запрашиваем размеры картинки
(a, b) = eval(input('Введите размеры картинки через запятую: '))
aMax = max(a, b)
aMin = min(a, b)

img = Image.new('RGB', (a, b), (255, 255, 255))
if a >= b:
    shape = [(0, (-aMax/2)+(aMin/2)), (aMax, (aMax/2)+(aMin/2))]
    fill = "#800080"
    outline = "green"
    img1 = ImageDraw.Draw(img)
    img1.ellipse(shape, fill, outline)

    shape2 = [((aMax/2)-(aMin/2), 0), ((aMax/2)+(aMin/2), aMin)]
    fill2 = "#100080"
    img2 = ImageDraw.Draw(img)
    img2.ellipse(shape2, fill2, outline)

if a < b:
    shape = [((-aMax / 2) + (aMin / 2), 0), ((aMax / 2) + (aMin / 2), aMax)]
    fill = "#800080"
    outline = "green"
    img1 = ImageDraw.Draw(img)
    img1.ellipse(shape, fill, outline)

    shape2 = [(0, (aMax / 2) - (aMin / 2)), (aMin, (aMax / 2) + (aMin / 2))]
    fill2 = "#100080"
    img2 = ImageDraw.Draw(img)
    img2.ellipse(shape2, fill2, outline)
fileName = str(a)+'_'+str(b)
img.save(fileName + ".jpg", quality=100)
