#!/usr/bin/env python
import requests

from terminal import *


requests.packages.urllib3.disable_warnings()

logging.basicConfig(filename='terminal.log', level=logging.DEBUG)

"""
    Sample usage :
    session = pyscript.open("https://localhost:8443")
    response = session.terminal().execute("list rootca")
    for line in response.get_output():
        print line
    app.close(session)
"""


def open(url):
    """
    Opens a connection towards the Server.

    The connection should be closed using close() if it is not required anymore.

    :param url:                 url of the deployment

    :raise: ValueError if username or password is invalid
            requests.exceptions.ConnectionError if there is an issue with the connection

    :return:                    PySession
    """
    logging.info('opening session: ' + url )

    session = PySession(url)
    session._open_session()

    logging.info('session is open: ' + url + ' ' + str(session))
    return session


def close(py_session):
    """
    Closes the session to free the underling resources
    :param PySession:    PySession instance to be closed. This will terminate the Session contained
                          in this instance
    :return:              boolean, true if successfully closed
    """
    logging.info('closing session: ' + str(py_session))

    py_session._close_session()

    logging.info('session is closed: ' + str(py_session))


class PySession():
    """
    This class holds a session to a running deployment
    """
    _se_login_headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                         'Content-Type': 'application/x-www-form-urlencoded'}

    def __init__(self, url):
        self._url = url
        self._session = requests.Session()
        self._terminal = PyTerminal(self._url, self._session)

    def terminal(self):
        """
        Returns an instance of Terminal
        """
        return self._terminal

    # Private methods from module's perspective
    def _open_session(self):
        """
        Opens a session towards Server.

        :param url:             url of the deployment

        """
        logging.debug('Opening session: ' + str(self))

        logging.debug('Session opened: ' + str(self))

        return True

    def _close_session(self):
        logging.debug('Closing session: ' + str(self))
        logging.debug('Session is closed: ' + str(self))
