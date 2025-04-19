"""Exception module."""


class ResumeException(Exception):
    """Generic resume exception"""


class ResumeParsingException(ResumeException):
    """Resume parsing exception"""


class ResumeProcessingException(ResumeException):
    """Resume processing exception"""
