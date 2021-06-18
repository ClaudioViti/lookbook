from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from django.shortcuts import redirect

UserModel = get_user_model()
from .forms import SignupForm, UserUpdateForm, UserFromMailForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

from django.views.generic.edit import UpdateView
class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name_suffix = '_update_form'  # if template is like user_update_form.html
    # template_name  # or provide custom name
  
    # if we need it in future


    
    def form_valid(self, form):

        if 'email' in form.changed_data:
            # current_email = self.object.email
            current_email = self.model.objects.get(pk=self.object.pk).email
            new_email = form.cleaned_data['email']
            print(f"'{new_email}' - '{current_email}' {current_email is new_email}")
            self.object = form.save(commit=False)
            self.object.email = current_email
            self.object.save()
            self.object.refresh_from_db() # debug remove later
            print(f"Email in db: {self.object.email}")
            # <email sending code>
            # store new_mail somewhere
            
            self.request.session['new_email'] = new_email
            current_site = get_current_site(self.request)
            mail_subject = 'Change your email.'
            message = render_to_string('acc_change.html', {
                'user': self.object,
                'domain': current_site.domain,
            
                'token': default_token_generator.make_token(self.object),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect(self.get_success_url())
        else:
            return super().form_valid(form)

                

    def get_object(self):
        return self.request.user
    def get_success_url(self):
        return reverse('manage')


def confirm_mail_change(request, token):
    user = request.user
    print(request.session)
    print(request.session.items())
    new_email = request.session.get('new_email')
    if new_email:
        if user.is_active and default_token_generator.check_token(user, token):
            user.email = new_email
            try:
                user.full_clean()
            except Exception as ex:
                # handle validation issue (e.g. email is not unique anymore)
                print(f"{ex}")
                return HttpResponse('Validation failed!')
            else:
                user.save()
                return HttpResponse(f'Thank you for your email confirmation. Email set as "{new_email}"')
        else:
            return HttpResponse('Confirmation link is invalid or your account is not yet activated!')
    else:
        return HttpResponse("Email is not found in session, please open this link in same browser you've used to request change.")

def UsernameFromMailView(request):

    if request.method == 'POST':
        form = UserFromMailForm(request.POST)
     
        if form.is_valid():

            to_email = form.cleaned_data.get('email')
            user = UserModel._default_manager.get(email=to_email)
            mail_subject = 'Your username.'
            message = render_to_string('username_email.html', {

                'user': user,
                
 
            })

           
            user.email_user(mail_subject, message, from_email=None)

    
    else:
        form = UserFromMailForm()

    return render(request, 'username_from_email.html', {'form': form})