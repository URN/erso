from .base import BaseHandler


class LogoutHandler(BaseHandler):
    """Handles Logout Requests."""

    def get(self):
        """Clears the cookie and redirects to the index page."""
        self.clear_cookie("token")
        self.redirect("/")
