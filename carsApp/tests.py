from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Cars


# Create your tests here.

class CarsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_Cars = Cars.objects.create(name='flower', owner=testuser1, desc="test desc ...")
        test_Cars.save()

    def thigs_model(self):
        Cars = Cars.objects.get(id=1)
        actual_owner= str(Cars.owner)
        actual_name = str(Cars.name)
        actual_desc = str(Cars.desc)
        self.assertEqual(actual_owner,"testuser1")
        self.assertEqual(actual_name,"flower")
        self.assertEqual(actual_desc,"test desc ...")