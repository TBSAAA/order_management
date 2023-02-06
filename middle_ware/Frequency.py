import django_redis
from django_redis import get_redis_connection
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse, HttpResponse


# 所有网页的访问频率
class VisitorFrequency(MiddlewareMixin):
    def process_request(self, request):
        # 1. 获取当前用户的ip
        ip = request.META.get('REMOTE_ADDR')
        conn = get_redis_connection('default')

        count = conn.get(ip)
        if count:
            if count < 10:
                conn.incr(ip)
            else:
                return JsonResponse({'status': False, 'msg': '访问频率过高'})
        else:
            conn.set(ip, 1, ex=60)

    def process_response(self, request, response):
        return response


# 短信接口的访问频率
class SmsFrequency(MiddlewareMixin):
    def process_request(self, request):
        # 获取url
        url = request.path_info
        if url == '/get_code/':
            # 1. 获取当前用户的ip
            ip = request.META.get('REMOTE_ADDR')
            conn = get_redis_connection('default')

            count = conn.get(ip)
            if count:
                return JsonResponse({'status': False, 'msg': '访问频率过高'})
            else:
                conn.set(ip, 1, ex=60)

    def process_response(self, request, response):
        return response
