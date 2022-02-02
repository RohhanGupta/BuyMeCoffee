from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

from bymecoffee.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def landing(request):
    if request.method == 'POST':
        DATA=dict(order_ammount = 50000,
        order_currency = 'INR',
        payment_capture = '1')
        client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
        payment = client.order.create(data=DATA)
    return render(request, 'landing.html')

def success(request):
    return render(request, 'success.html')