from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Register, Timeslot, Leaveform, Profile, Goal, Feedback
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect, request



def home(request):
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        per_address = request.POST['per_address']
        cur_address = request.POST['cur_address']
        phone = request.POST['phone']
        email = request.POST['email']
        dob = request.POST['dob']
        department = request.POST['department']
        seating_location = request.POST['seating_location']
        date_of_join = request.POST['date_of_join']
        date_of_confirmation = request.POST['date_of_confirmation']
        employee_status = request.POST['employee_status']
        work_phone = request.POST['work_phone']
        experience = request.POST['experience']
        username = request.POST['username']
        password = request.POST['password']
        # password2 = request.POST['password2']
        if Register.objects.filter(email=email).exists():
            error_message = "Email address is already registered."
            return HttpResponse("<script>alert('" + error_message + "');window.location='/signup'</script>")
        if Register.objects.filter(username=username).exists():
            error_message = "Username is already registered."
            return HttpResponse("<script>alert('" + error_message + "');window.location='/signup'</script>")
        user = Register.objects.create(
            fullname=fullname,
            per_address=per_address,
            cur_address=cur_address,
            phone=phone,
            email=email,
            department=department,
            seating_location=seating_location,
            date_of_join=date_of_join,
            date_of_confirmation=date_of_confirmation,
            employee_status=employee_status,
            work_phone=work_phone,
            experience=experience,
            username=username,
            password=password, dob=dob)
        user.save()
        print('User Created')

        return HttpResponse("<script>alert('Registration Successful');window.location='/signin'</script>")

    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Register.objects.filter(username=username, password=password).first()
        # user = Register.objects.get(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            username = request.session.get('username')
            script = "<script>alert('Login Successful, welcome back, {}');window.location='/base'</script>".format(
                username)
            return HttpResponse(script)
        else:
            return HttpResponse("<script>alert('login failed');window.location='signin'</script>")

    else:
        return render(request, 'signin.html')


def signin_html(request):
    return render(request, 'signin.html')



def logout_view(request):
    logout(request)
    request.session.flush()
    messages.info(request, "Logged out successfully!")
    return redirect('home')



def timeslot(request):
    if request.method == 'POST':
        cdate = request.POST['cdate']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']

        user = Timeslot.objects.create(cdate=cdate, checkin=checkin, checkout=checkout, )

        user.save()
        print('User Created')
    else:
        return render(request, 'signup.html')


# @login_required
def user_profile(request):
    return render(request, 'user-profile.html')


def leaveform(request):
    username = request.session.get('username')
    return render(request, 'leaveform.html', {'username': username})


def leave(request):
    username = request.session.get('username')
    return render(request, 'leave.html', {'username': username})


def leave_form(request):
    username = request.session.get('username')
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        position = request.POST['position']
        lead = request.POST['lead']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        leave_type = request.POST['leave_type']
        reason = request.POST['reason']

        leave_request = Leaveform(name=name, department=department, position=position, lead=lead, start_date=start_date,
                                  end_date=end_date, leave_type=leave_type, reason=reason)

        leave_request.save()

        return HttpResponse("<script>alert('values store Successful');window.location='/leaveform'</script>")
    else:
        return render(request, 'leaveform.html', {'username': username})


def view_username(request):
    username = request.session.get('username')
    return render(request, 'view_leaveform.html', {'username': username})


def view_leaveform(request):
    username = request.session.get('username')
    leave_reports = Leaveform.objects.filter(name=username)
    return render(request, 'view_leaveform.html', {'leave_reports': leave_reports})


def view_profile(request):
    username = request.session.get('username')
    profile_view = Register.objects.filter(username=username)
    return render(request, 'profile.html', {'profile_view': profile_view})


def birthday(request):
    username = request.session.get('username')
    births = Register.objects.all()
    return render(request, 'base.html', {'births': births, 'username': username})



def goal(request):
    username = request.session.get('username')
    if request.method == 'POST':
        name = request.POST['name']
        start_d = request.POST['start_d']
        goalname = request.POST['goalname']
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        description = request.POST['description']

        goals = Goal(name=name, start_d=start_d, goalname=goalname, due_date=due_date, priority=priority,
                     description=description)
        goals.save()

        return HttpResponse("<script>alert('values store Successful');window.location='/goal'</script>")
    else:
        return render(request, 'goal.html', {'username': username})


def feedback(request):
    username = request.session.get('username')
    if request.method == 'POST':

        description = request.POST['description']

        fd = Feedback(description=description)

        fd.save()

        return HttpResponse("<script>alert('values store Successful');window.location='/feedback'</script>")
    else:
        return render(request, 'feedback.html', {'username': username})


def tree(request):
    username = request.session.get('username')
    return render(request, 'tree.html', {'username': username})
