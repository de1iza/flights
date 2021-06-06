from django.db import models


class Flight(models.Model):
    """
    Model to register flights
    """
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    number = models.CharField(max_length=20)

    def get_info(self):
        """
        Returns flight info to display
        :return: dictionary
        """
        return {
            'Number': self.number,
            'DepartureTime': self.departure_time,
            'ArrivalTime': self.arrival_time
        }
