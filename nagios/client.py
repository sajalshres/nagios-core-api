from .rest_client import RestClient
from .cgi import ArchiveJsonCgi, ObjectJsonCgi, StatusJsonCgi


class Nagios:
    def __init__(self, url, username, password) -> None:
        self.rest_client = RestClient(url, username, password)
        self.archive_json_cgi = ArchiveJsonCgi(rest_client=self.rest_client)
        self.object_json_cgi = ObjectJsonCgi(rest_client=self.rest_client)
        self.status_json_cgi = StatusJsonCgi(rest_client=self.rest_client)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    def close(self):
        self.rest_client._close_session()
