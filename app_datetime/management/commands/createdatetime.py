from django.core.management.base import BaseCommand
from app_datetime.models import DateTimeRecord
from datetime import datetime
import pytz
from django.utils.translation import gettext as _


class Command(BaseCommand):
    help = 'Create 100 PST Date/Time'

    def handle(self, *args, **options):
        timezone = pytz.timezone('US/Pacific')
        pst_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')

        # create 100 date/time.
        for i in range(100):
            DateTimeRecord.objects.create(datetime=pst_time, isUTC=False)

        self.stdout.write(self.style.SUCCESS(_("100 PST Date/Time created.")))
