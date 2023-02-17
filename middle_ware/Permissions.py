from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import JsonResponse


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

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 1. Accessible to everyone
        if request.path_info in settings.WHITE_LIST_URL:
            return

        # 2. Generate the name of the user's access address
        visit_name = request.resolver_match.url_name

        # 3. Check whether visit_name is in the public permissions
        if visit_name in settings.PUBLIC_PERMISSION:
            return

        # 4. Get all permissions of the current user
        permission_dict = settings.PERMISSION_LIST[request.order_user.type]

        # 5. Check whether the current user has access to the current address
        if visit_name not in permission_dict:
            # ajax request
            if request.is_ajax():
                return JsonResponse({'code': 500, 'data': {}, 'msg': 'No permission', "success": False})
            # normal request
            return render(request, 'permission.html')

        # 6. if have permission, get navagation list
        nav_list = []
        nav_list.append(permission_dict[visit_name]['title'])
