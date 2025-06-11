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
    # --- Profile completeness check ---
    try:
        profile = UserProfile.objects.get(user_name=request.user.username)
        profile_is_complete = bool(profile.resume)  
    except UserProfile.DoesNotExist:
        profile_is_complete = False

    if not profile_is_complete:
        messages.warning(request, "Please update your profile before applying for a job.")
        return redirect('profilepage')  

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.resume = profile.resume
            application.save()
            messages.success(request, "Job applied successfully! You can check details on activity")  
            return redirect('jobpage')
    else:
        form = ApplicationForm()
    return render(request, 'apply.html', {'form': form, 'job': job})

@login_required
def activityView(request):
    if request.user.is_staff or request.user.is_superuser:
        # Admin or staff
        all_applications = Application.objects.select_related('job', 'user')
        return render(request, 'activity.html', {'applications': all_applications, 'show_user': True})
    else:
        # Regular user
        user_applications = Application.objects.filter(user=request.user).select_related('job')
        return render(request, 'activity.html', {'applications': user_applications, 'show_user': False})

def appliedView(request):
    user_applications = Application.objects.filter(user=request.user).select_related('job')
    return render(request, 'applied.html', {'applications': user_applications})