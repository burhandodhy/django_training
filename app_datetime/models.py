from django.db import models
from django.utils.translation import gettext as _


class DateTime(models.Model):
  datetime = models.DateTimeField(_("Date Time"))
  isUTC = models.BooleanField(_("Is UTC Time"), default=False)
