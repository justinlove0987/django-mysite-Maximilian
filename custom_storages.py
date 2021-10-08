from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticFileStorage(S3Boto3Storage):
    # STATICFILES_FOLDER is a setting we will add manually to the settings.py file.
    location = settings.STATICFILES_FOLDER

class MediaFileStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_FOLDER