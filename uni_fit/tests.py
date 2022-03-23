from urllib import response
from django.test import TestCase
from uni_fit.models import University, University_Department
from django.urls import reverse


class UniversityMethodTests(TestCase):
    def test_value_in_university_rank(self):
        university = University(UniName='Massachusetts Institute of Technology', Country='US', UniRank=1, About='The Massachusetts Institute of Technology is a private land-grant research university in Cambridge, Massachusetts.', Link='https://web.mit.edu/')
        university.save()
        self.assertEqual(university.UniRank >0,True)

class UniversityDepartmentMethodTests(TestCase):
    def test_value_in_university_rank(self):
        university = University(UniName='Massachusetts Institute of Technology', Country='US', UniRank=1, About='The Massachusetts Institute of Technology is a private land-grant research university in Cambridge, Massachusetts.', Link='https://web.mit.edu/')
        university.save()
        universitydept = University_Department(UniName=University.objects.filter(pk=1).first(),DeptName='Engineering', DeptRank=1,Link='https://engineering.mit.edu/')
        universitydept.save()
        self.assertEqual(universitydept.DeptRank >0,True)

class FavUniversityNameCheck(TestCase):
    def test_fav_university_name(self):
        #Dummy Data
        university = University(UniName='Massachusetts Institute of Technology', Country='US', UniRank=1, About='The Massachusetts Institute of Technology is a private land-grant research university in Cambridge, Massachusetts.', Link='https://web.mit.edu/')
        university.save()
        universitydept = University_Department(UniName=University.objects.filter(pk=1).first(),DeptName='Engineering', DeptRank=1,Link='https://engineering.mit.edu/')
        universitydept.save()
        response = self.client.get(reverse('uni_fit:index'))
        self.assertEqual(response.status_code, 200)




