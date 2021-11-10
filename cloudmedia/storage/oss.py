from django.core.files.storage import Storage
from django.conf import settings
import logging
import oss2

logger = logging.getLogger(__name__)


class AliOSSStorage(Storage):
    def __init__(self):
        self.access_key_id = settings.OSS_ACCESS_KEY_ID
        self.access_key_secret = settings.OSS_ACCESS_KEY_SECRET
        self.endpoint = settings.OSS_END_POINT
        self.bucket = settings.OSS_BUCKET
        auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        self.client = oss2.Bucket(auth, self.endpoint, self.bucket)

    def _open(self, name, mode='rb'):
        result = self.client.get_object(name).read()
        return result

    def _save(self, name, content):
        self.client.put_object(name, content)
        return name

    def delete(self, name):
        self.client.delete_object(name)

    def exists(self, name):
        return self.client.object_exists(name)

    def listdir(self, path):
        pass

    def size(self, name):
        result = self.client.get_object_meta(name)
        return result.content_length

    def url(self, name):
        return settings.OSS_BASE_URI + name

    def get_accessed_time(self, name):
        pass

    def get_created_time(self, name):
        pass

    def get_modified_time(self, name):
        result = self.client.get_object_meta(name)
        return result.last_modified

    def path(self, name):
        return settings.OSS_BASE_URI + name


