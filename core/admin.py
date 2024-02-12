from django.contrib import admin
import boto3
from decouple import config
from django.core.files.storage import default_storage

s3_client = boto3.client(
    's3',
    region_name='nyc3',  # or your Digital Ocean region
    endpoint_url=AWS_S3_ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def upload_to_space(file):
    file_name = file.name
    s3_client.upload_fileobj(
        file,
        AWS_STORAGE_BUCKET_NAME,
        file_name,
        ExtraArgs={'ACL': 'public-read'}  # if you want the file to be publicly accessible
    )
    return f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{file_name}"


@admin.register(VideoFile)
class VideoFileAdmin(admin.ModelAdmin):
    # Define list_display, fields, etc.

    def save_model(self, request, obj, form, change):
        if 'file' in form.cleaned_data:
            file = form.cleaned_data['file']
            obj.file_url = upload_to_space(file)
        super().save_model(request, obj, form, change)
