#!/usr/bin/env python3
""" Hashing Password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashing Password Function """
    _bytes = password.encode('utf-8')
    slat = bcrypt.gensalt()
    hash = bcrypt.hashpw(_bytes, slat)
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check Password """
    _bytes = password.encode('utf-8')
    return bcrypt.checkpw(_bytes, hashed_password)
