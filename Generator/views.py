from django.shortcuts import render
from Generator.models import UploadForm,Upload
from django.http import HttpResponseRedirect
from django.urls import reverse
from .QuestionsGenerator import handle_file, generateBank, generateAllQuestionsBank

# Create your views here.
def home(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)       
        if img.is_valid():
            img.save()  
            file = Upload.objects.last()
            questions, chap_nos = handle_file(file.pic.url)
            return render(request, 'select.html', {'questions':questions, 'chap_nos':chap_nos})
            
    else:
        img=UploadForm()
    images=Upload.objects.all()
    return render(request,'home.html',{'form':img,'images':images})

def generateQuestionBank(request):
    file = Upload.objects.last()
    questions, chap_nos = handle_file(file.pic.url)
    selected_chaps = list(map(int, request.POST.getlist('recommendations')))
    selected_qtypes = list(map(int, request.POST.getlist('recommendations2')))
    ques_nos = request.POST['ques_nos']
    prev_perf = request.POST.get('prev_pref', False)
    if(prev_perf):
        generateBank(file.pic.url, questions, chap_nos, selected_chaps, selected_qtypes, ques_nos)
    else:
        generateAllQuestionsBank(questions, chap_nos,selected_chaps, selected_qtypes)

    return render(request, 'result.html')
