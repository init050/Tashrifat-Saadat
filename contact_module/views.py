from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import View
from .forms import ContactUsModelForm
from .models import Contact



class ContactUsView(View):


    def get(self, request):
        form = ContactUsModelForm()
        return render(request, 'contact_module/contact_page.html', context={
            'form':form,
        })
        

    def post(self, request):
        form = ContactUsModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد')
            return redirect('home_page')
        
        return render(request, 'contact_module/contact_page.html',context={
            'form':form,
        })
        