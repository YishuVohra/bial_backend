import base64
import uuid

from django.core.files.base import ContentFile

def base64_to_image(base64_string):
    format, imgstr = base64_string.split(';base64,') 
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
