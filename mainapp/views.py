from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin, Student, Login, Enquiry
from adminapp.models import Course, Branch, Session, News, Study
import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def index(request):
    news_list = News.objects.all().order_by('-id')[:10]
    return render(request, 'index.html', {'news_list': news_list})

def about(request):
    return render(request, 'about.html')

def adlogin(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        
        try:
            ad = Admin.objects.get(email=email)
            if ad.password == password:
                request.session['admin'] = ad.email
                messages.success(request, "Welcome back, Admin!")
                return redirect('adminapp:adhome')
            else:
                messages.error(request, "Invalid Admin Password.")
        except Admin.DoesNotExist:
            messages.error(request, "Admin email not found.")
            
        return redirect('mainapp:adlogin')
    return render(request, 'adlogin.html')

def logout(request):
    request.session.flush()
    messages.success(request, "Successfully logged out.")
    return redirect('mainapp:index')

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        fname = request.POST.get('fname', '').strip()
        mname = request.POST.get('mname', '').strip()
        number = request.POST.get('number', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        gender = request.POST.get('gen', '').strip()
        course = request.POST.get('course', '').strip()
        branch = request.POST.get('branch', '').strip()
        session_val = request.POST.get('session', '').strip()
        address = request.POST.get('address', '').strip()
        pic = request.FILES.get('pic')

        if Login.objects.filter(email=email).exists() or Student.objects.filter(email=email).exists():
            messages.error(request, "A student with this email already exists!")
            return redirect('mainapp:registration')

        stu = Student(
            name=name,
            fname=fname,
            mname=mname,
            number=number,
            email=email,
            gender=gender,
            course=course,
            branch=branch,
            session=session_val,
            address=address,
            pic=pic
        )
        stu.save()
        Login.objects.create(email=email, password=password)

        # Attempt to send email, but don't fail registration if SMTP is unconfigured
        try:
            context = {
                'name': name,
                'email': email,
                'password': password,
                'year': datetime.datetime.now().year
            }
            html_content = render_to_string('email.html', context)
            subject = "Welcome to Biotech Park OLP"
            from_email = settings.EMAIL_HOST_USER
            to = [email]

            msg = EmailMultiAlternatives(subject, '', from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send(fail_silently=True)
        except Exception:
            pass

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('mainapp:login')

    cr = Course.objects.all()
    br = Branch.objects.all()
    se = Session.objects.all()
    return render(request, 'reg.html', {'cr': cr, 'br': br, 'se': se})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        
        try:
            lo = Login.objects.get(email=email)
            if lo.password == password:
                student = Student.objects.get(email=email)
                request.session['student'] = student.id
                messages.success(request, f"Welcome back, {student.name}!")
                return redirect('studentapp:stuhome')
            else:
                messages.error(request, "Incorrect password. Please try again.")
        except (Login.DoesNotExist, Student.DoesNotExist):
            messages.error(request, "No account found with this email address.")
            
        return redirect('mainapp:login')
    return render(request, 'login.html')

def organization(request):
    return render(request, 'org.html')

def certification(request):
    return render(request, 'certi.html')

def enquiry(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            Enquiry.objects.create(
                name=name,
                mobile=mobile,
                email=email,
                message=message
            )
            messages.success(request, "Thank you for reaching out! Your enquiry has been received.")
            return redirect('mainapp:enquiry')
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'enquiry.html')

def services(request):
    return render(request, 'services.html')
