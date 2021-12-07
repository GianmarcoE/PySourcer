import pyautogui
import time
import sys
import os
from tkinter import Tk
import winsound
import webbrowser
import re

##try:

def save_profile():
    pyautogui.click(1259, 857) #go on the body of the LI profile
    pyautogui.scroll(6000)
    time.sleep(0.2)
    pyautogui.click(702, 621)
    pyautogui.click(702, 651)
    pyautogui.click(702, 591)
    time.sleep(3)

def copy_link():
    pyautogui.click(1259, 857) #go on the body of the LI profile
    pyautogui.scroll(-7000)
    time.sleep(0.2)
    pyautogui.moveTo(505, 975) #click LI profile
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click() #for the drag to(1090, 975)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'c') #click on copy link (to LI profile)
    time.sleep(0.3)
    pyautogui.scroll(6000)
    root = Tk()
    root.withdraw()
    link = root.clipboard_get()
    print(f"\t{link}")
##        webbrowser.open(link)
##        time.sleep(1)
##        pyautogui.hotkey('ctrl', 'shift', 'tab')
##        time.sleep(1)

def ring_end(freq, duration):
    winsound.Beep(freq, duration)
    time.sleep(0.5)
    winsound.Beep(freq, duration)
    time.sleep(0.5)
    winsound.Beep(freq, 2*duration)
    
