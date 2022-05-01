"""Runs the Erso application."""

from os import environ as env
from tornado.ioloop import IOLoop
from tornado.web import Application
from erso import handlers


def main():
    """Runs the Tarkin application."""
    app_settings = {
        "login_url": "/login",
        "xsrf_cookies": True,
        "cookie_secret": env["SECRET_2"],
    }

    app = Application(
        [
            ("/login", handlers.LoginHandler),
            ("/logout", handlers.LogoutHandler),
            (r"/(.*)", handlers.AuthedStaticHandler, {"path": env["INPUT_DIR"]}),
        ],
        **app_settings
    )
    app.listen(8888)
    IOLoop.current().start()


if __name__ == "__main__":
    main()
