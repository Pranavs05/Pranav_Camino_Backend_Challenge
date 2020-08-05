from django.test import TestCase
from rest_framework.test import APITestCase
from loans.models import Requests
from  loans.models import Address
from  loans.models import Owners
from  loans.models import Business
from django.urls import reverse
from rest_framework import status
import json 
import os ,sys

class RegistrationTestCase(APITestCase):


    
    def test_status(self):
        
        response= self.client.get(reverse('status'))  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_application(self):
       
        v=os.getcwd()
        v=v+'/sample.json'
        with open (v) as myfile:
            data=myfile.read()
        response = self.client.post('loanapp',data,format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)