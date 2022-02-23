from django.shortcuts import redirect, render
from django.views import View
from .forms import RegisterAccountForm , LoginAccountForm
from django.contrib.auth.models import User 
from django.contrib.auth import login , authenticate  , logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Post
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class RegisterAccountView(View):
    form_class = RegisterAccountForm
    template_name = 'account/register.html'

    def dispatch(self, request , *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

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
    
class UserLoginView(View):
    form_class = LoginAccountForm
    template_name = 'account/login.html'

    def dispatch(self, request , *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)


    def get(self , request):
        form = self.form_class
        return render(request , self.template_name  , {'form': form })

    def post(self , request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username = cd['username'] , password = cd['password'])
            if user is not None:
                login(request , user)
                messages.success(request , 'you loged in successfully' , 'success')
                return redirect('home:home')
            messages.error(request , 'username and password is wrong', 'warning')
        return render(request , self.template_name , {'form': form})

class UserLogoutView(LoginRequiredMixin , View):
    # login_url ='/login_account/'
    def get(self , request):
        logout(request)
        messages.success(request , 'you are logouted successfully' , 'success')
        return redirect('home:home')

class UserProfileView(LoginRequiredMixin, View):
    def get(sel ,request):
        posts = Post.objects.filter(user = request.user)
        return render(request  , 'account/profile.html', {'posts':posts})


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'account/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'account/password_reset_email.html'