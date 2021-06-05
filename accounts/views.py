from django.shortcuts import render
from .forms import SignupForm
from django.http import HttpResponseRedirect

# Create your views here.

def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)
        

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

   
    else:
        form = SignupForm()


  

    return render(request, 'signup.html', {'form': form})

