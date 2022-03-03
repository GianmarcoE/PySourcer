import pyautogui
import time
import sys
import os
from tkinter import Tk
#import winsound
import webbrowser
import re
from playsound import playsound
from datetime import datetime

try:

    def save_profile():
        pyautogui.click(1259, 857) #go on the body of the LI profile
        pyautogui.scroll(6000)
        time.sleep(0.2)
        pyautogui.click(670, 621)
        pyautogui.click(670, 651)
        pyautogui.click(670, 591)
        time.sleep(4) #3 e la base

    def autosave():
        pyautogui.click(1259, 857) #go on the body of the LI profile
        pyautogui.scroll(6000)
        time.sleep(0.2)
        pyautogui.click(970, 595)
        time.sleep(0.3)
        pyautogui.press('down', presses=5, interval=0.3)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.click(1402, 470)
        time.sleep(1.5)
        pyautogui.write("autosave", interval=0.2)
        time.sleep(1.5)
        pyautogui.click(1565, 644)
##        pyautogui.press('down', presses=2, interval=0.3)
##        time.sleep(0.3)
##        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.scroll(-6000)
        time.sleep(1)
        pyautogui.click(1709, 911)
        time.sleep(4)
        

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

    def ring_end(): #freq, duration in bracket for bip
##        text_val = 'An error occurred and the program has been interrupted'    
##        language = 'en'  
##        obj = gTTS(text=text_val, lang=language, slow=False)    
##        obj.save("interrupt.mp3")
        playsound("sound-of-a-game-failed-trumpet.mp3")
        playsound("interrupt.mp3")