def main():
    total_saved = 0
    for r in range(1):
        
        time.sleep(1)
        pyautogui.click(690, 623) #click first profile list
        time.sleep(4)

        savedprofiles = 0
            
        for n in range(25):

            if n == 0 or n == 25:
                pass
            else:
                pyautogui.click(1798, 202) #next profile
                time.sleep(4)
                
            pyautogui.rightClick(1220, 515) #right click on profile
            time.sleep(0.5)
            pyautogui.press('up') #go on zbadaj for google inspect
            time.sleep(0.5)
            pyautogui.press('enter') #click it
            time.sleep(4)
            pyautogui.hotkey('ctrl', 'f') #find
            time.sleep(1.5)
            pyautogui.write('profile__int', interval=0.2) #find profile section of HTML
            time.sleep(0.5)
            pyautogui.moveTo(1493, 411)
            time.sleep(0.2)
            pyautogui.scroll(-15)
            time.sleep(0.3)
            pyautogui.rightClick() #right click on the HTML section found
            time.sleep(1)
            pyautogui.press('down', presses=3, interval=0.3) #go to edit HTML
            time.sleep(0.5)
            pyautogui.press('enter') #click it
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a') #select all
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'c') #copy
            root = Tk()
            root.withdraw()
            data = root.clipboard_get()
            #time.sleep(1)

            #file = open("C:\\Users\\ercolani\\OneDrive - TomTom\\Desktop\\Xample.txt", "r", encoding="utf8") #get file
            #data = file.read() #read content of file to string

            spl_word_header = 'class="topcard-requisitions topcard-condensed'
            header = data.partition(spl_word_header)[0]
            spl_word_beginning = 'class="component-card summary-card'
            spl_word_beginning2 = 'class="component-card background-card'
            if spl_word_beginning in data:
                data = header + data.partition(spl_word_beginning)[2] #selects the HTML up until the courses and certificates (excluded)
            elif spl_word_beginning2 in data:
                data = header + data.partition(spl_word_beginning2)[2]
                
            spl_word_end = 'class="recommendation recommendations-card'
            spl_word_end2 ='class="accomplishments component-card'
            if spl_word_end in data:
                data = data.partition(spl_word_end)[0] #selects the HTML up until the courses and certificates (excluded)
            elif spl_word_end2 in data:
                data = data.partition(spl_word_end2)[0]

            mutual_friends = 'class="shared-connections'
            mutual_end = 'class="component-card background-card'
            if mutual_friends in data:
                part1 = data.partition(mutual_friends)[0]
                part2 = data.partition(mutual_end)[2]
                data = part1 + part2

            education = 'class="background-section education-card'
            education_end = '<!----></section>'
            if education in data:
                part1 = data.partition(education)[0]
                part2 = data.partition(education_end)[2]
                data = part1 + part2 #forse puoi creare un def html_edit?
            
            occurrence = ['Java', 'java', 'JEE', 'JAVA', 'skill-name" title="JavaScript'] #get number of occurrences
            lenoccurrence = len(occurrence)

            sumoccurrence = 0
            for i in range(lenoccurrence):
                sumoccurrence += data.count(occurrence[i])

            falspos = ['Java</em>Script', 'Java</em>script', 'java</em>Script',
                        'java</em>script', 'JavaScript', 'Javascript',
                        'Java%', 'skill-name" title="Java',
                        'Java</em> script', 'Java</em> Script',
                       'skill-name" title="Core Java']
            lenfalspos = len(falspos)

            sumfalspos = 0
            for i in range(lenfalspos):
                sumfalspos += data.count(falspos[i])

            netofoccurrences = (sumoccurrence - sumfalspos)

            tester = ["QA", "test engineer", "Test Engineer",
                      "Test Automation", "test automation", "Quality Assurance",
                      "quality assurance", "Quality Engineer", "quality engineer",
                      "Testing Engineer", "in Test", "In Test", "in test",
                      "Test Developer", "Automation Quality", "tester",
                      "Tester", "Automation Engineer", "Test Development",
                      "Test Analyst"]
            lentester = len(tester)

            netdev = [".NET", ".Net", "C#"]
            lennetdev = len(netdev)

            network = ["network", "Network", "System Engineer",
                       "System Analyst", "System Administrator",
                       "Systems Engineer", "Infrastructure Specialist",
                       "Systems Administrator", "Integration"]
            lennetwork = len(network)

            devops = ["DevOps", "devops", "Devops"]
            lendevops = len(devops)

            prodman = ["Product Manager", "Product Management"]
            lenprodman = len(prodman)

            mobiledev = ["Mobile", "Android", "IOS", "iOS"]
            lenmobiledev = len(mobiledev)

            phpdev = ["PHP Developer", "PHP developer"]
            lenphpdev = len(phpdev)

            dataguy = ["Data Analyst", "Data Engineer", "Data Scientist"]
            lendataguy = len(dataguy)

            bidev = ["Business Consultant", "Business Analyst",
                     "Business Intelligence"]
            lenbidev = len(bidev)

            frontenddev = ["Frontend Developer", "Frontend developer", "Front-end Developer",
                           "Front-End Developer", "Front-end developer"]
            lenfrontenddev = len(frontenddev)

            otherwrong = ["Recruiter", "Support", "Salesforce"]
            lenotherwrong = len(otherwrong)

            current_jobtitle_start = 'class="position-item__position-title-link ember-view">'
            current_jobtitle_end = '</a>'
            current_jobtitle_start2 = 'class="ember-view" data-test-grouped-position-title-link="">'
            current_jobtitle_end2 = '</a>'
            first = data.find(current_jobtitle_start)
            second = data.find(current_jobtitle_start2)
            if first == -1:
                first += second + 2
            elif second == -1:
                second += first + 2
            if first < second: #checks index of the two strings to see which one comes first and uses it as current job title
                pass
            else:
                current_jobtitle_start = current_jobtitle_start2
                current_jobtitle_end = current_jobtitle_end2
            current_jobtitle = data.partition(current_jobtitle_start)[2]
            current_jobtitle = current_jobtitle.partition(current_jobtitle_end)[0]
            current_jobtitle = current_jobtitle.strip()

            var = []

            other_dur_start = 'data-test-position-entity-duration="">'
            other_dur_end = '</span>'
            duration_start = 'data-test-grouped-position-entity-date-overall-range="">'
            duration_end = '</div>'

            positions_listed = data.count(other_dur_start) + data.count(duration_start)

            for i in range(positions_listed):
                if i == 0:
                    first = data.find(other_dur_start)
                    second = data.find(duration_start)
                else:
                    first = duration1.find(other_dur_start)
                    second = duration1.find(duration_start)
                if second == -1:
                    second += first + 2
                elif first == -1:
                    first += second + 2
                    
                if first < second:
                    if i == 0:
                        duration1 = data.partition(other_dur_start)[2]
                    else:
                        duration1 = duration1.partition(other_dur_start)[2]
                    duration2 = duration1.partition(other_dur_end)[0]
                    var.append(duration2)
                else:
                    if i == 0:
                        duration1 = data.partition(duration_start)[2]
                    else:
                        duration1 = duration1.partition(duration_start)[2]
                    duration2 = duration1.partition(duration_end)[0]
                    var.append(duration2)

            lenvar = len(var)

            for i in range(lenvar):
                if var[i] != '':
                    if re.findall(".+ yrs .+ mos", var[i]):
                        current_duration = int(var[i][:2]) * 12 + int(var[i][6:-4])
                        var[i] = current_duration
                    elif re.findall(".+ yrs .+ mo", var[i]):
                        current_duration = int(var[i][:2]) * 12 + int(var[i][6:-3])
                        var[i] = current_duration
                    elif re.findall(".+ yr .+ mos", var[i]):
                        current_duration = int(var[i][:2]) * 12 + int(var[i][5:-4])
                        var[i] = current_duration
                    elif re.findall(".+ yr .+ mo", var[i]):
                        current_duration = int(var[i][:2]) * 12 + int(var[i][5:-3])
                        var[i] = current_duration
                    elif re.findall(".+ yrs", var[i]):
                        current_duration = int(var[i][:-4]) * 12
                        var[i] = current_duration
                    elif re.findall(".+ yr", var[i]):
                        current_duration = int(var[i][:2]) * 12
                        var[i] = current_duration
                    elif re.findall(".+ mos", var[i]):
                        current_duration = int(var[i][:-4])
                        var[i] = current_duration
                    elif re.findall(".+ mo", var[i]):
                        current_duration = int(var[i][:-3])
                        var[i] = current_duration
                else:
                    var.remove(var[i])

            lenvar = len(var)
            average_time = sum(var)/lenvar

            separator = '<em class="sh">Java</em>\n  </dt>\n\n    <dd class="skill__endorser-count">\n      <span class="skill__separator" aria-hidden="true">•</span>\n      <span aria-hidden="true" data-test-skill-entity-endorser-count="">'

            likelyhood = ""
            
            for i in range(lenprodman):
                if prodman[i] in current_jobtitle:
                    likelyhood = "No fit: Product"
                    
            for i in range(lennetwork):
                if network[i] in current_jobtitle:
                    likelyhood = "No fit: Network and Infrastructure"
                    
            for i in range(lendevops):
                if devops[i] in current_jobtitle:
                    likelyhood = "No fit: DevOps"

            for i in range(lennetdev):
                if netdev[i] in current_jobtitle:
                    likelyhood = "No fit: C#/.NET Developer"

            for i in range(lentester):
                if tester[i] in current_jobtitle:
                    likelyhood = "No fit: Tester"

            for i in range(lendevops):
                if devops[i] in current_jobtitle:
                    likelyhood = "No fit: DevOps"

            for i in range(lenphpdev):
                if phpdev[i] in current_jobtitle:
                    likelyhood = "No fit: PHP Developer"

            for i in range(lenmobiledev):
                if mobiledev[i] in current_jobtitle:
                    likelyhood = "No fit: Mobile Developer"

            for i in range(lendataguy):
                if dataguy[i] in current_jobtitle:
                    likelyhood = "No fit: Data Professional"

            for i in range(lenbidev):
                if bidev[i] in current_jobtitle:
                    likelyhood = "No fit: BI Developer"

            for i in range(lenfrontenddev):
                if frontenddev[i] in current_jobtitle:
                    likelyhood = "No fit: Frontend Developer"

            for i in range(lenotherwrong):
                if otherwrong[i] in current_jobtitle:
                    likelyhood = "No fit: Other Irrelevant"
                    
            if likelyhood == "":
                if "Architect" in current_jobtitle and var[0] > 16 and "Engineer" not in current_jobtitle and "Developer" not in current_jobtitle:
                    likelyhood = "No fit: Senior Architect"
                elif netofoccurrences == 2:
                    if var[0] < 7:
                        likelyhood = "No fit: Changed job recently"
                    elif average_time < 18 and var[0] < 24:
                        likelyhood = 'No fit: Changes too often'
                    else:
                        likelyhood = "50% good fit"
                elif netofoccurrences >= 3 and netofoccurrences < 7:
                    if var[0] < 7:
                        likelyhood = "No fit: Changed job recently"
                    elif average_time < 18 and var[0] < 24:
                        likelyhood = 'No fit: Changes too often'
                    else:
                        likelyhood = "65% good fit"
                elif netofoccurrences > 6:
                    if var[0] < 7:
                        likelyhood = "No fit: Changed job recently"
                    elif average_time < 18 and var[0] < 24:
                        likelyhood = 'No fit: Changes too often'
                    else:
                        likelyhood = "80% good fit"
                elif netofoccurrences < 2:
                    if var[0] < 7:
                        likelyhood = "No fit: Changed job recently"
                    elif average_time < 18 and var[0] < 24:
                        likelyhood = 'No fit: Changes too often'
                    else:
                        if separator in data:
                            endorsesection = data.partition(separator)[2]
                            potom = endorsesection.split()
                            endorse = potom[0][:-7]
                            if int(endorse) > 4:
                                likelyhood = "50% good fit - Endorsements"
                            else:
                                likelyhood = "No fit: No Java expertise/relevance"
                        else:
                            likelyhood = "No fit: No Java expertise/relevance"

            senior = ["Manager", "Director",
                      "Chief", "CEO", "CTO", "Owner", "Head"]
            lensenior = len(senior)

            too_senior = False
            for i in range(lensenior):
                if senior[i] in current_jobtitle:
                    too_senior = True

            if likelyhood == "50% good fit" or likelyhood == "65% good fit" or likelyhood == "80% good fit" or likelyhood == "50% good fit - Endorsements":
                if too_senior == True:
                    likelyhood = "Too Senior"

            employee = data.count("Your Company")

            if employee != 0:
                likelyhood += " CAREFUL - CURRENT/FORMER EMPLOYEE"
            
            spl_word = 'img title="'
            res = data.partition(spl_word)[2]
            splitted = res.split()
            name = splitted[0] + ' ' + splitted[1][:-1]
            print(n + 1, name, '-', likelyhood)


            time.sleep(1)
            pyautogui.click(1900, 178) # close Inspector
            time.sleep(1.5)

            if likelyhood == "80% good fit" or likelyhood == "65% good fit" or likelyhood == "50% good fit - Endorsements" or likelyhood == "50% good fit":
                save_profile()
                savedprofiles += 1
                total_saved += 1
            elif likelyhood == "Too Senior" or "No fit:" in likelyhood:
                pass
            else:
                copy_link()

        print(f"\nPage {r + 1} - Candidates saved: {savedprofiles}")
        pyautogui.click(1884, 202) #click x to close profiles
        time.sleep(1.5)
        pyautogui.click(126, 77) #click refresh
        time.sleep(14)

    print(f"Total candidates saved: {total_saved}\n")

main()
ring_end(440, 1000)

##except:
##
##    ring_end(700, 1000)

