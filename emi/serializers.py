from unittest import addModuleCleanup
from pkg_resources import load_entry_point
from rest_framework import serializers
from .models import DemoModel

class RequestEMILoanSerializer(serializers.ModelSerializer):
    output = serializers.BooleanField(default = False)
    approve_loan = serializers.BooleanField(default = False)
    user_id = serializers.UUIDField()
    amount = serializers.IntegerField()
    tenure = serializers.IntegerField()
    loan_type = serializers.CharField(min_length=1)
    bank_account_id = serializers.CharField(min_length=1)

    class Meta:
        model = DemoModel
        # fields = '__all__'
        exclude = ['id']