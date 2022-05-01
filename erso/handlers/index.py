from os import environ as env
import os
from .base import BaseHandler
from tornado.web import authenticated


class IndexHandler(BaseHandler):
    """Index Page Handler."""

    @authenticated
    def get(self):
        """Handles GET requests."""

        files = [
            f
            for f in os.listdir(env["INPUT_DIR"])
            if os.path.isfile(f'{env["INPUT_DIR"]}/{f}')
        ]

        self.write(
            self.loader.load("Index.html").generate(
                user=self.current_user,
                groups=self.get_groups() or [],
                env=env,
                files=files,
            )
        )
