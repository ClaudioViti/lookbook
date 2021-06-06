from django.shortcuts import render
from .forms import SignupForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)
        

        if form.is_valid():
            form.save()
            return redirect('signup_sent')

   
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def signup_sent_view(request):
    return render(request, 'signup_sent.html')