import time

from bs4 import BeautifulSoup
from selenium import webdriver
import string

def getDriver():
    arguments = webdriver.chrome.options.Options()
    arguments.add_argument("--headless")
    arguments.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(executable_path='/Users/deeptha/Desktop/chromedriver', options=arguments)
    return driver

def getLinks(url):
    driver = getDriver()

    driver.get(url)

    parsed = BeautifulSoup(driver.page_source, 'html.parser')

    categories = parsed.find_all(attrs={"class": "topicRow"})


    links = []
    # print(parsed.prettify())
    for cat in categories:
        for link in cat.find_all('a'):
            links.append(link.get('href'))

    questionLinks = []
    for link in links:
        print(link)
        driver.get(link)
        oldHeight = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 1);")
            oldHeight -= 1
            if oldHeight <= 0:
                break

        questionParsed = BeautifulSoup(driver.page_source, 'html.parser')
        questions = questionParsed.find_all(attrs={"class": "faqEntry"})
        for questionLink in questions:
            questionLinks.append(questionLink.get('href'))
        print(questionLinks)
        print(len(questionLinks))

    with open('links_disneyland.txt', 'w') as f:
        for link in questionLinks:
            f.write(str(link) + '\n')

    driver.close()
    driver.quit()

def getQuestions(fn):
    driver = getDriver()

    with open(fn, 'r') as f:
        links = f.readlines()

    missedLinks = []
    with open('q&a.txt', 'a') as f:
        for link in links:
            driver.get(link[:-1])
            parsed = BeautifulSoup(driver.page_source, 'html.parser')
            text = parsed.find_all(attrs={"class":"text"})
            # print(link)
            try:
                question = text[0].find_all(text = True)
                answer = text[1].find_all(text = True)
                answerString = ''
                # print(answer)
                for i in range(len(answer)):
                    if i == 0 or answer[i-1][-1] == ' ' or (i == len(answer) - 1 and answer[i].strip() in string.punctuation) or answer[i].strip() in string.punctuation or answer[i-1][-1] in ',;:.' or answer[i] == ' ':
                        answerString += answer[i]
                    else:
                        answerString += ', ' + answer[i]
                
                f.write(str(question[0]) + '\n')
                f.write(answerString + '\n')
            except:
                missedLinks.append(link)
    
    with open('missedLink_disneyland.txt', 'w') as f:
        for link in missedLinks:
            f.write(str(link) + '\n')


getQuestions('links_disneyland.txt')