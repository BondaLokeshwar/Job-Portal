from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, JobForm
from .models import Job
from .models import Job, Application
from .forms import ApplicationForm

from .models import Job

def home(request):

    latest_jobs = Job.objects.all().order_by('-id')[:4]

    return render(request, 'index.html', {
        'latest_jobs': latest_jobs
    })

from .models import Job

def jobs(request):
    jobs = Job.objects.all().order_by('-created_at')

    return render(
        request,
        'jobs.html',
        {
            'jobs': jobs
        }
    )

def login_page(request):

    if request.method == "POST":

        email = request.POST.get("email")

        password = request.POST.get("password")

        user = authenticate(
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:

            return render(
                request,
                "login.html",
                {
                    "error": "Invalid Email or Password"
                }
            )

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("home")

def signup(request):

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']

            # Check if email already exists
            if User.objects.filter(username=email).exists():

                return render(request, 'signup.html', {
                    'form': form,
                    'error': 'Email already exists!'
                })

            # Create new user
            User.objects.create_user(
                username=email,
                first_name=first_name,
                email=email,
                password=password
            )

            return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

@login_required
def post_job(request):

    if request.method == "POST":

        Job.objects.create(
            employer=request.user,
            title=request.POST.get("title"),
            company=request.POST.get("company"),
            location=request.POST.get("location"),
            salary=request.POST.get("salary"),
            experience=request.POST.get("experience"),
            job_type=request.POST.get("job_type"),
            description=request.POST.get("description"),
            skills=request.POST.get("skills"),
            deadline=request.POST.get("deadline"),
        )

        return redirect("jobs")

    return render(request, "post-job.html")


from django.shortcuts import get_object_or_404

def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":

        form = ApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            application = form.save(commit=False)

            application.job = job

            application.save()

            return redirect("jobs")

    else:

        form = ApplicationForm()

    return render(
        request,
        "apply-job.html",
        {
            "form": form,
            "job": job
        }
    )

from django.shortcuts import get_object_or_404



def dashboard(request):

    if request.user.is_authenticated:
        return render(request, "dashboard.html")

    return redirect("login")

from django.contrib.auth.decorators import login_required

