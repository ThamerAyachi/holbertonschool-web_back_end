#!/usr/bin/env python3
""" Basic Auth """

from api.v1.auth.auth import Auth
import re
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header Method"""

        if (base64_authorization_header is None or
                (type(base64_authorization_header) != str)):
            return None
        try:
            decodeBytes = base64.b64decode(base64_authorization_header)
            decodedStr = decodeBytes.decode("utf-8")
            return decodedStr
        except ValueError:
            return None
