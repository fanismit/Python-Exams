import urllib.request
print("please insert a webpage") 
x=input()
x="https://"+x
try:
    fp = urllib.request.urlopen(x)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")   
    fp.close()
    print(mystr)
    print("the number of <p> is:"," ",mystr.count("</p>")," ","the number of <br> is "," ",mystr.count("<br>")," ","the number of href is:"," ",mystr.count("href"))# Ο τρόπος που βρίσκω τις αλλαγές γραμμής μέσω της ετικέτας <br> <p> και τους συνδέσμους
except:
    print("the url is not valid")





