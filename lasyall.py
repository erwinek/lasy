from bs4 import BeautifulSoup

#from urllib.request import urlopen, Request

import urllib2
#Fix encoding problems
import sys

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


listaKato = ["nadl_andrychow", "nadl_bielsko", "nadl_brynek", "nadl_jelesnia","nadl_klobuck","nadl_koszecin","nadl_kup","nadl_proszkow","nadl_turawa","nadl_zawadzkie",
"nadl_brzeg", "nadl_chrzanow","nadl_gidle","nadl_herby","nadl_katowice","nadl_kedzierzyn","nadl_kluczbork",
"nadl_kobior","nadl_koniecpol","nadl_lubliniec","nadl_namyslow",
"nadl_olesno","nadl_olkusz","nadl_opole","nadl_prudnik","nadl_rudy","nadl_rudziniec","nadl_rybnik","nadl_siewierz","nadl_strzelce","nadl_sucha",
"nadl_swierklaniec","nadl_tulowice","nadl_ujsoly","nadl_ustron","nadl_wegierska","nadl_wisla","nadl_zloty_potok","gr_krogulna","gr_niemodlin","zts_swierklaniec",
]

rdlpKrakow =["nadl_brzesko", "nadl_dabrowa_tarnowska", "nadl_debica", "nadl_gorlice", "nadl_gromnik", "nadl_kroscienko", "nadl_krzeszowice", "nadl_limanowa", "nadl_losie", 
"nadl_miechow", "nadl_myslenice", "nadl_nawojowa", "nadl_niepolomice", "nadl_nowy_targ", "nadl_piwniczna", "nadl_stary_sacz" ] 



for index in range(len(listaKato)):
    url = "https://bip.lasy.gov.pl/pl/bip/dg/rdlp_katowice/" + listaKato[index] + "/komunikaty_i_ogloszenia"
    #page = urlopen(url)

    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request(url, None, headers)
    html = urllib2.urlopen(req).read()

    #page = urllib.request.urlopen(req)    
    #html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    
    webText = str(soup.get_text().encode('utf-8', errors='ignore'))
    
    fileName = listaKato[index] + ".txt"    
    
    prev_text = ""
    try:
        prev_file = open(fileName, "r")
        prev_text = prev_file.read()
        prev_file.close()
    except: 
        text_file = open(fileName, "w")
        text_file.write(webText)
        text_file.close()
    
    print(listaKato[index])
    
    if len(prev_text) != len(webText):
        text_file = open(fileName, "w")
        text_file.write(webText)
        text_file.close()
        print(" !!!!!! NOWY TEXT !!!!!!!!")
        
        senderEmail = "erwinek@wp.pl"
        receiverEmail = "leszek.kula@gmail.com"
        password = "EZ9w-8vpX.G@5Gf"

        message = MIMEMultipart("alternative")
        message["Subject"] = listaKato[index]
        message["From"] = senderEmail
        message["To"] = receiverEmail
		
        # Create the plain-text and HTML version of your message
        text = "https://bip.lasy.gov.pl/pl/bip/dg/rdlp_katowice/" + listaKato[index] + "/komunikaty_i_ogloszenia" + webText

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        message.attach(part1)

        msg = MIMEText("WARNING, FILE DOES NOT EXISTS, THAT MEANS UPDATES MAY DID NOT HAVE BEEN RUN")

        msg['Subject'] = "WARNING WARNING ON FIRE FIRE FIRE!"

     
        s = smtplib.SMTP_SSL('smtp.wp.pl:465')
        s.login(senderEmail,password)
        s.sendmail(senderEmail,receiverEmail, message.as_string())
        s.quit()

    else:
        print("brak zmian")


for index in range(len(rdlpKrakow)):
    url = "https://bip.lasy.gov.pl/pl/bip/dg/rdlp_krakow/" + rdlpKrakow[index] + "/komunikaty_i_ogloszenia"
    #page = urlopen(url)

    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request(url, None, headers)
    html = urllib2.urlopen(req).read()

    #page = urllib.request.urlopen(req)    
    #html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    
    webText = str(soup.get_text().encode('utf-8', errors='ignore'))
    
    fileName = rdlpKrakow[index] + ".txt"    
    
    try:
        prev_file = open(fileName, "r")
        prev_text = prev_file.read()
        prev_file.close()
    except: 
        text_file = open(fileName, "w")
        text_file.write(webText)
        text_file.close()
    
    print(rdlpKrakow[index])
    
    if len(prev_text) != len(webText):
        text_file = open(fileName, "w")
        text_file.write(webText)
        text_file.close()
        print(" !!!!!! NOWY TEXT !!!!!!!!")
        
        sender_email = "erwinek@wp.pl"
        receiver_email = "leszek.kula@gmail.com"
        password = "EZ9w-8vpX.G@5Gf"

        message = MIMEMultipart("alternative")
        message["Subject"] = rdlpKrakow[index]
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = "https://bip.lasy.gov.pl/pl/bip/dg/rdlp_katowice/" + listaKato[index] + "/komunikaty_i_ogloszenia" + webText

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        message.attach(part1)

        msg = MIMEText("WARNING, FILE DOES NOT EXISTS, THAT MEANS UPDATES MAY DID NOT HAVE BEEN RUN")

        msg['Subject'] = "WARNING WARNING ON FIRE FIRE FIRE!"

     
        s = smtplib.SMTP_SSL('smtp.wp.pl:465')
        s.login(senderEmail,password)
        s.sendmail(senderEmail,receiverEmail, message.as_string())
        s.quit()
    else:
        print("brak zmian")


'''



'''

