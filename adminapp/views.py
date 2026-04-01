
from django.shortcuts import render, redirect
from.models import News,Branch,Course,Session,Study
from mainapp.models import Student
from studentapp.models import Feedback

# Create your views here.

def adparent(request):
    return render(request, 'adparent.html')
def adnews(request):
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        news=News.objects.create(title=title,desc=desc)
        return redirect('adminapp:adnews')

    news=News.objects.all()
    return render(request,'adnews.html',{"news":news})
def adbranch(request):
    if request.method=="POST":
        branch=request.POST['branch']
        br=Branch.objects.create(branch=branch)
        return redirect('adminapp:adbranch')
    br=Branch.objects.all()
    return render(request,'adbranch.html',{"br":br})
def adcourse(request):
    if request.method=="POST":
        course=request.POST['course']
        
        cr=Course.objects.create(course=course)
        return redirect('adminapp:adcourse')
    cr=Course.objects.all()

    return render(request,'adcourse.html',{"cr":cr})
def adsession(request):
    if request.method=="POST":
        session=request.POST['session']
        
        se=Session.objects.create(session=session)
        return redirect('adminapp:adsession')
    se=Session.objects.all()

    return render(request,'adSession.html',{"se":se})


def adstudent(request):
    Student.objects.all()
    return render(request,'adstudent.html',locals())
def adstudy(request):
    return render(request,'adstudy.html')
def viewsstudy(request):
    return render(request,'viewstudy.html')

def editbranch(request,id):
    if request.method=="POST":
        branch=request.POST['branch']
        Branch.objects.filter(id=id).update(branch=branch)
        return redirect('adminapp:adbranch')
    br=Branch.objects.all()
    b=Branch.objects.get(id=id)
    return render(request,'adbranch.html',{'b':b,'br':br})

def deletebranch(request,id):
    Branch.objects.filter(id=id).delete()
    return redirect('adminapp:adbranch')

def editcourse(request,id):
    if request.method=="POST":
        course=request.POST['course']
        Course.objects.filter(id=id).update(course=course)
        return redirect('adminapp:adcourse')
    cr=Course.objects.all()
    i=Course.objects.get(id=id)
    return render(request,'adcourse.html',{'i':i,'cr':cr})

def deletecourse(request,id):
    Course.objects.filter(id=id).delete()
    return redirect('adminapp:adcourse')

def editsession(request,id):
    if request.method=="POST":
        session=request.POST['session']
        Session.objects.filter(id=id).update(session=session)
        return redirect('adminapp:adsession')
    se=Session.objects.all()
    i=Session.objects.get(id=id)
    return render(request,'adsession.html',{'i':i,"se":se})   

def deletesession(request,id):
    Session.objects.filter(id=id).delete()
    return redirect('adminapp:adsession')     


def adstudy(request):
    if request.method == "POST":
        course = request.POST['course']
        branch = request.POST['branch']
        session = request.POST['session']
        subject = request.POST['subject']
        file_name = request.POST['file_name']
        file = request.FILES.get('file')
        stu = Study()
        stu.course = course
        stu.branch = branch
        stu.session = session
        stu.subject = subject
        stu.file_name = file_name
        if file:
            stu.file = file
        stu.save()
        return redirect('adminapp:adstudy')
    cr = Course.objects.all()
    br = Branch.objects.all()
    se = Session.objects.all()
    return render(request,'adstudy.html',locals())
    

def adhome(request):
    st=Study.objects.all()
    stl = len(st)
    st = Student.objects.all()
    stul = len(st)
    n = News.objects.all()
    nl = len(n)
    fe = Feedback.objects.filter(feedtype = "Feedback")
    fel = len(fe)
    co = Feedback.objects.filter(feedtype = "Complain")
    col = len(co)
    sug =Feedback.objects.filter(feedtype = "Suggestion" )
    sugl = len(sug)
    return render(request, 'adhome.html',locals())

def viewstudy(request):
    return render(request,'viewstudy.html',locals())
def editstudy(request, id):
    if request.method == "POST":
        course = request.POST['course']
        branch = request.POST['branch']
        session = request.POST['session']
        subject = request.POST['subject']
        file_name = request.POST['file_name']
        study = Study.objects.get(id=id)
        study.course = course
        study.branch = branch
        study.session = session
        study.subject = subject
        study.file_name = file_name
        file = request.FILES.get('file')
        if file:
            study.file = file
        study.save()
        return redirect('adminapp:viewstudy')
    st = Study.objects.get(id=id)
    cr = Course.objects.all()
    br = Branch.objects.all()
    se = Session.objects.all()
    return render(request,'adstudy.html',locals())

def deletestudy(request,id):
    Study.objects.filter(id=id).delete()
    return redirect('adminapp:adstudy')           
