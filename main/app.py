import falcon
import json

from .resources import (
    RESTfulExample,
    APIInfo,
)

api = application = falcon.API()

# Addd route
api.add_route("/", APIInfo())
api.add_route("/restful", RESTfulExample())
