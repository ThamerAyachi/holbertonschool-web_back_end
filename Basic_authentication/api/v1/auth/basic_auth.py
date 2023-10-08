#!/usr/bin/env python3
""" Basic Auth """

from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """ Basic Auth Class"""

    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """extract_base64_authorization_header Method"""

        if authorization_header is None or (type(authorization_header) != str):
            return None
        if authorization_header.startswith("Basic ") is False:
            return None
        Base64 = re.split(' ', authorization_header)
        return Base64[1]
