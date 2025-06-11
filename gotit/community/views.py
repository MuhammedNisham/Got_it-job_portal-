from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def communityView(request):
    if request.method == "POST":
        content = request.POST.get("content")
        image = request.FILES.get("image")
        if content or image:
            Message.objects.create(sender=request.user, content=content, image = image if image else None)
            return redirect("communitypage")

    messages = Message.objects.order_by("timestamp")
    return render(request, "community.html", {"messages": messages})

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def deleteMessage(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return redirect('communitypage')