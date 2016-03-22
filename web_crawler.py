from urllib2 import urlopen,Request#Module for reading from the web
import re
import sys  
import subprocess
import os

reload(sys)  
sys.setdefaultencoding("ISO-8859-1")

final_urls_of_problems=[]

for r in range(19,20):

        k = "http://codeforces.com/problemset/page/"+str(r)
	request = Request(k)
	response = urlopen(request)
	the_page = response.read()
	theText = the_page.decode()

	f = open("1.txt",'w')
	f.write(theText)
        
	command = "grep '/problemset/problem' 1.txt"
	output = subprocess.check_output(command,shell=True)
	output = output.split("\n")
	output1=[]
	for i in output:
	    i = i.strip(" ")
	    output1.append(i)

	
	for i in range(0,len(output1),2):
	    h=""
	    h=h+output1[i][9:len(output1[i])-3]
	    final_urls_of_problems.append(h)
        os.system("rm 1.txt")

for i in range(0,len(final_urls_of_problems)):
#for i in range(0,1):
    final_tags = []
    k = "http://codeforces.com" + final_urls_of_problems[i]
    request = Request(k)
    try:
        response = urlopen(request)
    except:
        continue
    the_page = response.read()
    theText = the_page.decode()
    f = open("2.txt",'w')
    f.write(theText)
    command = "grep 'problem-statement\"' 2.txt"
    try:
        output =  subprocess.check_output(command,shell=True)
    except:
        os.system("rm 2.txt")
        continue

    
    output = re.sub('<[^>]+>', ' ', output)
    command = "grep 'tag-box\"' 2.txt"
    try:
        output_tags =  subprocess.check_output(command,shell=True)
    except:


        string="empty"

        w1 = open("problems.txt",'a')
        w2 = open("tags.txt",'a')
        w1.write(output)
        w2.write(string)
        os.system("rm 2.txt")
        continue
    output_tags = output_tags.split("\n")
    #output_tags = output_tags.split("=")
    for j in range(0,len(output_tags)):
        temp = output_tags[j].split("=")
        final_tags.append(temp[-1])

    

    string=""
    for i in final_tags:
        #print i
        i = i.replace("\"", "")
        i = i.replace(">", "")
        #print i
        string+=i+" "

    string+="\n"
    print string
    w1 = open("problems.txt",'a')
    w2 = open("tags.txt",'a')
    w1.write(output)
    w2.write(string)
    os.system("rm 2.txt")




