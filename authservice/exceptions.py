from rest_framework.exceptions import APIException,ValidationError
from rest_framework import status

class ExceptionCodes:
    USER_NOT_PRESENT = "AUTH001"


class UserNotPresentException(APIException):
    def __init__(self, message='User not found.'):
        super(UserNotPresentException, self).__init__(message, ExceptionCodes.USER_NOT_PRESENT)

class RestValidationError(ValidationError):
    def __init__(self, msg = "Unauthorized",status=status.HTTP_401_UNAUTHORIZED):
        super().__init__(detail={"error":msg}, code=status)