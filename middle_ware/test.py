# 获取当前访问者的ip
ip = request.META.get("REMOTE_ADDR")
print(ip)

# 获取当前访问者的浏览器类型
user_agent = request.META.get("HTTP_USER_AGENT")
print(user_agent)

# 把获取到的信息存入redis
conn = get_redis_connection("default")
# conn.set("ip", ip, ex=6)
if conn.get("ip"):
    print("ip已经存在")