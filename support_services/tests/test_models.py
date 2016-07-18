"""
A module that contains test cases for the models.
"""

from django.test import TestCase
from django.db import IntegrityError
from support_services.models import *

class ServiceTestCase(TestCase):
    def test_service_generate_slug(self):
        temp_service = Service()
        temp_service.name = 'A Temporary service'
        self.assertEqual(temp_service.generate_slug(), 'a-temporary-service')

    def test_str(self):
        temp_service = Service()
        temp_service.name = 'Another temporary Service'
        self.assertEqual(str(temp_service), 'Another Temporary Service')

    def test_save(self):
        temp_service = Service(name='A fine Ass day',
            description='It shall indeed be a fine ass day my good sir!')
        temp_service.slug = temp_service.generate_slug()
        temp_service.save()
        temp_service = Service.objects.get(slug='a-fine-ass-day')
        self.assertEqual(temp_service.name, 'a fine ass day')

    def test_name_uniqueness(self):
        temp_service_1 = Service(name='Temporary service one',
            description='The first temporary service', slug='temporary-service-one')
        temp_service_1.save()
        with self.assertRaises(IntegrityError):
            temp_service_2 = Service.objects.create(name='Temporary service one',
                description='A decoy service', slug='decoy-service')
                
    def test_slug_uniqueness(self):
        temp_service_1 = Service(name='Temporary service one',
            description='The first temporary service', slug='temporary-service-one')
        temp_service_1.save()
        with self.assertRaises(IntegrityError):
            temp_service_2 = Service.objects.create(name='Decoy Service',
                description='A decoy service', slug='temporary-service-one')
