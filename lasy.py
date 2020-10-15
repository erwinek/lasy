from bs4 import BeautifulSoup

#from urllib.request import urlopen, Request

import urllib2
#Fix encoding problems
import sys

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


lista = ["nadl_andrychow", "nadl_bielsko", "nadl_brynek", "nadl_jelesnia",
"nadl_klobuck",
"nadl_koszecin",
"nadl_kup",
"nadl_proszkow",
"nadl_turawa",
"nadl_zawadzkie",
"nadl_brzeg", "nadl_chrzanow","nadl_gidle","nadl_herby","nadl_katowice","nadl_kedzierzyn","nadl_kluczbork",
"nadl_kobior","nadl_koniecpol","nadl_lubliniec","nadl_namyslow",
"nadl_olesno","nadl_olkusz","nadl_opole","nadl_prudnik","nadl_rudy","nadl_rudziniec","nadl_rybnik","nadl_siewierz","nadl_strzelce","nadl_sucha",
"nadl_swierklaniec","nadl_tulowice","nadl_ujsoly","nadl_ustron","nadl_wegierska","nadl_wisla","nadl_zloty_potok","gr_krogulna","gr_niemodlin","zts_swierklaniec"
]

'''


req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))

'''

for index in range(len(lista)):
    url = "https://bip.lasy.gov.pl/pl/bip/dg/rdlp_katowice/" + lista[index] + "/komunikaty_i_ogloszenia"
    #page = urlopen(url)

    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request(url, None, headers)
    html = urllib2.urlopen(req).read()

    #page = urllib.request.urlopen(req)    
    #html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    
    webText = str(soup.get_text().encode('utf-8', errors='ignore'))
    
    fileName = lista[index] + ".txt"    
    
    try:
        prev_file = open(fileName, "r")
        prev_text = prev_file.read()
        prev_file.close()
    except: 
        text_file = open(fileName, "w")
        text_file.write(webText)
        text_file.close()
    
    print(lista[index])
    
    if len(prev_text) != len(webText):
        text_file = open(fileName, "w")
        text_file.write(webText)
        text_file.close()
        print(" !!!!!! NOWY TEXT !!!!!!!!")
        
        sender_email = "erwinek@wp.pl"
        receiver_email = "leszek.kula@gmail.com"
        password = "EZ9w-8vpX.G@5Gf"

        message = MIMEMultipart("alternative")
        message["Subject"] = lista[index]
        message["From"] = sender_email
        message["To"] = receiver_email
    else:
        print("brak zmian")




'''



'''

