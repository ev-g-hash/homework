from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

def index(request):
    return render(request, 'journal/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}

    return render(request, 'journal/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'journal/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal:topics')
    context = {'form':form}
    return render(request, 'journal/new_topic.html', context)