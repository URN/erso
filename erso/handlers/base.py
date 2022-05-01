from os import environ as env, path
import tornado.web
from tornado.template import Loader
import jwt


class BaseHandler(tornado.web.RequestHandler):
    """Base Handler."""

    def initialize(self):
        """Initialize the handler."""
        self.loader = Loader(f"{path.dirname(__file__)}/templates")

    def get_current_user(self):
        """Gets the current user from the cookie"""
        try:
            token = self.get_secure_cookie("token")
            data = jwt.decode(token, env["SECRET_1"], algorithms="HS256")
            return data["user"]
        except jwt.exceptions.InvalidTokenError as error:
            print(error)
        return None

    def get_groups(self):
        """Get groups for current user"""
        try:
            token = self.get_secure_cookie("token")
            data = jwt.decode(token, env["SECRET_1"], algorithms="HS256")
            return data["groups"]
        except jwt.exceptions.InvalidTokenError as error:
            print(error)
        return None
