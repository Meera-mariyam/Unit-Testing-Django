from django.test import SimpleTestCase
from django.urls import reverse,resolve
from budget.views import *

class Testurls(SimpleTestCase):
    
    def test_list(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func,project_list)

    def test_add(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class,ProjectCreateView)

    def test_detail(self):
        url = reverse('detail',args=['slug'])
        self.assertEquals(resolve(url).func,project_detail)
