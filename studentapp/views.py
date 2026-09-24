from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from mainapp.models import Student
from adminapp.models import News, Study
from .models import Feedback

def student_required(view_func):
    """Decorator to require student login session"""
    def wrapper(request, *args, **kwargs):
        if 'student' not in request.session or not request.session['student']:
            messages.error(request, "Please login as Student to access your portal.")
            return redirect('mainapp:login')
        return view_func(request, *args, **kwargs)
    return wrapper

@student_required
def stuhome(request):
    try:
        stu = Student.objects.get(id=request.session['student'])
    except Student.DoesNotExist:
        request.session.flush()
        messages.error(request, "Student account not found.")
        return redirect('mainapp:login')

    st = Study.objects.filter(course=stu.course, branch=stu.branch, session=stu.session)
    stl = len(st)
    fe = Feedback.objects.filter(sid=str(stu.id), feedtype="Feedback")
    fel = len(fe)
    co = Feedback.objects.filter(sid=str(stu.id), feedtype="Complain")
    col = len(co)
    su = Feedback.objects.filter(sid=str(stu.id), feedtype="Suggestion")
    sul = len(su)
    n = News.objects.all()
    nl = len(n)

    context = {
        'stu': stu,
        'stl': stl,
        'fel': fel,
        'col': col,
        'sul': sul,
        'nl': nl
    }
    return render(request, 'stuhome.html', context)

@student_required
def stunews(request):
    news_list = News.objects.all().order_by('-id')
    return render(request, 'stunews.html', {'news': news_list})

@student_required
def stustudy(request):
    try:
        stu = Student.objects.get(id=request.session['student'])
        study_materials = Study.objects.filter(course=stu.course, branch=stu.branch, session=stu.session).order_by('-id')
    except Student.DoesNotExist:
        study_materials = []
    return render(request, 'stustudy.html', {'study_materials': study_materials})

@student_required
def stufeedback(request):
    if request.method == "POST":
        feedtype = request.POST.get('feedtype', '').strip()
        title = request.POST.get('title', '').strip()
        desc = request.POST.get('desc', '').strip()
        sid = str(request.session['student'])

        if feedtype and title and desc:
            Feedback.objects.create(feedtype=feedtype, title=title, desc=desc, sid=sid)
            messages.success(request, f"{feedtype} submitted successfully!")
            return redirect('studentapp:stuviewfeedback')
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'stufeedback.html')

@student_required
def stuviewfeedback(request):
    sid = str(request.session['student'])
    viewfeedback = Feedback.objects.filter(sid=sid).order_by('-id')
    return render(request, 'stuviewfeedback.html', {'viewfeedback': viewfeedback})

@student_required
def deletefeedback(request, id):
    sid = str(request.session['student'])
    Feedback.objects.filter(id=id, sid=sid).delete()
    messages.success(request, "Feedback entry deleted.")
    return redirect('studentapp:stuviewfeedback')