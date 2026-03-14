from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm

# Create your views here.

@login_required
def inbox(request):
    messages_list = Message.objects.filter(receiver=request.user).order_by('-date_sent')
    return render(request, 'messaging/inbox.html', {'messages': messages_list})

@login_required
def sent_messages(request):
    messages_list = Message.objects.filter(sender=request.user).order_by('-date_sent')
    return render(request, 'messaging/sent.html', {'messages': messages_list})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Message sent successfully.')
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form})

@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk, receiver=request.user)
    if not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'messaging/message_detail.html', {'message': message})
