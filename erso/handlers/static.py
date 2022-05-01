from os import environ as env
import os
import tornado.web
from tornado.template import Loader
import jwt

from .base import BaseHandler


class AuthedStaticHandler(BaseHandler):

    def initialize(self, path):
        """Initialize the handler."""
        self.root = path
        super().initialize()

    def get_current_user(self):
        """Gets the current user from the cookie"""
        try:
            token = self.get_secure_cookie("token")
            data = jwt.decode(token, env["SECRET_1"], algorithms="HS256")
            return data["user"]
        except jwt.exceptions.InvalidTokenError as error:
            print(error)
        return None

    @tornado.web.authenticated
    def get(self, p):
        """Get content of a file"""
        path = f'{self.root}/{p}'
        if os.path.isdir(path):
            files = [f for f in os.listdir(path) if os.path.isfile(f"{path}/{f}")]
            folders = [f for f in os.listdir(path) if os.path.isdir(f"{path}/{f}")]
            self.finish(self.loader.load("Index.html").generate(
                    files=files,
                    folders=folders,
                    p=f'{p}/' if p else '',
                ))
        elif os.path.isfile(path):
            with open(path, 'rb') as f:
                print(p)
                self.set_header("Content-Type", "application/octet-stream")
                self.set_header("Content-Disposition", f"attachment; filename={os.path.basename(p)}")
                self.write(f.read())
                self.finish()
        else:
            raise tornado.web.HTTPError(404)