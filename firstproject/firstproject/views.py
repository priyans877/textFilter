from django.http import HttpResponse
from django.shortcuts import render
"""
#code till video 6
#it require request argument to operate ,it does't work with no argument
def index(request):
    return HttpResponse("hello")
    
def about(request):
    return HttpResponse("About priyanshu bhai")

def index(request):
    return HttpResponse('''<h1>hii this is my first navigator using django python</h1>''')
    
    
def harry(request):
    return HttpResponse('''<h1>Hii this is our first navigator website using django</h1><a href="https://www.codewithharry.com/">toward Code with harry website</a> ''')
def facebook(request):
    return HttpResponse('''<h1>Hii this is our first navigator website using django</h1><a href="https://www.facebook.com/login/">toward facebook</a>''')
def Whatsappweb(request):
    return HttpResponse('''<h1>Hii this is our first navigator website using django</h1><a href="https://web.whatsapp.com/"> toward Whatsapp Web</a>''')
def Youtube(request):
    return HttpResponse('''<h1>Hii this is our first navigator website using django</h1><a href="https://www.youtube.com/"> toward Youtube</a>''')

"""

#code from video 7
"""def index(request):
    return HttpResponse('''<h1>HOME</h1><br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/removepunc'><h1>Remove line</h1></a></button><br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/capfirst'><h1>Caps first</h1></a></button><br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/spaceremove'><h1>space remove</h1></a></button><br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/newlineremove'><h1>New line Remove</h1></a></button><br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/charcout'><h1>character count</h1></a></button>''')

def removepunc(request):
    return HttpResponse('''Remove puncuation<br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/'>Click here</a></button>''')

def capfirst(request):
    return HttpResponse('''Caps First<br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/'>Click here</a></button>''')
def spaceremove(request):
    return HttpResponse('''space Remover<br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/'>Click here</a></button>''')
def newlineremove(request):
    return HttpResponse('''New line Remove<br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/'>Click here</a></button''')
def charcout(request):
    return HttpResponse('''char count<br></br><button type="button"><font-size : 16px></font-size><a href='http://127.0.0.1:8000/'>Click here</a></button>''')
"""  
#from video 8 to 9
'''def index(request):
    params={'name':'Priyanshu kumar choubey','place':'delhi ncr','date':'2006.aa'}
    return render(request,'index.html')
def removepunc(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse("Hello")
def charcout(request):
    return HttpResponse("Hello")
def spaceremove(request):
    return HttpResponse("Hello")
def newlineremove(request):
    return HttpResponse("Hello")
def capfirst(request):
    return HttpResponse("Hello")'''

def index(request):
    return render(request,'index.html')
def analyzetxt(request):
    djtext=request.POST.get('text','defualt')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    NEWlineremove=request.POST.get('nlremover','off')
    spaceremo=request.POST.get('spaceremove','off')
    charcount=request.POST.get('charcout','off')
    puntuates='''!()-{};:\/,.<>'"?@#$%^&*_~`'''
    
    if removepunc=='on':
        rtext=""
        for char in djtext:
            if char not in puntuates:
                rtext=rtext+char
        param={'purpose':'REMOVE PUNTUATION','analyze_txt':rtext}
        djtext=rtext
    if fullcaps=='on':
        cap=""
        for char in djtext:
            cap=cap+char.upper()
        param={'purpose':'CAPITALIZED TEXT','analyze_txt':cap}
        djtext=cap
    if spaceremo=='on':
        space=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]=="  "):
                space=space+char
        param={'purpose':'SPACE REMOVER','analyze_txt':space}
        djtext=space
    if NEWlineremove=='on':
        nline=""
        for char in djtext:
            if char!="\n" and char!="\r":
                nline=nline+char
        param={'purpose':'NEWLINE REMOVER','analyze_txt':nline}
        djtext=nline
    if charcount=='on':
        caout=0
        for char in djtext:
            if char != " ":
                caout+=1
        djtext=caout
        param={'purpose':'CHARACTER COUNT','analyze_txt':caout}
    if (removepunc!='on' and fullcaps!='on' and spaceremo!='on' and NEWlineremove!='on' and charcount!='on'):
        return HttpResponse("Error please choose any option to operate")
    return render(request,'analyze.html',param)
            
                 

    





'''    param={}
    def removepu(request,text,fhts,hdd):
        for char in text:
            if char not in hdd:
                fhts=fhts+char   
        param={'purpose':"REMOVE PUNCUATION",'analyzed_txt2':fhts}    
        return render(request,'analyze.html',param)

    def fullcapss(request,text,analyucaps):
        for char in text:
            analyucaps=analyucaps+(char.upper())        
        param={'purpose1':"UPPERCSE LETTER's",'uppercase':analyucaps}    
        return param

    def newline(request,text,newlines):
        for char in text:
            if char!="\n":
                newlines=newlines+char
        param={'purpose2':"NEW LINE REMOVED",'newlinermove':newline}    
        return render(request,'analyze.html',param)

    def spacerem(request,text,spacere):
        for char in text:
            if char!="  " or char<="":
                spacere=spacere+char
        return spacere

    def charcout(request,text,number):
        for char in text:
            if char != " ":
                number+=1
        return number
  
    if removepunc=='on' and fullcaps=='on' and spaceremo=='on' and NEWlineremove=='on' and charcount=='on':
        removepu(request,djtext,rtext,puntuates)
        spacerem(request,rtext,space)
        fullcapss(request,rtext,full)
        newline(request,rtext,nline)
        charcout(request,rtext,cout)
    elif fullcaps=='on':
        fullcapss(request,djtext,full)
    elif spaceremo=='on':
        spacerem(request,djtext,space)
    elif charcount=='on':
        charcout(request,djtext,cout)
    else:
        newline(request,djtext,nline)'''
    
    


'''  para={'purpose':"REMOVE PUNCUTATION",'analyzed_text':djtext,'analyzed_txt2':rtext,'purpose4':"CHARACTER COUNTER",'charactercout':cout,'purpose3':"EXTRA SPACE REMOVED",'spaceremover':space,'purpose2':"NEW LINE REMOVED",'newlinermove':nline,'purpose1':"UPPERCSE LETTER's",'uppercase':full}
    return render(request,'analyze.html',para)'''

    
    