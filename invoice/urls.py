from django.urls import path
from .views import *

urlpatterns = [
    path('items/', AllItems.as_view(), name='all_items'),
    path('list/', ListView.as_view(), name='list_view'),
    path('invoice/', InvoiceView.as_view(), name='invoice_view'),
]