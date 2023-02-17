from django.template import Library
from django.conf import settings
import copy


register = Library()


@register.inclusion_tag("tag/menu.html")
def dynamic_menu(request):
    print(request.order_user.type)
    user_menu_list = copy.deepcopy(settings.MENU_LIST[request.order_user.type])

    # for item in user_menu_list:
    #     for child in item['children']:
    #         # if child['url'] == request.path_info: # v1版
    #         if child['name'] == request.order_user.menu_name:
    #             child['class'] = 'choice'
    #             # item['class'] = ""

    return {'menu_list': user_menu_list}


@register.inclusion_tag("tag/breadcrumb.html")
def dynamic_breadcrumb(request):
    breadcrumb_list = request.order_user.breadcrumb_list
    return {'breadcrumb_list': breadcrumb_list}