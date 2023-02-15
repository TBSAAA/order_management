from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.conf import settings


class UserInfo(object):
    def __init__(self, user_id, user_type, name, level):
        self.id = user_id
        self.type = user_type
        self.name = name
        self.level = level


class Authority(MiddlewareMixin):
    def process_request(self, request):

        # 1. Access without login
        if request.path_info in settings.WHITE_LIST_URL:
            return

        # 2. Access with login
        user_dict = request.session.get(settings.ORDER_USER_SESSION)
        # 2.1 If not logged in, redirect to login page
        if not user_dict:
            return redirect(settings.LOGIN_URL)
        request.order_user = UserInfo(**user_dict)
        return None

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     pass
