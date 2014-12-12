from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.template import RequestContext
import os

# Create your views here.

def show_main(request):
	return render(request,'security/show_main.html',{})
	
def upload(request):
	if request.method == 'POST':
		handle_upload_file(request.FILES['uploadAPK'])
	os.system("rm /home/cyy/androidanalyzer/tmp/test.apk")
	os.system("/usr/bin/java -jar /home/cyy/nsrc/FlowDroid.jar /home/cyy/androidanalyzer/tmp/test.apk /opt/android-sdk-linux/platforms > /home/cyy/androidanalyzer/static/output/result.txt 2> /home/cyy/androidanalyzer/static/output/error" )
	return redirect("/static/output/result.txt")

	# return render_to_response('security/succ.html',{}, RequestContext(request))

def handle_upload_file(f):
	destination = open('/home/cyy/androidanalyzer/tmp/test.apk','wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
    
