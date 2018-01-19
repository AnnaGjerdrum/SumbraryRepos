from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .forms import UserForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Summary
from .models import Book
from .models import University
from .models import Subject
from django.shortcuts import render, redirect, get_object_or_404

def summary_list(request):
    summaries = Summary.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'summary_list.html', { 'summaries': summaries })

def summary_detail(request, pk):
    summary = get_object_or_404(Summary, pk=pk)
    return render(request, 'summary_detail.html', { 'summary': summary })

def pdf_view(request, filename):
    url = '%s\\%s' % (settings.MEDIA_ROOT, filename)
    with open(url, 'r') as pdf:
        response = HttpResponse(pdf.read(), type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=' + url
        return response
    pdf.closed

def uni(request, pk):
    uni = get_object_or_404(University, id=pk)
    summaries = Summary.objects.filter(university=uni.universityName)
    return render(request, 'university.html', { 'summaries': summaries, 'uni': uni })

def book(request, pk):
    book = get_object_or_404(Book, id=pk)
    summaries = Summary.objects.filter(book=book.title)
    return render(request, 'book.html', { 'summaries': summaries, 'book': book })

def subject(request, pk):
    subj = get_object_or_404(Subject, id=pk)
    summaries = Summary.objects.filter(subject=subj.subjectCode)
    return render(request, 'subject.html', {'summaries': summaries, 'subj': subj })

def allUnis(request):
    unis = University.objects.all()
    return render(request, 'allUnis.html', { 'unis': unis })

def allSubj(request):
    subj = Subject.objects.all()
    return render(request, 'allSubj.html', { 'subjs': subj })

def allBooks(request):
    books = Book.objects.all()
    return render(request, 'allBooks.html', { 'books': books })

class index_view(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        subjects = Subject.objects.all()
        books = Book.objects.all()
        unis = University.objects.all()
        summaries = Summary.objects.all()
        context = {
            'subjects': subjects,
            'books': books,
            'unis': unis,
	        'summaries': summaries,
            }
        return render(request, self.template_name, context)

class login_auth(TemplateView):
    form_class = UserForm
    template_name = 'login.html'
    # process form data registration
    def post(self, request):
        error_message = "Username or password is wrong"
        form = request.POST

        username = form.get('username', None)
        password = form.get('password', None)

        if username and password:

            #returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active: #logged in with everything ok: pw, exists
                    login(request, user)
                    return redirect('../user/')

        return render(request, self.template_name, { 'error_message': error_message })

class addSummary(TemplateView):
    template_name = 'add_summary.html'

    def get(self, request):
        if request.user.is_authenticated():
            return render(request, self.template_name, '')
        return redirect('../login')

    def post(self, request):
         form = request.POST

         title = form.get('title', None)
         user = request.user.username
         book, created = Book.objects.get_or_create(title=str(form.get('book', None)))
         subject, created = Subject.objects.get_or_create(subjectName=str(form.get('subject', None)))
         university, created = University.objects.get_or_create(universityName=str(form.get('university', None)))
         summaryfile = ''

         if request.method == 'POST' and request.FILES['myfile']:
             myfile = request.FILES['myfile']
             fs = FileSystemStorage()
             summaryfile = '%s' % myfile.name
             filename = fs.save(summaryfile, myfile)

         summary = Summary(title=title, user=user, book=book.title, subject=subject.subjectName, university=university.universityName, filepath=summaryfile, rating=0, numRates=0)
         summary.save()

         return redirect('../user/')

def deleteSummary(request, pk):
        if request.user.is_authenticated():
            summary = get_object_or_404(Summary, pk=pk)
            summary.delete()
        return redirect('../../user/')

class logout_auth(TemplateView):

    def get(self, request):
        if request.user.is_authenticated():
            logout(request)

        return redirect('../')


class signup(TemplateView):
    form_class = UserForm
    template_name = 'signup.html'
    # process form data registration
    def post(self, request):
        error_message = "Your input is not valid"
        form = self.form_class(request.POST)

        if form.is_valid():
            #store information in database
            user = form.save(commit=False)
            #clean normalized data, formated properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            #returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active: #logged in with everything ok: pw, exists
                    login(request, user)
                    return redirect('../user/')
        return render(request, self.template_name, { 'error_message': error_message })


class userView(TemplateView):
    template_name = 'user.html'

    def get(self, request):
        error_message = "Your input is not valid"
        summaries = Summary.objects.filter(user=request.user.username)
        if request.user.is_authenticated():
            context = {
                'username':  request.user.username,
                'summaries': summaries,
            }
            #get all items the user needs
            return render(request, self.template_name, context)
        return render(request, 'user.html', { 'error_message': error_message })
