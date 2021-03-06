from django.core.management.base import BaseCommand
from app_datetime.models import DateTimeRecord
from datetime import datetime
import pytz
from django.utils.translation import gettext as _


class Command(BaseCommand):
    help = "Covert 10 PST Date/Time into UTC Date/Time"

    def handle(self, *args, **options):
        date_time = DateTimeRecord.objects.filter(isUTC=False)[:10]
        
        # IF PST time exist convert them into UTC. Else convert all UTC to PST.
        if date_time.exists():
            for obj in date_time:
                obj.datetime = obj.datetime.utcnow()
                obj.isUTC = True
                obj.save()
            
            self.stdout.write(self.style.SUCCESS(_("10 PST Date/Time converted into UTC Date/Time")))
        else:
            date_time = DateTimeRecord.objects.filter(isUTC=True)
            count = 0
            for obj in date_time:
                obj.datetime = obj.datetime.astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S')
                obj.isUTC = False
                obj.save()
                count += 1

            self.stdout.write(self.style.SUCCESS( _("%s UTC Time/Date converted in PST Date/Time" % count)))
                

        
