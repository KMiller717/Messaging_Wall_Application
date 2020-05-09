from django.shortcuts import render, redirect
from login_app.models import User
from .models import Message, Comment
from django.contrib import messages
# Create your views here.

def wall_index(request):
    context = {
        'all_messages' : Message.objects.all(),
        'all_comments' : Comment.objects.order_by('created_at')
    }
    return render(request, 'wall_page.html', context)

def logout(request):
    return redirect('/')


def post_message(request):
    errors = Message.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')

    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.create(
        content= request.POST['message'],
        creator= user
    )
    return redirect('/wall')

def post_comment(request, message_id):
    errors = Comment.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')

    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    comment = Comment.objects.create(
        content = request.POST['comment'],
        message = message,
        user = user
    )
    return redirect('/wall')

def delete_comment(request, comment_id):
    comment_delete = Comment.objects.get(id=comment_id)
    comment_delete.delete()

    return redirect('/wall')

def edit_message(request, message_id):
    context = {
        'message' : Message.objects.get(id=message_id)
    }

    return render(request, 'message.html', context)