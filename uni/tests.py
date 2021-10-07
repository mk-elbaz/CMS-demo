from django.test import TestCase
from .models import *

# Create your tests here.
class AverageTestCase(TestCase):

    def setUp(self):

        # Create Users.
        a1 = User.objects.create(username="AAA", role="a")
        a3 = User.objects.create(username="BBB", role="a")
        a2 = User.objects.create(username="TTT", role="b")

        # Create rating.
        a = Rating.objects.create(rate=4, tutor=a2)
        b = Rating.objects.create(rate=5, tutor=a2)
        c = Rating.objects.create(rate=3, tutor=a2)
        d = Rating.objects.create(rate=3, tutor=a2)
        e = Rating.objects.create(rate=5, tutor=a2)
        a.student.add(a1)
        b.student.add(a1)
        c.student.add(a1)
        d.student.add(a3)
        e.student.add(a3)

    def testAverageRating(self):
        a = User.objects.get(username="TTT")
        self.assertEqual(a.getRate(), 4)