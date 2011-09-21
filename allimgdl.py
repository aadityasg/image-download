import urllib
from BeautifulSoup import BeautifulSoup as bs
url = raw_input("enter the url of the page here :")
homeurl=raw_input("enter the main domain url")
http=urllib.urlopen(url).read()
soup=bs(http)
listoftags=soup.findAll('img')
print listoftags
totalimages=len(listoftags)
for i in range(totalimages):
  lpos=0
  hpos=0
  imgurl=str(listoftags[i])
  print imgurl
  imgurllist=list(imgurl)
  #print imgurl
  #print imgurllist
  lenofurl=len(imgurllist[i])
  for j in range(100000):
    #if imgurllist[j]==':' and imgurllist[j-1]=='s':
    #  lpos=j-5
    #if imgurllist[j]==':' and imgurllist[j-1]=='p':
    #  lpos=j-4
    if imgurllist[j]=='c' and imgurllist[j-1]=='r' and imgurllist[j-2]=='s':
      lpos=j+3
    if imgurllist[j]=='"' and imgurllist[j-1]=='g':
      hpos=j
      break;
  finalurl=imgurl[lpos:hpos]
  finalurllist=list(finalurl)
  if finalurllist[0]!='h':
    finalurl=homeurl+"/"+finalurl
  print finalurl
  #print lpos,hpos
  f=open("/home/aaditya/blogdl/img%d"%i+".jpg",'wb')
  f.write(urllib.urlopen(finalurl).read())
  f.close()
  

