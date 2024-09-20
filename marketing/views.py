from django.shortcuts import render,redirect
import time
from .forms import NewjobForm
from marketing.models import Subscription,New_Project,Open_posts,Payment,OrderUpdate
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
from instamojo_wrapper import Instamojo
from django.conf import settings
api = Instamojo(api_key=settings.API_KEY,
                auth_token=settings.AUTH_TOKEN, endpoint= 'https://www.instamojo.com/api/1.1/')

def contacts(request):

  open_posts = Open_posts.objects.all().values()
  posts = Open_posts.objects.all()
  form = NewjobForm(request.POST, request.FILES or None)
  context = {
    'posts' : posts,
    'open_posts' : open_posts,
    'form': form,
  }
  
  if request.method == 'POST':
    if 'collect_slide' in request.POST:
      name = request.POST.get('name')
      email_id = request.POST.get('email_id')
      company = request.POST.get('company')
      phone_lead = request.POST.get('phone_lead')
      budget_min = request.POST.get('budget_min')
      budget_max = request.POST.get('budget_max')
      proj_details = request.POST.get('proj_details')
      New_Project.objects.create(name=name,email_id=email_id,company=company,phone_lead=phone_lead,budget_min=budget_min,budget_max=budget_max,proj_details=proj_details)
      messages.success(request, "Thanks for the enuiry, we'll contact you in next 24 hours!")
      return HttpResponseRedirect('https://biz499.com/contacts')

    elif 'payment' in request.POST:
      name = request.POST.get('name')
      email_id_pay = request.POST.get('email_id_pay')
      proj_details = request.POST.get('proj_details')
      phone = request.POST.get('phone')
      #service = request.POST.get('service')
      amount = request.POST.get('amount')
      order = Payment.objects.create(name=name,email_id_pay=email_id_pay,proj_details=proj_details,amount=amount,phone=phone)
      order.save()

      id = order.order_id

      # messages.success(request, "Thankyou for clearing your payment,our project manager shall get to you soon! ")
      param_dict = {

                'MID': 'Pufksy81577218609508',
                'ORDER_ID': str(id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email_id_pay,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'https:biz499.com/handlerequest/',

        }
      param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
      return render(request, 'paytm.html', {'param_dict': param_dict})
          
    elif 'email_sub' in request.POST:
      email = request.POST['email']
      subscriber = Subscription()
      subscriber.email = email
      subscriber.save()
      messages.success(request, "You have successfully subscribed to our mailing list")

    
    
    elif 'job_application' in request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been successfully sent")
        else:            
          messages.error(request, "Please fill the form correctly")

  return render(request,'contacts.html',context)

# @csrf_exempt
def paybutton(request):
    return render(request,'paybutton.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def termsandconditions(request):
    return render(request,'termsandconditions.html')

def cancellationpolicy(request):
    return render(request,'cancellationpolicy.html')

def developmentservice(request):         
        if request.method == 'POST' :
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          email_id_pay = request.POST.get('email_id_pay')
          phone = request.POST.get('phone')
          #service = request.POST.get('service')
          amount = request.POST.get('amount')

          purpose = request.POST.get('purpose')

          response = api.payment_request_create(
            amount = amount,
            purpose = purpose,
            buyer_name = first_name +" " + last_name,
            email = email_id_pay,
            phone = phone,
            redirect_url = 'https://www.biz499.com/ordersuccess/',
          )

          order_obj = Payment.objects.create(
            first_name=first_name,last_name=last_name,email_id_pay=email_id_pay,amount=amount,phone=phone,purpose=purpose,is_paid = False)

          order_obj.payment_id = response['payment_request']['id']
          order_obj.save()


          return render(request,'paybutton.html', context= {
            'payment_url' : response['payment_request'] ['longurl']
          })
        
        return render(request,'development_service_details.html')

def ordersuccess(request):
    payment_request_id = request.GET.get('payment_request_id')
    order_obj = Payment.objects.get(payment_id = payment_request_id)
    order_obj.is_paid = True
    order_obj.save()
    return HttpResponse("Success")

def adsservice(request):
        if request.method == 'POST' :
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          email_id_pay = request.POST.get('email_id_pay')
          phone = request.POST.get('phone')
          #service = request.POST.get('service')
          amount = request.POST.get('amount')

          purpose = request.POST.get('purpose')

          response = api.payment_request_create(
            amount = amount,
            purpose = purpose,
            buyer_name = first_name +" " + last_name,
            email = email_id_pay,
            phone = phone,
            redirect_url = 'https://www.biz499.com/ordersuccess/',
          )

          order_obj = Payment.objects.create(
            first_name=first_name,last_name=last_name,email_id_pay=email_id_pay,amount=amount,phone=phone,purpose=purpose,is_paid = False)

          order_obj.payment_id = response['payment_request']['id']
          order_obj.save()


          return render(request,'paybutton.html', context= {
            'payment_url' : response['payment_request'] ['longurl']
          })     
        return render(request,'ads_service_details.html')

def designservice(request):
        if request.method == 'POST' :
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          email_id_pay = request.POST.get('email_id_pay')
          phone = request.POST.get('phone')
          #service = request.POST.get('service')
          amount = request.POST.get('amount')

          purpose = request.POST.get('purpose')

          response = api.payment_request_create(
            amount = amount,
            purpose = purpose,
            buyer_name = first_name +" " + last_name,
            email = email_id_pay,
            phone = phone,
            redirect_url = 'https://www.biz499.com/ordersuccess/',
          )

          order_obj = Payment.objects.create(
            first_name=first_name,last_name=last_name,email_id_pay=email_id_pay,amount=amount,phone=phone,purpose=purpose,is_paid = False)

          order_obj.payment_id = response['payment_request']['id']
          order_obj.save()


          return render(request,'paybutton.html', context= {
            'payment_url' : response['payment_request'] ['longurl']
          })
        return render(request,'graphics_service_details.html')