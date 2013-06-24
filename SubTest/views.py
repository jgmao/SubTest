# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
import glob
import os
from random import randint, sample
from SubTest.models import SubTestResult

def show_image(request):
        global imgfiles
        posts = SubTestResult.objects.all()
        posts.orgName = []
        posts.candName = []
        posts.rank = []
        path = 'E:/texture/totest/png/'
        
        for file in os.listdir(path):
                if file.startswith("org"):
                        posts.orgName.append(file)
		if file.startswith("cand"):
                        posts.candName.append(file)
                candi_org = []
        for candi in posts.candName:
		if candi[4] == posts.orgName[0][3]:
			candi_org.append(candi)
	candi_index = range(0,len(candi_org))
	candinum = sample(candi_index,2)
	# print the collection of canidates
	print 'selected candidate'
	print posts.candName[candinum[0]]
	print posts.candName[candinum[1]]
	
	imgfiles = [posts.orgName[0],posts.candName[candinum[0]],posts.candName[candinum[1]] ]
	return render(request,'display_images.html',{'images':imgfiles})

def view_rank(request):
        if request.method == 'POST':
                c = imgfiles
                p = request.POST.getlist('answer[]')
                combo = [[c[0],p[0]],[c[1],p[1]],[c[2],p[2]]]
        return render(request,'result.html',{'rank':combo})
