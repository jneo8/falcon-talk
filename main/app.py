"""App."""
import falcon
import json

from neologger import Logger
from .resources import v1

logger = Logger(__name__)


class AddPostParams():
    """Get Params from stream & set to params."""

    def process_request(self, req, resp):
        """Process_request."""
        body = req.stream.read()
        post_params = json.loads(body.decode("utf-8"))
        for k, v in post_params.items():
            req.params[k] = v


class VersionRouting:
    """Version control."""

    def process_request(self, req, resp):
        """Process_request."""
        version = req.get_header("version", None)
        if version:
            req.path = f"/v{version}{req.path}"
            if req.path[-1] == "/":
                req.path = req.path[:-1]


api = application = falcon.API(
    middleware=[
        AddPostParams(),
        VersionRouting(),
    ]
)


# Addd route
api.add_route("/", v1.APIInfo())
api.add_route("/restful", v1.RESTfulExample())


api.add_route("/v1", v1.APIInfo())
api.add_route("/v1/restful", v1.RESTfulExample())
