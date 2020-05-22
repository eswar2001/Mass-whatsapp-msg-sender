# Mass-whatsapp-msg-sender

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://github.com/eswar2001/Mass-whatsapp-msg-sender)

:smile: [Download the repo](https://github.com/eswar2001/Mass-whatsapp-msg-sender/archive/master.zip) :smile:

### Requirements

- [Latest version of Python](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)
- [Latest version of chrome](https://www.google.com/chrome/)
- [Latest version of Pyautoit](https://github.com/jacexh/pyautoit)
- [Geckodriver for firefox](https://github.com/mozilla/geckodriver/releases)
- [ChromeDriver for chrome and it is version specific](https://chromedriver.chromium.org/)
- To know your chrome version got to settings/help

### Code to be executed/Procedure

- [Latest version of Python](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)
- [Latest version of chrome](https://www.google.com/chrome/)
- [Geckodriver for firefox](https://github.com/mozilla/geckodriver/releases)
- [ChromeDriver for chrome and it is version specific](https://chromedriver.chromium.org/)
- To know your chrome version got to settings/help
- [as on 21-05-2020 the latest exe files are here](https://github.com/eswar2001/Mass-whatsapp-msg-sender/tree/master/resources/)

### Code to be executed irrespective of platform

    python -m pip install --upgrade pip
    pip install selenium
    pip install PyAutoIt
    pip install os-sys
    pip install python-csv

### Platform: Windows

ChromeDriver used: If this versions becomes outdated or gives problem
download the latest version from <a href ="http://chromedriver.chromium.org/downloads"> Download Link </a>
(or)
FirefoxDriver used: [Geckodriver for firefox](https://github.com/mozilla/geckodriver/releases)

After downloading the driver you will have to add the location of those exe files in path.Chrome is prefered if your using firefox then
modify the code in whatsapp.py file. by default it is using chrome drivers just change the below code.

![chrome](https://github.com/eswar2001/Mass-whatsapp-msg-sender/blob/master/images/code.jpg)

> driver = webdriver.Chrome()
>
> to
>
> driver = webdriver.Firefox()

### Platform: Linux

    pip install webdriver-manager

### How to run the script?

    step-1:git clone or download the zip of this repo then cd Mass-whatsapp-msg-sender
    step-2:get your mobile ready to scan the qr code
    step-3:I suggest you to use chrome so update to the latest version
    step-4:Type the message in the 'message.txt' file
    step-5:Type the phone numbers in the 'numbers.csv' each number should start with country code without '+'
    step-6:each number should be in seperate line without comas or colon's
    step-7:then run the below command in the terminal or cmd.
              python whatsapp.py
    step-8:as soon as the browser loads the whatsapp desktop webpage, scan the qr with your mobile
    step-9:now time to relax

:relieved:

### NOTE: For Sending Files:

Paste your document in the Documents Folder in the directory.Then go to whatsapp.py file and paste the document name along with file extension 
in the variable $doc_filename.

### NOTE: For contacts:

Do enter your country code then contact number.

> Use: 919999999999
>
> Don't Use: +919999999999
> <a href="https://www.wikihow.tech/Scan-a-QR-Code-on-WhatsApp" target="__blank"> For scanning qr to get whatsapp web using ios or android devices</a>

![how to put numbers in the csv file](https://github.com/eswar2001/Mass-whatsapp-msg-sender/blob/master/images/numberslist.jpg)

#### :star: the repo :+1:
