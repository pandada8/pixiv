import requests
import uuid

class PixivAPI(object):

    """ Based on android api """

    def __init__(self):

        self.r = requests.session()
        self.r.headers["User-Agent"] = "PixivAndroidApp/5.0 10 (Android 6.0.1; Mi-4c)"
        self.r.headers["Accept-Language"] = "zh_CN"
        self.r.headers["App-OS"] = "android"
        self.r.headers["App-OS-Version"] = "6.0.1"
        self.r.headers["App-Version"] = "5.0.10"



    def auth(self, username, password):
        data = {
            "client_id": "BVO2E8vAAikgUBW8FYpi6amXOjQj",
            "client_secret": "LI1WsFUDrrquaINOdarrJclCrkTtc3eojCOswlog",
            "grant_type": "password",
            "username": username,
            "password": password,
            # "device_token": uuid.uuid4().hex,  # could be omited
            "get_secure_url": True
        }
        ret = self.r.post("https://oauth.secure.pixiv.net/auth/token", data=data).json()
        self.r.headers["Authorization"] = ret["response"]["token_type"] + " "  + ret["response"]["access_token"]
        self.user = ret["response"]["user"]

    def refresh_token(self):
        pass

    def get_recommand(self):
        data = {
            "content_type": 'illust',
            "include_ranking": 'true'
        }
        return self.r.get("https://app-api.pixiv.net/v1/illust/recommand", params=data).json()

    def add_bookmark(self, illust_id, restrict="public"):
        return self.r.post("https://app-api.pixiv.net/v1/illust/bookmark/add/", data={"illust_id": illust_id, "restrict": restrict}).json()

    def get_bookmark(self, restrict="public"):
        return self.r.get("https://app-api.pixiv.net/v1/user/bookmarks/illust", params=dict(user_id=self.user['id'], restrict=restrict)).json()
