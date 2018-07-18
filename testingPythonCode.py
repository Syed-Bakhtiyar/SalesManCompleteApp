import datetime
import base64
import os
date = datetime.datetime.now()

print(date.day)
print(str(date.month))
print(str(date.year))
print(str(date.hour))
print(str(date.minute))
print(str(date.second))
print(str(date.microsecond))


def convertBase64ToImage(image):
    date = datetime.datetime.now()
    image_name = 'IMG_' + str(date.day) + "_" + str(date.month) + "_" + str(date.year) + "_" + str(date.hour) + "_" + str(date.minute) + "_" + str(date.microsecond) + ".jpg"
    ima_64_decode = base64.b64decode(image)
    image_directory = os.path.dirname(image_name)
    _image_  = os.path.join(image_directory,image_name)
    with open(image_name, 'wb') as f:
        f.write(ima_64_decode)

a = input("")
convertBase64ToImage(a)