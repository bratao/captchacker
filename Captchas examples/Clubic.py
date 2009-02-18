#!coding: utf-8
import urllib2
import os
import cookielib
import time
import re

#TRACEBACK
import traceback
import sys
def Myexcepthook(type, value, tb):
        lines=traceback.format_exception(type, value, tb)
        f=open('error.txt', 'a')
        f.write("\n".join(lines))
        f.close()
        print "\n".join(lines)
sys.excepthook=Myexcepthook


#INSTALLATION DU COOKIE
cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'), ('Connection' , 'Keep-Alive')]
urllib2.install_opener(opener)


def html(s):
    f=open("a.html","w")
    f.write(s)
    f.close()
    os.startfile("a.html")

def request(URL, data=None, headers={}):
    req = urllib2.Request(URL, data)
    for key, content in headers.items():
        req.add_header(key, content)
    handle = urllib2.urlopen(req)
    data=handle.read()
    return data


def write_file(file, s):
    f=open(file, 'wb')
    f.write(s)
    f.close()



LIEN_IMAGES = "http://www.clubic.com/api/creer_un_compte.php"




def save_image(i):
    data = request(LIEN_IMAGES)
    captcha_urls = re.findall('(http://www.clubic.com/divers/image-code.php\?refresh=([^"]*))"', data)
    
    if not captcha_urls:
        print "No captcha link..."
        return
    
    data = request(captcha_urls[0][0])
    write_file("Captchas Clubic/%s.png"%captcha_urls[0][1], data)
    print i, captcha_urls[0][1]


for i in range(100):
    save_image(i)

raw_input()

