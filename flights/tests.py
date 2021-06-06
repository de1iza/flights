from django.core.management import call_command
from django.test import TestCase
from flights.models import Flight
import datetime


class CommandTest(TestCase):
    """Tests for load_flight command"""
    def setUp(self):
        args = ['../flights.csv']
        call_command('load_flights', *args)

    def test_count_records(self):
        """Checks if number of created records is correct"""
        self.assertEqual(Flight.objects.count(), 6)

    def test_records_info(self):
        """Checks if records contain valid data"""
        flight_1 = Flight.objects.get(pk=1)
        flight_3 = Flight.objects.get(pk=3)
        self.assertEqual(flight_1.departure_date, datetime.date(2021, 7, 1))
        self.assertEqual(flight_3.arrival_date, datetime.date(2021, 7, 4))


class FlightTest(TestCase):
    """Tests for Flight model"""
    def setUp(self):
        Flight.objects.create(origin='DME', destination='MUC',
                              departure_date=datetime.date(2021, 6, 7), departure_time=datetime.time(13, 45),
                              arrival_date=datetime.date(2021, 6, 7), arrival_time=datetime.time(16, 0),
                              number='S7 3555'
                              )
        Flight.objects.create(origin='CDG', destination='LTN',
                              departure_date=datetime.date(2021, 7, 3), departure_time=datetime.time(21, 55),
                              arrival_date=datetime.date(2021, 7, 3), arrival_time=datetime.time(23, 15),
                              number='U2 2442'
                              )
        self.flight_1 = Flight.objects.get(pk=1)
        self.flight_2 = Flight.objects.get(pk=2)

    def test_records(self):
        """Checks if records contain valid data"""
        self.assertEqual(Flight.objects.count(), 2)
        self.assertEqual(self.flight_1.origin, 'DME')
        self.assertEqual(self.flight_1.number, 'S7 3555')
        self.assertEqual(self.flight_1.departure_time, datetime.time(13, 45))
        self.assertEqual(self.flight_2.destination, 'LTN')
        self.assertEqual(self.flight_2.arrival_date, datetime.date(2021, 7, 3))
        self.assertEqual(self.flight_2.number, 'U2 2442')

    def test_get_info(self):
        """Checks get_info() method"""
        flight_1 = Flight.objects.get(pk=1)
        flight_2 = Flight.objects.get(pk=2)
        self.assertEqual(flight_1.get_info(), {'Number': 'S7 3555',
                                               'DepartureTime': datetime.time(13, 45),
                                               'ArrivalTime': datetime.time(16, 0)})
        self.assertEqual(flight_2.get_info(), {'Number': 'U2 2442',
                                               'DepartureTime': datetime.time(21, 55),
                                               'ArrivalTime': datetime.time(23, 15)})


class ViewTest(TestCase):
    """Test for view of /flights/<id>"""
    def setUp(self):
        Flight.objects.create(origin='DME', destination='MUC',
                              departure_date=datetime.date(2021, 7, 10), departure_time=datetime.time(1, 45),
                              arrival_date=datetime.date(2021, 7, 10), arrival_time=datetime.time(4, 0),
                              number='S7 3595'
                              )
        Flight.objects.create(origin='SVO', destination='CDG',
                              departure_date=datetime.date(2021, 7, 5), departure_time=datetime.time(19, 50),
                              arrival_date=datetime.date(2021, 7, 5), arrival_time=datetime.time(22, 30),
                              number='U2 1713'
                              )

    def test_view_existing_flights(self):
        """Checks if GET requests for existing flights returns valid data"""
        resp_1 = self.client.get('/flights/1')
        resp_2 = self.client.get('/flights/2')
        self.assertEqual(resp_1.status_code, 200)
        self.assertEqual(resp_2.status_code, 200)
        self.assertEqual(resp_1.content.decode('utf-8'), '{"Number": "S7 3595", "DepartureTime": "01:45:00", '
                                                         '"ArrivalTime": "04:00:00"}')
        self.assertEqual(resp_2.content.decode('utf-8'), '{"Number": "U2 1713", "DepartureTime": "19:50:00", '
                                                         '"ArrivalTime": "22:30:00"}')

    def test_view_not_existing_flights(self):
        """Checks if GET requests for not existing flights returns 404"""
        resp = self.client.get('/flights/10')
        self.assertEqual(resp.status_code, 404)
