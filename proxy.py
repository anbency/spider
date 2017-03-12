#-*-coding=utf-8-*-


import sqlite3
import urllib2
import random
from bs4 import BeautifulSoup
import re
import os
import shutil
import chardet
'''
import urllib2
import proxy
from bs4 import BeautifulSoup
i = 9
webpage = proxy.getWebpage("http://helloyesyes.iteye.com/blog/search?page=" + str(i) + "&query=kernel",i)
webpage.getPageContent()
webpage.parseHTML(open("text"+ str(i) + (".html")))

'''
class getWebpage():

    def __init__(self, url, page):
        self.user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        self.header = {"User-Agent": self.user_agent}
        self.url = url
        self.page = str(page)

    def parseHTML(self,html):
        soup = BeautifulSoup(html, "lxml")

        targeturl = "http://helloyesyes.iteye.com"
        targetlist = []
        #print soup.find_all(href = re.compile("\/blog\/[0-9]+$"))
        for x in soup.find_all(href = re.compile("\/blog\/[0-9]+$")):
            #s = x.encode('utf-8')
            print x.string; print x.get('href')
            #print chardet.detect(x.string)
            #print chardet.detect(x.get('href'))
            targetlist.append([x.string, targeturl + x.get('href')])
            #targetlist.append(s)
        print targetlist

        if os.path.exists('output'):
            shutil.rmtree('output')
        os.mkdir('output')

        for x in targetlist:
            req=urllib2.Request(x[1],headers=self.header)
            try:
                resp=urllib2.urlopen(req,timeout=10)
	        
                if resp.code==200:
                    print "work"
                else:
                    print "not work"
                
            except :
                print "except Not work"
            html = resp.read()
             
            self.saveHtml("output//",x[0],html)


    def getPageContent(self):
	#proxy = create_proxy()
	#proxy_support=urllib2.ProxyHandler(proxy)
    	#opener=urllib2.build_opener(proxy_support)
    	#urllib2.install_opener(opener)
        #html = opener.open(self.url)
        req=urllib2.Request(self.url,headers=self.header)
        try:
            #timeout 设置为10，如果你不能忍受你的代理延时超过10，就修改timeout的数字
            resp=urllib2.urlopen(req,timeout=10)
	    
            if resp.code==200:
                print "work"
            else:
                print "not work"
            
        except :
            print "Not work"
         
        html = resp.read()

        filename = "text" + self.page
        #self.saveHtml("", filename,html) 
        self.parseHTML(html)

    def saveHtml(self,path, file_name,file_content):  
        with open (path + file_name +".html","wb") as f:  
            f.write( file_content ) 

def create_proxy():
    dbname="proxy.db"
    try:
        conn=sqlite3.connect(dbname)
    except:
        print "Error to open database%" %self.dbname
    proxys = []
    c = conn.cursor()
    query_cmd='''
    select IP,PORT from PROXY;
    '''
    cursor=c.execute(query_cmd)
    proxys = c.fetchall()
    print proxys

    (IP,PORT) = random.choice(proxys)
    proxy={'http':IP+':'+PORT}
    print proxy

    c.close()
    conn.close()

    return proxy



    #dream_url = http://helloyesyes.iteye.com/blog/search?page=2&query=kernel

if __name__ == "__main__":
    for i in range(9,10):
    	dream_url = "http://helloyesyes.iteye.com/blog/search?page="+ str(i) + "&query=kernel"
	print dream_url
    	webpage = getWebpage(dream_url,i)
        webpage.getPageContent()
        #webpage.parseHTML(open("text9.html").read())
    
