from django.db import models
from django.core.validators import RegexValidator
from utils.validators import img_standard


class ActiveBaseModel(models.Model):
    active = models.SmallIntegerField(verbose_name="state", default=1, choices=((1, "active"), (0, "delete"),))

    # The database will not generate tables for abstract models
    class Meta:
        abstract = True


class Level(ActiveBaseModel):
    """ level table """
    title = models.CharField(verbose_name="title", max_length=32)
    percent = models.IntegerField(verbose_name="discount")


class User(ActiveBaseModel):
    """ customer table / Administrator table"""
    user_type = models.SmallIntegerField(verbose_name="user_type", default=2)
    username = models.CharField(verbose_name="user_name", max_length=32, db_index=True)
    password = models.CharField(verbose_name="password", max_length=32)
    mobile = models.CharField(verbose_name="phone_number", max_length=10, db_index=True, null=True, blank=True,
                              validators=[RegexValidator(r'^\d{10}$', 'Malformed phone number'), ], )
    balance = models.DecimalField(verbose_name="balance", default=0, max_digits=10, decimal_places=2)
    level = models.ForeignKey(verbose_name="level", to="Level", on_delete=models.CASCADE, default=1)
    avatar = models.FileField(verbose_name="avatar", null=True, default='avatar/default.jpg', upload_to='avatar', validators=[img_standard])
    create_date = models.DateTimeField(verbose_name="create_date", auto_now_add=True)


class PricePolicy(models.Model):
    """ Price Strategy table """
    count = models.IntegerField(verbose_name="count")
    price = models.DecimalField(verbose_name="price", default=0, max_digits=10, decimal_places=2)


class Order(ActiveBaseModel):
    """ Order table """
    status_choices = (
        (1, "pending"),
        (2, "is executing"),
        (3, "completed"),
        (4, "fail"),
    )
    status = models.SmallIntegerField(verbose_name="status", choices=status_choices, default=1)
    oid = models.CharField(verbose_name="order_id", max_length=64, unique=True)
    url = models.URLField(verbose_name="url", db_index=True)
    count = models.IntegerField(verbose_name="count")
    price = models.DecimalField(verbose_name="price", default=0, max_digits=10, decimal_places=2)
    real_price = models.DecimalField(verbose_name="real_price", default=0, max_digits=10, decimal_places=2)
    old_view_count = models.CharField(verbose_name="old_view_count", max_length=32, default="0")
    create_datetime = models.DateTimeField(verbose_name="create_datetime", auto_now_add=True)
    customer = models.ForeignKey(verbose_name="customer", to="User", on_delete=models.CASCADE)
    memo = models.TextField(verbose_name="notes", null=True, blank=True)


class TransactionRecord(ActiveBaseModel):
    """ Transaction Record table """
    charge_type_class_mapping = {
        1: "Success",
        2: "Danger",
        3: "Default",
        4: "Info",
        5: "Primary",
    }
    charge_type_choices = ((1, "Top up"), (2, "Debit"), (3, "Create Order"), (4, "Delete order"), (5, "Cancel"),)
    charge_type = models.SmallIntegerField(verbose_name="charge_type", choices=charge_type_choices)
    customer = models.ForeignKey(verbose_name="customer", to="User", on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name="amount", default=0, max_digits=10, decimal_places=2)
    order_oid = models.CharField(verbose_name="order_id", max_length=64, null=True, blank=True, db_index=True)
    create_datetime = models.DateTimeField(verbose_name="create_datetime", auto_now_add=True)
    memo = models.TextField(verbose_name="notes", null=True, blank=True)
