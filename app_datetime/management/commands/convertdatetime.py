from django.core.management.base import BaseCommand, CommandError
from app_datetime.models import DateTime
from datetime import datetime
import pytz
from django.utils.translation import gettext as _


class Command(BaseCommand):
    help = 'Covert 10 PST Date/Time into UTC Date/Time'

    def handle(self, *args, **options):
        dateTime = DateTime.objects.filter(isUTC=False)[:10]
        
        # IF PST time exist convert them into UTC. Else convert all UTC to PST.
        if dateTime.exists():
            for obj in dateTime:
                obj.datetime = obj.datetime.utcnow()
                obj.isUTC = True
                obj.save()
            
            self.stdout.write(self.style.SUCCESS(_("10 PST Date/Time converted into UTC Date/Time")))
        else:
            dateTime = DateTime.objects.filter(isUTC=True)
            for obj in dateTime:
                obj.datetime = obj.datetime.astimezone(pytz.timezone('US/Pacific')).strftime("%Y-%m-%d %H:%M:%S")
                obj.isUTC = False
                obj.save()
                
            self.stdout.write(self.style.SUCCESS( _("UTC Time/Date converted in PST Date/Time")))
                

        
