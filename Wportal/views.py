from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import User, Teacher, Student, Note
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from .forms import NoteForm


def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password,)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        category = request.POST["user_type"]

        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(
                username, email, password, user_type=category)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")


def upload_file(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'createNote.html', {
        'form': form
    })


def profile(request, id):
    users = User.objects.get(id=id)
    try:
        check = Teacher.objects.get(user=users)
        c = True
    except Teacher.DoesNotExist:
        c = False
    try:
        check2 = Student.objects.get(user=users)
        c2 = True
    except Student.DoesNotExist:
        c2 = False
    # if request.method == "POST":
    #     if(users.user_type == "Teacher"):
    #         if(c):
    #             obj = check
    #             obj.qualify = request.POST['qualification']
    #             obj.subject = request.POST['subject']
    #             obj.experince = request.POST['expericence']
    #         else:
    #             obj = Teacher(
    #                 user=request.user,
    #                 qualify=request.POST['qualification'],
    #                 subject=request.POST['subject'],
    #                 experince=request.POST['expericence']
    #             )
    #         obj.save()
    #     else:
    #         if(c2):
    #             obj2 = check2
    #             obj2.standard = request.POST["standard"]
    #             obj2.dob = request.POST["dob"]
    #             obj2.age = request.POST["age"]
    #         else:
    #             obj2 = Student(
    #                 user=request.user,
    #                 standard=request.POST["standard"],
    #                 dob=request.POST["dob"],
    #                 age=request.POST["age"]
    #             )
    #         obj2.save()
    #     return render(request, "index.html")
    # else:
    if(users.user_type == "Teacher"):
        if(c):
            return render(request, "createProfile.html", {
                "profile": check
            })
        else:
            return render(request, "createProfile.html")
    else:
        if(c2):
            return render(request, "createProfile.html", {
                "profile": check2
            })
        else:
            return render(request, "createProfile.html")


# def user(request, id):
#     user = User.objects.get(id=id)
#     if(user.user_type == "Teacher"):
#         try:
#             common = Teacher.objects.get(user=user)
#             g = True
#         except Teacher.DoesNotExist:
#             g = False
#     else:
#         try:
#             common = Student.objects.get(user=user)
#             g = True
#         except Student.DoesNotExist:
#             g = False
#     if(g):
#         return render(request, "userProfile.html", {
#             "profile": common
#         })
#     else:
#         return render(request, "createProfile.html", {
#             "profile": common
#         })


# def allnotes(request):
#     allnote = Note.objects.all()
#     return render(request, "allNotes.html", {
#         'allnote': allnote
#     })


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        return render(request, 'createNote.html', context)


def filters(request):
    if request.method == "POST":
        sub = request.POST['subject']
        sta = request.POST['standard']
        try:
            fil = Note.objects.filter(subject=sub, standard=sta)
            flag = True
            return render(request, "allNotes.html", {
                'allnote': fil,
                'flag': flag
            })
        except Note.DoesNotExist:
            flag = False
            return render(request, "allNotes.html", {
                'flag': flag
            })
    else:
        return render(request, "filter.html")


@csrf_exempt
def searchs(request):
    if request.method == "POST":
        details = json.loads(request.body)
        s1 = details["sta"]
        s2 = details["sub"]
        try:
            store = Note.objects.filter(standard=s1, subject=s2)
            flag = True
            return JsonResponse({'allnotes': [p.serialize() for p in store], 'flag': flag})
        except Note.DoesNotExist:
            flag = False
            return JsonResponse({'flag': flag})
    else:
        return JsonResponse({"post": "Post method required"})
