from re import I
from django import views
from django.shortcuts import redirect, render
from django.views import View
from .forms import RegisterAccountForm
from django.contrib.auth.models import User
from django.contrib import messages


class RegisterAccountView(View):
    form_class = RegisterAccountForm
    template_name = 'account/register.html'

    def get(self ,request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form } )
      
    def post(self , request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password_1'] and cd['password_2'] and cd['password_1'] != cd['password_2']:
                messages.error(request, 'passwords is not match!' , 'danger')
                return redirect('account:register_account')
            
            user = User.objects.create_user(cd['username'] , cd['email'] , cd['password_2'])
            messages.success(request, 'you registered successfully' , extra_tags= 'success')
            return redirect('home:home')
            

        return render(request, self.template_name, {'form' : form } ) 
        


