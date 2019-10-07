from PIL import Image
img = Image.open('image.jpg').convert('LA')
im = Image.new('LA', img.size)

for i in range(1,img.size[0]):
    for y in range(1,img.size[1]):
        pixel=img.getpixel((i,y))
        #edit the value 45 if you want to remove more noise 
        if pixel[0]<45:
            im.putpixel((i,y),pixel)
        else:
            pixel=(255,255)
            im.putpixel((i,y),pixel)
im.convert('RGB').save('new.jpeg')
