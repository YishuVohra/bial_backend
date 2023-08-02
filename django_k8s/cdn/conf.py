import os

#AWS_STORAGE_BUCKET_NAME='django-k8s-space'
#AWS_S3_ENDPOINT_URL="https://sgp1.digitaloceanspaces.com"
#AWS_S3_OBJECT_PARAMETERS = {
#    "CacheControl": "max-age=86400",
#    "ACL": "public-read"
#}
#AWS_LOCATION="https://django-k8s-space.sgp1.digitaloceanspaces.com"
#DEFAULT_FILE_STORAGE = "django_k8s.cdn.backends.MediaRootS3BotoStorage"
#STATICFILES_STORAGE = 'django_k8s.cdn.backends.StaticRootS3BotoStorage'

AWS_DEFAULT_ACL = None
AWS_ACCESS_KEY_ID =  os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("S3_BUCKET")
AWS_S3_REGION_NAME = os.environ.get("S3_REGION")
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
    "ACL": "public-read"
}
AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
# DEFAULT_FILE_STORAGE = "django_k8s.cdn.backends.MediaRootS3BotoStorage"  // uncomment after deployment
# STATICFILES_STORAGE = "django_k8s.cdn.backends.StaticRootS3BotoStorage"  // uncomment after deployment
