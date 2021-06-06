import argparse
from django.core.management.base import BaseCommand
from flights.models import Flight
from datetime import datetime
import csv


class Command(BaseCommand):
    help = 'Loads flights data from csv file to database'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=argparse.FileType('r'), help='csv file with flights info')

    def handle(self, *args, **options):
        file = options['filename']
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            Flight.objects.get_or_create(
                origin=row[1],
                destination=row[2],
                departure_date=datetime.strptime(row[3], '%Y%m%d'),
                departure_time=datetime.strptime(row[4], '%H%M'),
                arrival_date=datetime.strptime(row[5], '%Y%m%d'),
                arrival_time=datetime.strptime(row[6], '%H%M'),
                number=row[7],
           )

