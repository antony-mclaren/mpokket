from django.urls import path
from .views import RequestEMILoanAPIView

urlpatterns = [
    path('request_emi_loan/', RequestEMILoanAPIView.as_view(), name='request_emi_loan'),
]