import django_redis
from django_redis import get_redis_connection

conn = get_redis_connection("default")
conn.set("name", "jack", ex=6)
print(conn.get("name"))

