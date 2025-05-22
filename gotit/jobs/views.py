from django.shortcuts import render, redirect
from .models import Job
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import JobForm


# Create your views here.
# @login_required
def jobView(request):
    jobs = Job.objects.all()
    selected_id = request.GET.get('selected')
    selected_job = None
    if selected_id:
        selected_job = Job.objects.filter(id=selected_id).first()
    elif jobs.exists():
        selected_job = jobs.first()
    context = {
        'jobs': jobs,
        'selected_job': selected_job,
    }
    return render(request, 'jobs.html', context)

@login_required
def addJobView(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobpage')  
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

@login_required
def editJobView(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobpage')  
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form': form})

@login_required
def deleteJobView(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == "POST":
        job.delete()
        return redirect('jobpage')
    return redirect('jobpage')
