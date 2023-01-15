from customers.models import Customer
from customers.serializers import CustomerSerializer
from django.http import JsonResponse

def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data,many=True)
    return JsonResponse({'customers':serializer.data})