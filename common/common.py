import base64
import datetime

def convertBase64ToImage(self, image):
        date = datetime.datetime.now()
        image_name = 'IMG_' + str(date.day) + "_" + str(date.month) + "_" + str(date.year) + "_" + str(
            date.hour) + "_" + str(date.minute) + "_" + str(date.microsecond) + ".jpg"
        ima_64_decode = base64.b64decode(image)
        with open(image_name, 'wb') as f:
            f.write(ima_64_decode)
            return image_name