##        winsound.Beep(freq, duration)
##        time.sleep(0.5)
##        winsound.Beep(freq, duration)
##        time.sleep(0.5)
##        winsound.Beep(freq, 2*duration)
        
    def main():

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        hour = 8
        minute = 17
        target = f"0{hour}:{minute}"

        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            if current_time == target or current_time == f"0{hour}:{minute + 1}":
                break
            else:
                time.sleep(59)
            
        total_saved = 0
        savedprofiles = 0
        checkprofiles = 0
        for r in range(2):
            
            time.sleep(1)
            pyautogui.click(690, 623) #click first profile list
            time.sleep(4)

            page_saved = 0
                
            for n in range(25):

                if n == 0 or n == 25:
                    pass
                else:
                    pyautogui.click(1798, 202) #next profile
                    time.sleep(6) #4 e la base
                    
                pyautogui.rightClick(1200, 515) #right click on profile #1220 before
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
                education_end = 'class="skills-card__header'
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
                          "Test Analyst", "Test Lead", "Tests", "Test Consultant",
                          "Test automation", "Test Framework", "Testing Consultant",
                          "testów", "Testów"]
                lentester = len(tester)

                netdev = [".NET", ".Net", "C#"]
                lennetdev = len(netdev)

                network = ["network", "Network", "System Engineer",
                           "System Analyst", "System Administrator",
                           "Systems Engineer", "Infrastructure Specialist",
                           "Infrastructure Engineer", "Systems Administrator",
                           "Integration", "Administrator aplikacji",
                           "Inżynier Systemowy", "inżynier systemowy",
                           "Systems engineer", "Administrator systemu",
                           "Systems administrator", "Administrator IT",
                           "Administrator systemów"]
                lennetwork = len(network)

                devops = ["DevOps", "devops", "Devops", "Site Reliability Engineer",
                          "SRE"]
                lendevops = len(devops)

                prodman = ["Product Manager", "Product Management", "Product Engineer"]
                lenprodman = len(prodman)

                mobiledev = ["Mobile", "Android", "IOS", "iOS", "Xamarin", "Flutter"]
                lenmobiledev = len(mobiledev)

                phpdev = ["PHP Developer", "PHP developer"]
                lenphpdev = len(phpdev)

                dataguy = ["Data Analyst", "Data Engineer", "Data Scientist",
                           "Data Warehouse", "Database Developer", "ETL",
                           "Oracle Developer", "Database Administrator"]
                lendataguy = len(dataguy)

                bidev = ["Business Consultant", "Business Analyst",
                         "Business Intelligence", "BI ", "BI/DW"]
                lenbidev = len(bidev)

                frontenddev = ["Frontend Developer", "Frontend developer", "Front-end Developer",
                               "Front-End Developer", "Front-end developer", "Frontend React Developer",
                               "Frontend Engineer"]
                lenfrontenddev = len(frontenddev)

                otherwrong = ["Recruit", "Support", "Salesforce", "Security", "security",
                              "SAP Commerce", "SAP Developer", "Managing Partner",
                              "AEM", "Resourcer", "Bootcamp", "bootcamp"]
                lenotherwrong = len(otherwrong)

                current_jobtitle_start = 'class="ember-view position-item__position-title-link">'
                current_jobtitle_start2 = 'class="ember-view" data-test-grouped-position-title-link="">'
                current_jobtitle_end = '</a>'
                prev_jobtitle_start = 'class="ember-view position-item__position-title-link">'
                prev_jobtitle_end = '</a>'
                first = data.find(current_jobtitle_start)
                second = data.find(current_jobtitle_start2)

                if first == -1:
                    first += second + 2
                elif second == -1:
                    second += first + 2

                if first < second: #checks index of the two strings to see which one comes first and uses it as current job title
                    current_jobtitle = data.partition(current_jobtitle_start)[2]

                    prev_jobtitle = current_jobtitle.partition(prev_jobtitle_start)[2]
                    prev_jobtitle = prev_jobtitle.partition(prev_jobtitle_end)[0]
                    prev_jobtitle = prev_jobtitle.strip()
                    #check location
                    current_location_start = 'class="background-entity__summary-definition--location" data-test-position-entity-location="">'
                    current_location_end = '</dd>'
                    current_location = current_jobtitle.partition(current_location_start)[2]
                    current_location = current_location.partition(current_location_end)[0]
                    current_location = current_location.strip()
                    current_jobtitle = current_jobtitle.partition(current_jobtitle_end)[0]
                    current_jobtitle = current_jobtitle.strip()
                    itsgroup = False
                elif second < first:
                    current_jobtitle_start = current_jobtitle_start2    
                    current_jobtitle = data.partition(current_jobtitle_start)[2]

                    ### Inizio test nuovo
                    prev_jobtitle_start = 'class="ember-view" data-test-grouped-position-title-link="">'
                    prev_jobtitle_end = '</a>'
                    prev_jobtitle = current_jobtitle.partition(prev_jobtitle_start)[2]
                    prev_jobtitle = prev_jobtitle.partition(prev_jobtitle_end)[0]
                    prev_jobtitle = prev_jobtitle.strip()
                    duration_group_start = 'data-test-grouped-position-entity-duration="">'
                    duration_group_end = '</span>'
                    durationtest1 = current_jobtitle.partition(duration_group_start)[2]
                    durationtest = durationtest1.partition(duration_group_end)[0]
                    if re.findall(".+ yrs .+ mos", durationtest):
                        group_first_duration = int(durationtest[:2]) * 12 + int(durationtest[6:-4])
                    elif re.findall(".+ yrs .+ mo", durationtest):
                        group_first_duration = int(durationtest[:2]) * 12 + int(durationtest[6:-3])
                    elif re.findall(".+ yr .+ mos", durationtest):
                        group_first_duration = int(durationtest[:2]) * 12 + int(durationtest[5:-4])
                    elif re.findall(".+ yr .+ mo", durationtest):
                        group_first_duration = int(durationtest[:2]) * 12 + int(durationtest[5:-3])
                    elif re.findall(".+ yrs", durationtest):
                        group_first_duration = int(durationtest[:-4]) * 12
                    elif re.findall(".+ yr", durationtest):
                        group_first_duration = int(durationtest[:2]) * 12
                    elif re.findall(".+ mos", durationtest):
                        group_first_duration = int(durationtest[:-4])
                    elif re.findall(".+ mo", durationtest):
                        group_first_duration = int(durationtest[:-3])

                    itsgroup = True
                    current_jobtitle = current_jobtitle.partition(current_jobtitle_end)[0]
                    current_jobtitle = current_jobtitle.strip()

