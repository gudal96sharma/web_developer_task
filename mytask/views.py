from django.shortcuts import render

def index(request):
    context={}
    if request.method=='POST':
    	print(request.method,"POST")
    	try:
		    fullname = request.POST['fullname']
			email = request.POST["email"]
			message = request.POST["message"]
			print(fullname,"fullname")

    return render(request, 'index.html', context)
   