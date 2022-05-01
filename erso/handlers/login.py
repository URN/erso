from os import environ as env
import jwt
from ldap3 import Connection
import ldap3.core.exceptions as ldap_exceptions

from .base import BaseHandler


class LoginHandler(BaseHandler):
    """Class to handle login requests."""

    def get(self):
        """Handles GET requests. Returns HTML for the login page."""
        self.write(
            self.loader.load("Login.html").generate(
                csrf_html=self.xsrf_form_html(), error=None
            )
        )

    def post(self):
        """Handles POST requests.
        Redirects to index (or last specified page) on success, but the form on failure."""
        username = self.get_argument("login")
        password = self.get_argument("password")
        try:
            conn = Connection(
                env["LDAP_SERVER"],
                f'uid={username},{env["LDAP_USER_BASE"]}',
                password,
                auto_bind=True,
            )
        except ldap_exceptions.LDAPException as error:
            # Login Failed, send them back to the login page with an error
            print(error)
            self.write(
                self.loader.load("Login.html").generate(
                    csrf_html=self.xsrf_form_html(), error=str(error)
                )
            )
            return

        # Find the User's Groups - Only search for the ones we care about
        groups = []
        for g in [env["LDAP_GROUP"]]:
            conn.search(
                search_base=f'uid={username},{env["LDAP_USER_BASE"]}',
                search_filter=f'(memberof=cn={g},{env["LDAP_GROUP_BASE"]})',
                attributes=["cn"],
            )
            if conn.entries:
                groups.append(g)

        if env["LDAP_GROUP"] not in groups:
            # User is not in the group we care about
            self.write(
                self.loader.load("Login.html").generate(
                    csrf_html=self.xsrf_form_html(),
                    error="You are not authorized to use this application.",
                )
            )
            return

        # Successful login, set the cookie and redirect to the index page
        token = jwt.encode(
            {"user": username, "groups": groups},
            env["SECRET_1"],
            algorithm="HS256",
        )
        self.set_secure_cookie("token", token)
        self.redirect(self.get_argument("next", "/"))
