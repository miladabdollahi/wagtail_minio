import os
import sys


def create_otp(key, header=None, length=8, **options):
    """
    generates otp with given length and stores it with given key and header.

    :param str key: key value to be used for storing otp.
    :param str header: header value to be used for storing otp.
    :param int length: length of generated otp.

    :keyword int expire: number of seconds to expire the key.
                         defaults to None if not provided and
                         the key won't be expired.

    :rtype: str
    """

    otp = str(int.from_bytes(os.urandom(int(length / 2)), sys.byteorder))
    otp = otp[:length]
    if len(otp) < length:
        otp = otp.zfill(length)

    return otp
