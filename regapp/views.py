
from django.shortcuts import render
from regapp.models import Person,Admin,Student,Faculty,Attend,Mark,Leave_s,leave_f
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def display(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        emailid=request.POST.get('emailid')
        mobilenumber=request.POST.get('mobilenumber')
        password=request.POST.get('password')

        a= Person(firstname=firstname,emailid=emailid,mobilenumber=mobilenumber,password=password,)
        a.save()
    return render(request,'login.html')
def authentication(request):
    if request.method=='POST':
        firstname=request.POST.get('name')
        password=request.POST.get('password')
        firstname=str(firstname)
        password=str(password) 
        u=Person.objects.filter(password=password)
        p=Person.objects.filter(firstname=firstname) 
        c=0
        if u.count()==1 and p.count()==1:
            c+=1
            if c==1:
                return HttpResponse('login successful')
            else:
                return HttpResponse('login unsuccessful')
def ad(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        name=str(name)
        password=str(password) 
        k=Admin.objects.filter(name=name,password=password)
        if k.count()==1:
                return render(request,'dropdown.html')
        else:
                l=Student.objects.filter(Sname=name,Password=password)
                if l.count()==1:
                         request.session['Sname']=name
                         return render(request,'sdrp.html')
                         # return HttpResponse("Hello")
                else:
                        p=Faculty.objects.filter(Fname=name,password=password)
                        if p.count()==1:
                                 request.session['Fname']=name
                                 return render(request,'fdrop.html')
                                # return HttpResponse("Hello")
                        else:
                                 return HttpResponse('login failed')
                        

'''def Sty(request):
    if request.method=='POST':
        Sname=request.POST.get('Sname')
        Password=request.POST.get('Password')
        Sname=str(Sname)
        Password=str(Password) 
        k=Student.objects.filter(Password=Password)
        l=Student.objects.filter(Sname=Sname)
        c=0 
        if k.count()==1 and l.count()==1:
            
            c=c+1
            if c==1:
                request.session['Sname']=Sname
                return render(request,'sdrp.html')
                # return HttpResponse("Hello")
            else:
                return HttpResponse('login failed')
        else:
            return HttpResponse(' failed')
def Facu(request):
    if request.method=='POST':
        Fname=request.POST.get('Fname')
        password=request.POST.get('password')
        Fname=str(Fname)
        password=str(password) 
        p=Faculty.objects.filter(password=password)
        q=Faculty.objects.filter(Fname=Fname)
        c=0 
        if p.count()==1 and q.count()==1:
            c=c+1
            if c==1:
                request.session['Fname']=Fname
                return render(request,'fdrop.html')
                # return HttpResponse("Hello")
            else:
                return HttpResponse('login failed')
        else:
            return HttpResponse(' failed')'''   
def Stu(request):
    if request.method=='POST':
        Sname=request.POST.get('Sname')
        Sid=request.POST.get('Sid')
        Address=request.POST.get('Address')
        Gender=request.POST.get('Gender')
        AdmDate=request.POST.get('AdmDate')
        Mobileno=request.POST.get('Mobileno')
        Batch=request.POST.get('Batch')
        Email=request.POST.get('Email')
        Guardian=request.POST.get('Guardian')
        Password=request.POST.get('Password')


        b= Student(Sname=Sname,Sid=Sid,Address=Address,Gender=Gender,AdmDate=AdmDate,
        Mobileno=Mobileno,Batch=Batch,Email=Email,Guardian=Guardian,Password=Password)
        b.save()
    return render(request,'dropdown.html')

def facdb(request):
    if request.method=='POST':
        Fname=request.POST.get('Fname')
        Fid=request.POST.get('Fid')
        Address=request.POST.get('Address')
        Gender=request.POST.get('Gender')
        Qual=request.POST.get('Qual')
        Mobileno=request.POST.get('Mobileno')
        Batch=request.POST.get('Batch')
        Email=request.POST.get('Email')
        password=request.POST.get('password')


        c= Faculty(Fname=Fname,Fid=Fid,Address=Address,Gender=Gender,Qual=Qual,
        Mobileno=Mobileno,Batch=Batch,Email=Email,password=password)
        c.save()
    return render(request,'dropdown.html')
def attendance(request):
    if request.method=='POST':
        Sname=request.POST.get('Sname')
        Sid=request.POST.get('Sid')
        Period1=request.POST.get('Period1')
        Period2=request.POST.get('Period2')
        Period3=request.POST.get('Period3')
        Period4=request.POST.get('Period4')

        d=Attend(Sname=Sname,Sid=Sid,Period1=Period1,Period2=Period2,Period3=Period3,Period4=Period4)
        d.save()
    return render(request,'fdrop.html')
def marks(request):
    if request.method=='POST':
        Sname=request.POST.get('Sname')
        Sid=request.POST.get('Sid')
        C=request.POST.get('C')
        CPP=request.POST.get('CPP')
        Java=request.POST.get('Java')
        Python=request.POST.get('Python')
        Html=request.POST.get('Html')
        

        e=Mark(Sname=Sname,Sid=Sid,C=C,CPP=CPP,Java=Java,Python=Python,Html=Html)
        e.save()
    return render(request,'fdrop.html')
def sleave(request):
    if request.method=='POST':
        Sname=request.POST.get('Sname')
        Sid=request.POST.get('Sid')
        From_date=request.POST.get('From_date')
        To_date=request.POST.get('To_date')
        Reason=request.POST.get('Reason')
        Status=request.POST.get('Status')        
        f=Leave_s(Sname=Sname,Sid=Sid,From_date=From_date,To_date=To_date,Reason=Reason,Status=Status)
        f.save()
    return render(request,'sdrp.html')
def fleave(request):
    if request.method=='POST':
        Fname=request.POST.get('Fname')
        Fid=request.POST.get('Fid')
        From_date=request.POST.get('From_date')
        To_date=request.POST.get('To_date')
        Reason=request.POST.get('Reason')
        Status=request.POST.get('Status')
        
        g=leave_f(Fname=Fname,Fid=Fid,From_date=From_date,To_date=To_date,Reason=Reason,Status=Status)
        g.save()
    return render(request,'fdrop.html')


def fetche(request):
    queryset=Student.objects.all()
    return render(request,'stufetch.html',{'authors':queryset})

def fetf(request):
    queryy=Faculty.objects.all()
    return render(request,'facfetch.html',{'authors':queryy})

def stup(request):
    query1=Student.objects.all().filter(Sname=request.session['Sname'])
    return render(request,'sprof.html',{'authors':query1})

def facp(request):
    query2=Faculty.objects.all().filter(Fname=request.session['Fname'])
    return render(request,'fprof.html',{'authors':query2})

def fetchatt(request):
    queryset1=Attend.objects.all()
    return render(request,'fattfetch.html',{'authors':queryset1})

def stuat(request):
    query3=Attend.objects.all().filter(Sname=request.session['Sname'])
    return render(request,'stuattv.html',{'authors':query3})

def facmfe(request):
    queryset4=Mark.objects.all()
    return render(request,'fmafet.html',{'authors':queryset4})

def stuma(request):
    query5=Mark.objects.all().filter(Sname=request.session['Sname'])
    return render(request,'stumarv.html',{'authors':query5})

def stlea_fet(request):
    query6=Leave_s.objects.all().filter()
    return render(request,'stleafet.html',{'authors':query6})

def flea_fet(request):
    query7=leave_f.objects.all().filter()
    return render(request,'fleafet.html',{'authors':query7})
def logoutt(request):
    logout(request)
    return redirect('index')
def approvef(request):
    if request.method=='POST':
        Fid=request.POST.get('Fid')
        leave_f.objects.filter(Fid=Fid).update(Status='Approved')
    return redirect('fleafet')
def approves(request):
    if request.method=='POST':
        Sid=request.POST.get('Sid')
        Leave_s.objects.filter(Sid=Sid).update(Status='Approved')
    return redirect('stleafet')