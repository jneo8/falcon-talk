import json
import falcon
from neologger import Logger

logger = Logger(__name__)


__all__ = ["APIInfo"]

class APIInfo:

    def on_get(self, req, resp):
        """GET Method."""
        doc = {
            "version": "1.0",
            "http_method": req.method,
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        """POST Method."""
        doc = {
            "version": "1.0",
            "http_method": req.method,
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

