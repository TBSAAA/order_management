from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def img_standard(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(gettext_lazy('Image too large (max 2MB)'))
    if not value.name.endswith(('.jpg', '.png', '.jpeg')):
        raise ValidationError(gettext_lazy('Image must be .jpg, .png or .jpeg'))
