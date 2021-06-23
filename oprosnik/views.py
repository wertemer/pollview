from django.shortcuts import render,redirect
from django.http import request
from oprosnik.models import Opros,Questions,Answers,UserAnswers,Users
from datetime import datetime
from django.db.models import Max
from  more_itertools import unique_everseen

# Create your views here.

def index (request):
	polls=Opros.objects.filter(date_end__gte=datetime.now())
	return render(request,'index.html',{'polls':polls})

def poll(request):
	id=request.GET.get("id")
	poll=Opros.objects.filter(id=id)
	questions=Questions.objects.filter(f_opros=id)
	list=[]
	for pol in poll:
		p=pol.name
		pid=pol.id
	for q in questions:
		vars=Answers.objects.filter(f_questions=q.id)
		list.append({'qid':q.id,'name':q.name, 'type':q.type, 'vars':vars})
	return render(request,'poll.html',{'poll':list, 'name':p, 'pid':pid})

def CompletePoll(request):
	user=request.user.id
	if user!=None:
		username=request.user
		u=Users(id=user,name=str(username))
		u.save()
	else:
		user=Users.objects.all().aggregate(Max('id'))
		username='Aноним'
		userid=user['id__max']+1
		u=Users(id=userid,name=str(username))
		u.save()

	if 'poll' in request.POST:
		pid=request.POST['poll']
		questions=Questions.objects.filter(f_opros=pid)
		for q in questions:
			vars=Answers.objects.filter(f_questions=q.id)
			if q.type!=3 :
				for var in vars:
					if str(var.id) in request.POST:
						ua=UserAnswers(f_user=u,f_answer=var)
						ua.save()
			else:
				if 'radio-'+str(q.id) in request.POST:
					s=request.POST['radio-'+str(q.id)]
					print(s)
					vv=Answers.objects.filter(id=int(s))
					for v in vv:
						ua=UserAnswers(f_user=u,f_answer=v)
						ua.save()

	return render(request,"complete.html")

def listusers(request):
	users=Users.objects.all()
	return render(request,'listusers.html',{'users':users})

def results(request):
	list=[]
	vopr=[]
	ansr=[]
	id=request.GET.get("id")
	user=Users.objects.filter(id=id)
	polls=Opros.objects.all()
	ua=UserAnswers.objects.filter(f_user=id)
	for poll in polls:
		ques=Questions.objects.filter(f_opros=poll)
		for que in ques:
			answ=Answers.objects.filter(f_questions=que.id)
			for ans in answ:
				cnt=0
				usa=UserAnswers.objects.filter(f_answer=ans.id,f_user=id)
				for us in usa:
					cnt=cnt+1
				print(cnt)
				ansr.append({'otv':ans.name,'cnt':cnt})
			vopr.append({'vopros':que.name,'answ':ansr})
			ansr=[]
		list.append({'opros':poll.name,'desc':poll.desc,'questions':vopr})
		vopr=[]
	print(list)
	return render(request, 'results.html', {'ua':ua,'lists':list})
