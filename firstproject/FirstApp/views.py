from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):  #viwe function
    #nn==> multi lineis the html code
    ss='''
    <center>
        <h2 style="color:orange;">
            hello nani, welcome to django firstproject 
            FirstApp
        </h2>
        <hr />
    </center>
 ''';
    return HttpResponse(ss);


def show(request):   #viwe function
    #nn==> multi lineis the html code
    ss='''
<html>
    <head>
        <title>***welcome to my world***</title>
        <body>
        <center>
        <h1>welcome to django HTML webpage</h1>
        <hr/>
        <h2>welcome to python world</h2>
        <hr/>
        <h3>welcome to django HTML webpage</h3>
        <hr/>
        <h4>welcome to python world</h4>
        <hr/>
        </center>
        </body>        
     <head>
<html>
 ''';
    return HttpResponse(ss);
 
def defa(request):
    bb='''
<html>
     <head>
     <body>
     <center>
          <h1>welcome to django  default HTML webpage</h1>
     </center>
     </body> 
<html>
''';
    return HttpResponse(bb);
    
    