from rest_framework import status
from rest_framework.exceptions import APIException
from django.conf import settings


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = settings.CONSTANTS.messages.BAD_REQUEST
    default_code = 'bad_request'


class ObjectAlreadyExist(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = settings.CONSTANTS.messages.OBJECT_ALREADY_EXIST
    default_code = 'object_already_exists'


class StudentInvalidYear(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = settings.CONSTANTS.messages.STUDENT_INVALID_YEAR
    default_code = 'year_invalid'


class StudentInActive(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = settings.CONSTANTS.messages.STUDENT_INACTIVE
    default_code = 'student_in_active'


class CustomError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = settings.CONSTANTS.messages.INVALID_INPUT
    code = 'invalid'

    def __init__(self, detail=None, status_code=None, code=None):
        if detail is not None:
            self.detail = detail
        if status_code is not None:
            self.status_code = status_code
        if code is not None:
            self.code = code
