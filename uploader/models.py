import os, uuid, datetime
from django.db import models
from django_summernote.models import AbstractAttachment
from django_summernote.utils import get_attachment_storage

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext) # 
    today = datetime.datetime.now().strftime('%d-%m-%Y')
    return os.path.join('attachments', today, filename)

# Create your models here.
class Attachment(AbstractAttachment):
    file = models.FileField(
        upload_to=upload_to,
        storage=get_attachment_storage()
    )
 

