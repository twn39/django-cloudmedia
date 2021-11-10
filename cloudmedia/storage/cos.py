from django.core.files.storage import Storage
from django.conf import settings
from qcloud_cos import CosConfig, CosServiceError
from qcloud_cos import CosS3Client
import logging

logger = logging.getLogger(__name__)


class CosCloudStorage(Storage):
    def __init__(self):
        self.secret_id = settings.COS_SECRET_ID
        self.secret_key = settings.COS_SECRET_KEY
        self.region = settings.COS_REGION
        self.token = None
        self.scheme = settings.COS_SCHEME
        self.config = CosConfig(Region=self.region, SecretId=self.secret_id, SecretKey=self.secret_key, Token=self.token, Scheme=self.scheme)
        self.bucket = settings.COS_BUCKET
        self.client = CosS3Client(self.config)

    def _open(self, name, mode='rb'):
        response = self.client.get_object(name, True)
        return response.content

    def _save(self, name, content):
        response = self.client.put_object(
            Bucket=self.bucket,
            Body=content.read(),
            Key=name,
            EnableMD5=False
        )
        return name

    def delete(self, name):
        self.client.delete_object(
            Bucket=self.bucket,
            Key=name
        )

    def exists(self, name):
        return self.client.object_exists(self.bucket, name)

    def listdir(self, path):
        pass

    def size(self, name):
        info = self._info(name)
        if info is not None:
            return info['Content-Length']
        return None

    def url(self, name):
        return settings.COS_BASE_URI + name

    def get_accessed_time(self, name):
        pass

    def get_created_time(self, name):
        pass

    def get_modified_time(self, name):
        info = self._info(name)
        if info is not None:
            return info['Last-Modified']
        return None

    def path(self, name):
        return settings.COS_BASE_URI + name

    # return data struct:
    # {'Content-Type': 'image/png', 'Content-Length': '132973', 'Connection': 'keep-alive',
    # 'Date': 'Mon, 26 Jul 2021 07:14:07 GMT', 'ETag': '"d9d11dc01f0fed2fb8788ee247130e99"',
    # 'Last-Modified': 'Mon, 26 Jul 2021 07:13:19 GMT', 'Server': 'tencent-cos',
    # 'x-cos-hash-crc64ecma': '3957965839468282517', 'x-cos-request-id': 'NjBmZTYwYmZfMmM5ZDA4MDlfMTVhZl83Y2U1NjBk'}
    def _info(self, name):
        try:
            response = self.client.head_object(
                Bucket=self.bucket,
                Key=name
            )
            return response
        except CosServiceError:
            return None


