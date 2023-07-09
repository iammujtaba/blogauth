from rest_framework.exceptions import APIException

class ExceptionCodes:
    USER_NOT_PRESENT = "AUTH001"


class UserNotPresentException(APIException):
    def __init__(self, message='User not found.'):
        super(UserNotPresentException, self).__init__(message, ExceptionCodes.USER_NOT_PRESENT)