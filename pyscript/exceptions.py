class CommandException(Exception):
    """Root exception class"""


class TimeoutException(CommandException):
    """Indicates that the command execution timed out"""


class IllegalStateException(CommandException):
    """Indicates that an object is in an illegal state to process"""


class InternalError(CommandException):
    """Indicates that an InternalError occurred. This could happen for example if the server response is invalid."""