##                if itsgroup == False:
##                    for jbt in range(2):
##                        prev_jobtitle_start = 'class="position-item__position-title-link ember-view">'
##                        prev_jobtitle_start2 = 'class="ember-view" data-test-grouped-position-title-link="">'
##                        prev_jobtitle_end = '</a>'
##                        if jbt == 0:
##                            first = data.find(prev_jobtitle_start)
##                            second = data.find(prev_jobtitle_start2)
##                        elif jbt == 1:
##                            if prev_jobtitle_start in prev_jobtitle or prev_jobtitle_start2 in prev_jobtitle:
##                                first = prev_jobtitle.find(prev_jobtitle_start)
##                                second = prev_jobtitle.find(prev_jobtitle_start2)
##                                if first == -1:
##                                    first += second + 2
##                                elif second == -1:
##                                    second += first + 2
##                                if first < second: #checks index of the two strings to see which one comes first and uses it as current job title
##                                    pass
##                                else:
##                                    prev_jobtitle_start = prev_jobtitle_start2
##                        if jbt == 0:
##                            prev_jobtitle = data.partition(prev_jobtitle_start)[2]
##                        elif jbt == 1:
##                            prev_jobtitle = prev_jobtitle.partition(prev_jobtitle_start)[2] #strips twice to get the job title prior to current
##                            
##                    prev_jobtitle = prev_jobtitle.partition(prev_jobtitle_end)[0]
##                    prev_jobtitle = prev_jobtitle.strip()

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

                again = True
                while again == True:
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
                                pass
                            again = False
                        else:
                            var.remove(var[i])
                            again = True

                lenvar = len(var)
                average_time = sum(var)/lenvar

                java_skill_count = '<em class="sh">Java</em>\n  </dt>\n\n    <dd class="skill__endorser-count">\n      <span class="skill__separator" aria-hidden="true">•</span>\n      <span aria-hidden="true" data-test-skill-entity-endorser-count="">'
                javascript_skill_count = '<em class="sh">Java</em>Script\n  </dt>\n\n    <dd class="skill__endorser-count">\n      <span class="skill__separator" aria-hidden="true">•</span>\n      <span aria-hidden="true" data-test-skill-entity-endorser-count="">'
                
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

                if likelyhood == "" and itsgroup == False:
                    if "Minsk" in current_location or "Belarus" in current_location or "India" in current_location:
                        likelyhood = "No fit: Based outside PL CHECK"

                if likelyhood == "":
                    if "Junior" in current_jobtitle and var[0] < 29 and "Java" not in prev_jobtitle:
                        likelyhood = "No fit: Just recently started Java"

                if likelyhood == "":
                    first_exp = 'class="background-entity__summary'
                    first_exp_end = '</dd>\n<!----><!----></dl></div>'
                    if first_exp in data:
                        first_exp = data.partition(first_exp)[2]
                        first_exp = first_exp.partition(first_exp_end)[0]
                    current_description = 'class="background-entity__summary-definition--description'
                    current_description_end = '</dd>\n</dl></div>'
                    if current_description in first_exp:
                        current_description = first_exp.partition(current_description)[2]
                        current_description = current_description.partition(current_description_end)[0]
                        if ".NET" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "C#" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "Python" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "Node.js" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "node.js" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "React" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "JavaScript" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "Angular" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "Swift" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "PHP" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"
                        elif "C++" in current_description and "Java " not in current_description and "Java." not in current_description and "Java)" not in current_description and "Java," not in current_description and "Java/" not in current_description and "JAVA" not in current_description and "Spring" not in current_description and var[0] > 18:
                            likelyhood = "No fit: Not using Java"

                if likelyhood == "":
                    if java_skill_count in data:
                        java_endorsement = data.partition(java_skill_count)[2]
                        potomj = java_endorsement.split()
                        java_endorse = potomj[0][:-7]
                        if javascript_skill_count in data:
                            javascript_endorsement = data.partition(javascript_skill_count)[2]
                            potomjs = javascript_endorsement.split()
                            javascript_endorse = potomjs[0][:-7]
                            if netofoccurrences < 3 and int(javascript_endorse) > 1.5*(int(java_endorse)):
                                likelyhood = "No fit: More focused on FE rather than BE"

                if likelyhood == "" and itsgroup == False:
                    if "Architect" in current_jobtitle and var[0] > 16 and "Engineer" not in current_jobtitle and "Developer" not in current_jobtitle:
                        likelyhood = "No fit: Senior Architect"
                    elif "Architect" in current_jobtitle and var[0] < 16 and var[0] > 6 and "Engineer" not in current_jobtitle and "Developer" not in current_jobtitle:
                        if "Architect" in prev_jobtitle and "Engineer" not in prev_jobtitle and "Developer" not in prev_jobtitle:
                            likelyhood = "No fit: Senior Architect 2"
                        else:
                            pass
                elif likelyhood == "" and itsgroup == True:
                    if "Architect" in current_jobtitle and group_first_duration > 16 and "Engineer" not in current_jobtitle and "Developer" not in current_jobtitle:
                        likelyhood = "No fit: Senior Architect"
                    elif "Architect" in current_jobtitle and group_first_duration < 16 and group_first_duration > 6 and "Engineer" not in current_jobtitle and "Developer" not in current_jobtitle:
                        if "Architect" in prev_jobtitle and "Engineer" not in prev_jobtitle and "Developer" not in prev_jobtitle:
                            likelyhood = "No fit: Senior Architect 2"
                        else:
                            pass
                        
                if likelyhood == "":
                    if var[0] < 7:
                            likelyhood = "No fit: Changed job recently"
                    elif average_time < 18 and var[0] < 24:
                            likelyhood = "No fit: Changes too often"
                    if var[0] > 6 and var[0] < 30 and itsgroup == False:
                        for i in range(lenprodman):
                            if prodman[i] in prev_jobtitle:
                                likelyhood = "No fit: Product till recently"
                                
                        for i in range(lennetwork):
                            if network[i] in prev_jobtitle:
                                likelyhood = "No fit: Network and Infrastructure till recently"
                                
                        for i in range(lendevops):
                            if devops[i] in prev_jobtitle:
                                likelyhood = "No fit: DevOps till recently"

                        for i in range(lennetdev):
                            if netdev[i] in prev_jobtitle:
                                likelyhood = "No fit: C#/.NET Developer till recently"

                        for i in range(lentester):
                            if tester[i] in prev_jobtitle:
                                likelyhood = "No fit: Tester till recently"

                        for i in range(lendevops):
                            if devops[i] in prev_jobtitle:
                                likelyhood = "No fit: DevOps till recently"

                        for i in range(lenphpdev):
                            if phpdev[i] in prev_jobtitle:
                                likelyhood = "No fit: PHP Developer till recently"

                        for i in range(lenmobiledev):
                            if mobiledev[i] in prev_jobtitle:
                                likelyhood = "No fit: Mobile Developer till recently"

                        for i in range(lendataguy):
                            if dataguy[i] in prev_jobtitle:
                                likelyhood = "No fit: Data Professional till recently"

                        for i in range(lenbidev):
                            if bidev[i] in prev_jobtitle:
                                likelyhood = "No fit: BI Developer till recently"

                        for i in range(lenfrontenddev):
                            if frontenddev[i] in prev_jobtitle:
                                likelyhood = "No fit: Frontend Developer till recently"

                        for i in range(lenotherwrong):
                            if otherwrong[i] in prev_jobtitle:
                                likelyhood = "No fit: Other Irrelevant till recently"

                    elif itsgroup == True:
                        if group_first_duration < 30:
                            for i in range(lenprodman):
                                if prodman[i] in prev_jobtitle:
                                    likelyhood = "No fit: Product till recently"
                                    
                            for i in range(lennetwork):
                                if network[i] in prev_jobtitle:
                                    likelyhood = "No fit: Network and Infrastructure till recently"
                                    
                            for i in range(lendevops):
                                if devops[i] in prev_jobtitle:
                                    likelyhood = "No fit: DevOps till recently"

                            for i in range(lennetdev):
                                if netdev[i] in prev_jobtitle:
                                    likelyhood = "No fit: C#/.NET Developer till recently"

                            for i in range(lentester):
                                if tester[i] in prev_jobtitle:
                                    likelyhood = "No fit: Tester till recently"

                            for i in range(lendevops):
                                if devops[i] in prev_jobtitle:
                                    likelyhood = "No fit: DevOps till recently"

                            for i in range(lenphpdev):
                                if phpdev[i] in prev_jobtitle:
                                    likelyhood = "No fit: PHP Developer till recently"

                            for i in range(lenmobiledev):
                                if mobiledev[i] in prev_jobtitle:
                                    likelyhood = "No fit: Mobile Developer till recently"

                            for i in range(lendataguy):
                                if dataguy[i] in prev_jobtitle:
                                    likelyhood = "No fit: Data Professional till recently"

                            for i in range(lenbidev):
                                if bidev[i] in prev_jobtitle:
                                    likelyhood = "No fit: BI Developer till recently"

                            for i in range(lenfrontenddev):
                                if frontenddev[i] in prev_jobtitle:
                                    likelyhood = "No fit: Frontend Developer till recently"

                            for i in range(lenotherwrong):
                                if otherwrong[i] in prev_jobtitle:
                                    likelyhood = "No fit: Other Irrelevant till recently"
                        
                if likelyhood == "":
                    if netofoccurrences == 2:
                        if "Java" in current_jobtitle and "JavaScript" not in current_jobtitle and "Javascript" not in current_jobtitle:
                            likelyhood = "85% good fit *"
                        else:
                            likelyhood = "50% good fit"
                    elif netofoccurrences >= 3 and netofoccurrences < 7:
                        if "Java" in current_jobtitle and "JavaScript" not in current_jobtitle and "Javascript" not in current_jobtitle:
                            likelyhood = "90% good fit *"
                        else:
                            likelyhood = "65% good fit"
                    elif netofoccurrences > 6:
                        if "Java" in current_jobtitle and "JavaScript" not in current_jobtitle and "Javascript" not in current_jobtitle:
                            likelyhood = "95% good fit *"
                        else:
                            likelyhood = "80% good fit"
                    elif netofoccurrences == 1:
                        if "Java" in current_jobtitle and "JavaScript" not in current_jobtitle and "Javascript" not in current_jobtitle:
                            likelyhood = "70% good fit *"
                        else:
                            if java_skill_count in data:
                                java_endorsement = data.partition(java_skill_count)[2]
                                potomj = java_endorsement.split()
                                java_endorse = potomj[0][:-7]
                                if int(java_endorse) > 3:
                                    likelyhood = "50% good fit - Endorsements"
                                else:
                                    likelyhood = "No fit: No Java expertise/relevance"
                            else:
                                likelyhood = "No fit: No Java expertise/relevance"
                    elif netofoccurrences < 1:
                        likelyhood = "No fit: No Java expertise/relevance"

                senior = ["Manager", "Director", "Chief",
                          "CEO", "CIO", "CTO", "Owner", "Head"]
                lensenior = len(senior)

                too_senior = False
                for i in range(lensenior):
                    if senior[i] in current_jobtitle:
                        too_senior = True

                if "good fit" in likelyhood:
                    if too_senior == True:
                        likelyhood = "Too Senior"

                employee = data.count("TomTom")

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

                if "good fit" in likelyhood and "*" not in likelyhood:
                    save_profile()
                    checkprofiles += 1
                    page_saved += 1
                    total_saved += 1
                elif "*" in likelyhood:
                    autosave()
                    savedprofiles += 1
                    page_saved += 1
                    total_saved += 1
                elif likelyhood == "Too Senior" or "No fit:" in likelyhood:
                    pass
                else:
                    copy_link()

            print(f"\nPage {r + 1} - Candidates saved: {page_saved}\n")
            pyautogui.click(1884, 202) #click x to close profiles
            time.sleep(1.5)
            pyautogui.click(126, 77) #click refresh
            time.sleep(14) #THIS TO BE RESTORED TO GO >25

        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        saved_percentage = (float(total_saved)*100)/(float(r+1)*float(n+1))
        print(f"Total candidates saved: {total_saved} out of {(r+1)*(n+1)} ({int(saved_percentage)}%) - {current_time}")
        print(f"{checkprofiles} to be checked, {savedprofiles} to be contacted\n")

    main()
    #ring_end(440, 1000)
    playsound("success-sound-effect.mp3")
    playsound("success.mp3")

except:
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    ring_end()
    print(f"\nProgram interrupted at {current_time}")
