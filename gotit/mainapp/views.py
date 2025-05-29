from django.shortcuts import render, redirect

from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.

def homeView(request):
    template = loader.get_template('home.html')

    context = {
    }
    return HttpResponse(template.render(context, request))

@login_required
def ProfileView(request):
    profile, created = UserProfile.objects.get_or_create(user_name=request.user.username,)
    if created:
        return redirect('edit_profile')
    return render(request, 'profile.html', {'profile': profile})
    

def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user_name=request.user.username)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profilepage')  
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form, 'profile': profile})

