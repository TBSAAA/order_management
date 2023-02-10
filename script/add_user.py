# active django
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_management.settings')
django.setup()  # 伪fake to get django to start

from web import models
from utils.encrypt import md5

# add level
# level_object = models.Level.objects.create(title="test", percent=90)

models.User.objects.create(
    user_type=1,
    username='jack@qq.com',
    password=md5("jackjack"),
    mobile='0452509135',
    level_id=1,
)
