from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import News, Branch, Course, Session, Study
from mainapp.models import Student, Enquiry
from studentapp.models import Feedback

def admin_required(view_func):
    """Helper decorator to protect admin routes"""
    def wrapper(request, *args, **kwargs):
        if 'admin' not in request.session:
            messages.error(request, "Please login as Admin to access this page.")
            return redirect('mainapp:adlogin')
        return view_func(request, *args, **kwargs)
    return wrapper

@admin_required
def adparent(request):
    return redirect('adminapp:adhome')

@admin_required
def adhome(request):
    st = Study.objects.all()
    stl = len(st)
    students = Student.objects.all()
    stul = len(students)
    n = News.objects.all()
    nl = len(n)
    fe = Feedback.objects.filter(feedtype="Feedback")
    fel = len(fe)
    co = Feedback.objects.filter(feedtype="Complain")
    col = len(co)
    sug = Feedback.objects.filter(feedtype="Suggestion")
    sugl = len(sug)
    enquiries = Enquiry.objects.all()
    eql = len(enquiries)

    context = {
        'stl': stl,
        'stul': stul,
        'nl': nl,
        'fel': fel,
        'col': col,
        'sugl': sugl,
        'eql': eql,
        'recent_students': students.order_by('-id')[:5],
        'recent_enquiries': enquiries.order_by('-id')[:5],
    }
    return render(request, 'adhome.html', context)

@admin_required
def adnews(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        desc = request.POST.get('desc', '').strip()
        if title and desc:
            News.objects.create(title=title, desc=desc)
            messages.success(request, "News item added successfully!")
        else:
            messages.error(request, "Title and description are required.")
        return redirect('adminapp:adnews')

    news_list = News.objects.all().order_by('-id')
    return render(request, 'adnews.html', {'news': news_list})

@admin_required
def editnews(request, id):
    item = get_object_or_404(News, id=id)
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        desc = request.POST.get('desc', '').strip()
        if title and desc:
            item.title = title
            item.desc = desc
            item.save()
            messages.success(request, "News updated successfully!")
            return redirect('adminapp:adnews')
    news_list = News.objects.all().order_by('-id')
    return render(request, 'adnews.html', {'item': item, 'news': news_list})

@admin_required
def deletenews(request, id):
    News.objects.filter(id=id).delete()
    messages.success(request, "News item deleted.")
    return redirect('adminapp:adnews')

@admin_required
def adbranch(request):
    if request.method == "POST":
        branch = request.POST.get('branch', '').strip()
        if branch:
            Branch.objects.create(branch=branch)
            messages.success(request, "Branch added successfully!")
        return redirect('adminapp:adbranch')
    br = Branch.objects.all()
    return render(request, 'adbranch.html', {'br': br})

@admin_required
def editbranch(request, id):
    b = get_object_or_404(Branch, id=id)
    if request.method == "POST":
        branch = request.POST.get('branch', '').strip()
        if branch:
            b.branch = branch
            b.save()
            messages.success(request, "Branch updated successfully!")
            return redirect('adminapp:adbranch')
    br = Branch.objects.all()
    return render(request, 'adbranch.html', {'b': b, 'br': br})

@admin_required
def deletebranch(request, id):
    Branch.objects.filter(id=id).delete()
    messages.success(request, "Branch deleted.")
    return redirect('adminapp:adbranch')

@admin_required
def adcourse(request):
    if request.method == "POST":
        course = request.POST.get('course', '').strip()
        if course:
            Course.objects.create(course=course)
            messages.success(request, "Course added successfully!")
        return redirect('adminapp:adcourse')
    cr = Course.objects.all()
    return render(request, 'adcourse.html', {'cr': cr})

@admin_required
def editcourse(request, id):
    i = get_object_or_404(Course, id=id)
    if request.method == "POST":
        course = request.POST.get('course', '').strip()
        if course:
            i.course = course
            i.save()
            messages.success(request, "Course updated successfully!")
            return redirect('adminapp:adcourse')
    cr = Course.objects.all()
    return render(request, 'adcourse.html', {'i': i, 'cr': cr})

@admin_required
def deletecourse(request, id):
    Course.objects.filter(id=id).delete()
    messages.success(request, "Course deleted.")
    return redirect('adminapp:adcourse')

@admin_required
def adsession(request):
    if request.method == "POST":
        session_val = request.POST.get('session', '').strip()
        if session_val:
            Session.objects.create(session=session_val)
            messages.success(request, "Session added successfully!")
        return redirect('adminapp:adsession')
    se = Session.objects.all()
    return render(request, 'adsession.html', {'se': se})

@admin_required
def editsession(request, id):
    i = get_object_or_404(Session, id=id)
    if request.method == "POST":
        session_val = request.POST.get('session', '').strip()
        if session_val:
            i.session = session_val
            i.save()
            messages.success(request, "Session updated successfully!")
            return redirect('adminapp:adsession')
    se = Session.objects.all()
    return render(request, 'adsession.html', {'i': i, 'se': se})

@admin_required
def deletesession(request, id):
    Session.objects.filter(id=id).delete()
    messages.success(request, "Session deleted.")
    return redirect('adminapp:adsession')

@admin_required
def adstudent(request):
    st = Student.objects.all().order_by('-id')
    return render(request, 'adstudent.html', {'st': st})

@admin_required
def adstudy(request):
    if request.method == "POST":
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        session_val = request.POST.get('session')
        subject = request.POST.get('subject')
        file_name = request.POST.get('file_name')
        file_obj = request.FILES.get('file')

        study = Study(
            course=course,
            branch=branch,
            session=session_val,
            subject=subject,
            file_name=file_name
        )
        if file_obj:
            study.file = file_obj
        study.save()
        messages.success(request, "Study Material uploaded successfully!")
        return redirect('adminapp:viewstudy')

    cr = Course.objects.all()
    br = Branch.objects.all()
    se = Session.objects.all()
    return render(request, 'adstudy.html', {'cr': cr, 'br': br, 'se': se})

@admin_required
def viewstudy(request):
    st = Study.objects.all().order_by('-id')
    return render(request, 'viewstudy.html', {'st': st})

@admin_required
def editstudy(request, id):
    st_item = get_object_or_404(Study, id=id)
    if request.method == "POST":
        st_item.course = request.POST.get('course')
        st_item.branch = request.POST.get('branch')
        st_item.session = request.POST.get('session')
        st_item.subject = request.POST.get('subject')
        st_item.file_name = request.POST.get('file_name')
        file_obj = request.FILES.get('file')
        if file_obj:
            st_item.file = file_obj
        st_item.save()
        messages.success(request, "Study Material updated successfully!")
        return redirect('adminapp:viewstudy')

    cr = Course.objects.all()
    br = Branch.objects.all()
    se = Session.objects.all()
    return render(request, 'adstudy.html', {'st': st_item, 'cr': cr, 'br': br, 'se': se})

@admin_required
def deletestudy(request, id):
    Study.objects.filter(id=id).delete()
    messages.success(request, "Study material deleted.")
    return redirect('adminapp:viewstudy')

@admin_required
def viewenquiries(request):
    enquiries = Enquiry.objects.all().order_by('-id')
    return render(request, 'adenquiry.html', {'enquiries': enquiries})

@admin_required
def deleteenquiry(request, id):
    Enquiry.objects.filter(id=id).delete()
    messages.success(request, "Enquiry record deleted.")
    return redirect('adminapp:viewenquiries')
