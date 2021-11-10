from django.core.files.storage import Storage
from django.conf import settings
import logging
from obs import ObsClient

logger = logging.getLogger(__name__)


class OBSStorage(Storage):
    def __init__(self):
        self.access_key_id = settings.OBS_ACCESS_KEY_ID
        self.access_key_secret = settings.OBS_ACCESS_KEY_SECRET
        self.endpoint = settings.OBS_END_POINT
        self.bucket = settings.OBS_BUCKET
        self.client = ObsClient(
            access_key_id=self.access_key_id,
            secret_access_key=self.access_key_secret,
            server=self.endpoint
        )

    def _open(self, name, mode='rb'):
        result = self.client.getObject(self.bucket, name, loadStreamInMemory=True)
        if result.status < 300:
            return result.body.buffer
        else:
            raise Exception(result.errorMessage)

    def _save(self, name, content):
        self.client.putContent(self.bucket, name, content)
        return name

    def delete(self, name):
        self.client.deleteObject(self.bucket, name)

    def exists(self, name):
        res = self._get_meta(name)
        if res is None:
            return False
        else:
            return True

    def listdir(self, path):
        pass

    def size(self, name):
        res = self._get_meta(name)
        if res is None:
            return 0
        else:
            return res.body.contentLength

    def url(self, name):
        return settings.OBS_BASE_URI + name

    def get_accessed_time(self, name):
        return self.get_modified_time(name)

    def get_created_time(self, name):
        return self.get_modified_time(name)

    def get_modified_time(self, name):
        res = self._get_meta(name)
        return res.body.lastModified

    def path(self, name):
        return settings.OBS_BASE_URI + name

    def _get_meta(self, name):
        res = self.client.getObjectMetadata(self.bucket, name)
        if res.status < 300:
            return res
        else:
            return None

