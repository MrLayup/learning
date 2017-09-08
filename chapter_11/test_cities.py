import unittest
from city_functions import get_city

class CitiesTestCase(unittest.TestCase):
	"""Test for city_sunctions"""
	
	def test_city_country(self):
		"""Fuuuck"""
		country_city = get_city('russia','moscow')
		self.assertEqual(country_city, 'Russia Moscow')
	def test_city_country_pouplation(self):
		country_city = get_city('russia','moscow','100500')
		self.assertEqual(country_city, 'Russia Moscow 100500')
unittest.main()
