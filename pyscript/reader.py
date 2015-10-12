import ssl
from OpenSSL import crypto

class Reader:

    """
    This class ssl cert of the server
    """
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def get_server_cert(self):
        cert = ssl.get_server_certificate((self._host, self._port))
        x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
        return x509
