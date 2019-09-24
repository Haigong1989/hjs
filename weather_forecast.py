import requests,bs4,smtplib
def sendMail(body):
    sender = "from@tianqi.com"
    receivers = ['380045146@qq.com']
    from_name = 'Weather Monitor'
    subject = 'Raining Today!'
    #msg = '\n'.join(mail)
    try:
        s = smtplib.SMTP_SSL('from@tianqi.com',465)
        s.login(receivers)
        s.sendmail(sender)
        s.quit()
    except smtplib.SMTPException as e:
        print("Error: "+e)
if __name__ == "__main__":
    headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0'}
    url='http://www.tianqi.com/beijing/'
    urlhtml=requests.get(url,headers=headers)
    urlhtml.raise_for_status()
    weatherhtml=bs4.BeautifulSoup(urlhtml.text[:],'html.parser')
    weather=weatherhtml.select('div li p')
    for i in range(len(weather)):
        weathnow=weather[i].getText()
        if weathnow == '有雨':
            sendMail("It's rainy today. Remember to bring your umbrella!")
            print("DONE!")
