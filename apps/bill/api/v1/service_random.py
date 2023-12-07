import random
from apps.bill.models import Bill


def get_random_bill(queryset):
    queryset = Bill.objects.filter("bill_number")
    bill_number_ids = list(queryset.values_list('id', flat=True))
    bill_number_ids = random.choices(bill_number_ids, k=8)
    random_bill = queryset.filter(bill_number=bill_number_ids)
    print("random", random_bill)
