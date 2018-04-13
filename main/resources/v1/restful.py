"""RESTful API example."""

__all__ = ["RESTfulExample"]


class RESTfulExample:

    def on_get(self, req, resp):
        # Do Something.
        resp.body = f"{req.method}"

    def on_post(self, req, resp):
        # Do Something.
        resp.body = f"{req.method}"

    def on_delete(self, req, resp):
        # Do Something.
        resp.body = f"{req.method}"

    def on_put(self, req, resp):
        # Do Something.
        resp.body = f"{req.method}"

    def on_patch(self, req, resp):
        # Do Something.
        resp.body = f"{req.method}"

