class BaseResponse(object):
    def __init__(self, success=False, code=None, data=None, message=None):
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    @property
    def dict(self):
        return self.__dict__
