from unittest2 import TestCase
from datetime import datetime
from http.date import Date
import time


class TestDate(TestCase):

    def test_time2str(self):
        str = Date.time2str(datetime(2011, 12, 12, 12, 0, 0))
        self.assertEqual(str, 'Mon, 12 Dec 2011 12:00:00 GMT')

    def test_str2time(self):
        time = Date.str2time('Mon, 12 Dec 2011 12:00:00 GMT')
        self.assertEqual(time.year, 2011)

    def test_str2epoch(self):
        epoch = Date.str2epoch('Mon, 12 Dec 2011 12:00:00 GMT')
        self.assertEqual(epoch, 1323720000)

    def test_epoch2time(self):
        time = Date.epoch2time(1323720000)
        self.assertEqual(time.year, 2011)
        pass

    def test_epoch2str(self):
        str = Date.epoch2str(1323720000)
        self.assertEqual(str, 'Mon, 12 Dec 2011 12:00:00 GMT')
