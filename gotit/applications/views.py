from django.shortcuts import render, redirect, get_object_or_404
from jobs.models import Job
from .forms import ApplicationForm
from .models import Application
from mainapp.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def applyView(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            profile = UserProfile.objects.get(user_name=request.user.username)
            application.resume = profile.resume
            application.save()
            messages.success(request, "Job applied successfully! You can check details on activity")  
            return redirect('jobpage')
    else:
        form = ApplicationForm()
    return render(request, 'apply.html', {'form': form, 'job': job})


@login_required
def activityView(request):
    user_applications = Application.objects.filter(user=request.user).select_related('job')
    return render(request, 'activity.html', {'applications': user_applications})

def appliedView(request):
    user_applications = Application.objects.filter(user=request.user).select_related('job')
    return render(request, 'applied.html', {'applications': user_applications})