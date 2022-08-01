import copy
from urllib import response
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from mpokket.constants import RESPONSE_DATA_ERROR, RESPONSE_DATA_SUCCESS
from .serializers import (RequestEMILoanSerializer,)
# Create your views here.


class RequestEMILoanAPIView(generics.GenericAPIView):
    serializer_class = RequestEMILoanSerializer
    def post(self,request, *args, **kwargs):
        if request.data.get('output') and request.data.get('approve_loan'):
            response_data = copy.deepcopy(RESPONSE_DATA_SUCCESS)
            response_data['message'] = 'loan approved successfully'
            response_data['data'] = {
                'amount': request.data.get('amount'),
                'tenure' : request.data.get('tenure'),
                'bank_account_id' : request.data.get('bank_account_id')
            }
            return Response(response_data, status = status.HTTP_200_OK)
        if request.data.get('output'):
            response_data = copy.deepcopy(RESPONSE_DATA_SUCCESS)
            response_data['statusCode'] = status.HTTP_201_CREATED
            response_data['message'] = 'loan disbursal successful'
            return Response(response_data, status = status.HTTP_201_CREATED)
        else:
            response_data = copy.deepcopy(RESPONSE_DATA_ERROR)
            response_data['message'] = 'Given data was invalid'
            return Response(response_data, status = status.HTTP_400_BAD_REQUEST)