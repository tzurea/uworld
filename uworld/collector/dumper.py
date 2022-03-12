import json
import sqlite3
import requests


cookies = {
    '_gcl_au': '1.1.1654644536.1646711823',
    '_rdt_uuid': '1646711824359.8088cc27-b824-4530-9843-a79da63501b6',
    '_fbp': 'fb.1.1646711824883.1306743491',
    '_pin_unauth': 'dWlkPU9UZzFOV1JoWmpJdE1ETmpPUzAwTUdVMkxUazNaVGN0TVRaaE16TXlNbUl6WlRJNA',
    '_clck': 'f7q65m|1|ezl|0',
    'uts_id': 'uts1646711861.829',
    'tracker_device': 'f1823d86-448f-46c0-b000-bed62521e257',
    'consentCookieUWorld': 'true',
    'lvn-7231878': '61daed0a115cf9117d6ef678',
    '_gid': 'GA1.2.1027890366.1646968104',
    'lcid': 'LC1646966396.2332996',
    '__utmz': '188023084.1646977256.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '_ga_0K1JDYWLEE': 'GS1.1.1646977273.2.1.1646977350.0',
    '_ga': 'GA1.2.1679904444.1646711823',
    'LCUTS_UID_900134': '900134',
    'ASP.NET_SessionId': 'hr25a14vlthhfhu33rnsrpuc',
    '_gat_gtag_UA_539627_1': '1',
    '_gat_UA-539627-1': '1',
    '__utma': '188023084.1679904444.1646711823.1646996189.1647051197.5',
    '__utmc': '188023084',
    '__utmt': '1',
    '__utmb': '188023084.1.10.1647051197',
    '_uetsid': '83b0d5e0a0e811ecbcfd77596ae6cd42',
    '_uetvid': 'd08fb3109e9311ecad7131263912ad65',
    'BIGIP': '!zadjM1LnyqPAxx+QUYeKStxuJaLGLgEQ5AzuiAFqAgfLH3CbR8AyGSoDuH41EOCE+BxeI0aB8IcxruU=',
}

headers = {
    'authority': 'www.uworld.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'sPb5argcA5amwh4a6P7gge4QBNL9Gj9wxO9ZdEJxc9IAUGt25Qb/J5LZou+eo5rRubX3SrKxY30of5wqqqHOUezSQZ8jZ7lWnhCz1vOX0ZF8SzK7iQKp+t5ZWvpyDb5FfftgWnRxIShWI4cQe3Y1moVo6uZV2hB/S9/mhAO7qW3XNDEJ5lxMNESScyNEzfqoZ0IAbhr9/9ESWgOo9f/J94J1RCyK4yy6R+lNFenPLXRN1lAqPpdKfNGvb7hN7M+b5uGVtXTAoWLsZWXqdK9p1mqsPCpeE4c2Z7q7aQvR69awjhG9/hF8lTbeZZ3q96+zl+dfMTf3k1LaUVpRKNiU8zzW+z6qdttUw0G75xKU1iWtXJirG7mdHE/mdEXR7or/Kskj1UGX22myO4847+cDw1bWhaq4tFd9DhaQr7/72evWb/ayirecl9i7KNrA/F1JsY80UE8LfxdpzkWNh+xBQSmgMXijoFfpZANCEsMEF9CqrmHZDNxhdcjkZrnWSchB5TWu0jkdHoS/mlbi4aVcaM0D8l9Oqsi6hLxOoO9MlHbVYUPAaTgpHMjys7mlcf1jQuOfA3rDmWybUiYCQogBbjowC+ktJ4th5Ioqr/MZa803GDducoSM5culZWvs8MOVEDLPdEIXBI5vBVIsRp/7/xCmcHinUjQscEL6sZPH4Npg/PTa/whymmJEOvMA3vErchmc8oej4Qsl5LuUVesaLtamQbiw1Sy8ztj01oLqOxYInIO3U5Ik0Hqscim5okvPxAvLRUSBbUy1D5RHC52vpISnp3CpmsIjKDHOxWyWECG/NqVYpLYhlhaMA1uN02Xzz1wsTuAlgq6/HF6WlUUl+ggbH/RkjmLDxGb8HDjAmW4mAgP4AidbYOnWKUty7iG8nrDuyY2bin1E6+FWCsinu2Eze1klubfoWEYhqiRgM1IgKnsBfBD6zoHNen4tJ0sLpDuwwtAHKZ2lV9Kor3tH2I0qAwOWI/NoI02D3+qV2vRfsvn4uYSUmUGBtK24lODJTks/7ChA+KEXvL0s/SjGR7A5kau9gWu/EF+zdw5F0x4LxfZW8qsvGIeitEP692XT78h9zrLMfKoFa0dJT5uZviqsGGn2zdM+jGXJinjS6B7DsCfdgEH3aqobrRyBzxned1jWgMRl+ZpMuIszcpzgq0Nr4mIJmL8F5WMqgKUHPZEQgKa22Puo0PO8XNqU2ZtD6S1ogyq1rER831sxP1fHq6jaOggxR2FQdcsPV78P/eZ/heZ/8DNPb06rZ9mi+7veCZIe+YYfHT++D8B4KoSTGjMLlE7xhYIslhCZyYoi0eE=',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'api-uwsub-key': 'c8+WDO4MTsHcDnRgn+jWnwWYFJkM7u23AQKFHSTTEd2kaUfy6J62JnHI27Wn3MWtH+TMwKI2B3HvA8rfrX4RydZzmCs8m2IpgU2tKxMVUtjsUsdn8dXBzl9CIxOtR/fxS8Enm8/ncpQNpFEXwF9NxGxBcYsLNV7L6GyP8Os3ApGUXSFmR5xCxNDLphGImbjrd07KYpIvxJ3xmqcqPF813sOObl4OyXuWLfANHq9koUxwGRiBzkLtcEfGsMKCJAvnCjy4KLVt54EQ2rhL6A1DWzNdk4e0UThuJgzFbaB388Ua4PwJAznOhvLb6QUHLgqFMNc7yfyVEe10PSwBgaFGMk9Kmvx3Xsp/2gDIbnJ2qJqDnKiMqW5NrdRxYMjjUxve/wndyywme4j2qVoCDyOvUxZtMqQbUHOV28hqgOumvpLkcuLgZPXE8uOyd1sTHBRI3fjQYoYN22tclxwtjj1ZYy/VrW482xP8IKsllzgdavpKfwOADJEFJpX2/dTm2iIU9SUZ2AIPyToGqv/4p+kkdgGX/qACl0MAkWI/dYyTTdCVbsn3fiZ4oZgJOvBEoneV2PhBfmNkWQKbB2OTaOTG+byBLPi+Ehi+GGSdcShHIe+gyjmLnwuHZDHiiQj5sAQHxSzOkbhmBAOElFdT5wFo/MEHRzUbxkKM+ghGQxn4tOTGoSubwkvVEg09KbBbxO3JH9jYR/Q/a4hQQydWjvngIQ==',
    'sec-ch-ua-platform': '"Linux"',
    'authkey': 'QQRq1ZZwmNl7TePz6R3pnnR6nxlvtROUX7ihzE30HovY6zZ46XIx76a9SB/irCSh4r9xRg/f7tJPIj4Aa3+ootrnrqFDXnGJmf5h5+F9H6ytlORhtLG3fvLutIvpRAF+eXj2HG+qMA82k30Xu6/91KkYOpiZs8C42ZhOkzlGlj8ffPBDrCFQHjiXSVCsxkyldfEjnjRILGZajdLQvNmoqlNW9mpKMJs9pJ7Dq+MAm1mly1p7qSNPm+d0S4fKb2hShQ86dKmFn5ZxIwSHY5dCTA==',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.uworld.com/courseapp/usmle/v34/previoustests/7231878',
    'accept-language': 'en-US,en;q=0.9',
}


json_create_test_data = {
    'objData': {
        'testMode': 4,
        'testSource': 1,
        'questionMode': 0,
        'superDivisioIds': [
            240010,
            240007,
            240009,
            240008,
            240002,
            240003,
            240004,
            240005,
            240006,
        ],
        'divisionIds': [
            201,
            216,
            203,
            202,
            217,
            211,
            212,
            205,
            215,
            206,
            210,
            213,
            222,
            208,
            220,
            219,
            214,
            218,
            204,
            207,
            209,
            221,
        ],
        'topics': [],
        'questionIds': '',
        'maxQuestionCount': 1,
        'autoSelectMaxQuestion': False,
        'isQuickTest': None,
        'isAllSubjectsSelected': True,
        'isAllSystemsSelected': True,
        'allowCalculator': None,
        'testTypeId': None,
        'sectionId': 1012,
        'difficultyLevelId': None,
        'formatTypeIds': None,
        'questionModes': '0',
    },
}

create_question_table = """
CREATE TABLE questions (
            exhibits TEXT,
            sequenceId INTEGER,
            questionId INTEGER PRIMARY KEY,
            questionIndex INTEGER,
            questionText TEXT, 
            questionHeader TEXT,
            explanationText TEXT, 
            abstractId INTEGER,
            qbankId INTEGER,
            sectionId INTEGER,
            section TEXT,
            subjectId INTEGER,
            subject TEXT,
            secondarySubjectId INTEGER,
            secondarySubject TEXT,
            systemId INTEGER,
            system TEXT,
            topicId INTEGER,
            topic TEXT,
            titleId INTEGER,
            title TEXT,
            topicAttributeId INTEGER,
            topicAttribute TEXT,
            correctAnswer TEXT,
            userAnswer TEXT,
            parentQuestionId INTEGER,
            subParentQuestionId INTEGER,
            questionSetSequenceId INTEGER,
            questionSetCount INTEGER,
            questionToAnswerBeforeThis INTEGER,
            answerChoiceList TEXT,
            formatTypeId INTEGER,
            questionTypeId INTEGER,
            highlights INTEGER,
            isCorrect TEXT,
            isIncorrect TEXT,
            isMarked TEXT,
            isOmitted TEXT,
            isQuestionDirty TEXT,
            isAnswerChoiceDisabled TEXT,
            isQuestionDisabled TEXT,
            questionMappingReferencesList TEXT,
            questionMedia TEXT,
            timeSpent INTEGER,
            othersAvgTimeSpent INTEGER,
            notes TEXT,
            peopleTaken INTEGER,
            hotspotImageUrl TEXT,
            lastUpdatedDate TEXT,
            correctPercentile INTEGER ,
            isSubmitted TEXT,
            isActive TEXT,
            activeStatusId INTEGER,
            hint TEXT,
            allowCalculator TEXT,
            difficultyLevelId TEXT,
            additionalText TEXT,
            mobileExcerpt TEXT,
            passageExcerpt TEXT,
            confSurveyValue INTEGER,
            timePerQuestionInMilliSec INTEGER,
            answerHeader TEXT,
            standards TEXT,
            totalTimeSpentReview INTEGER,
            dailyTimeSpentReview INTEGER,
            dailyTimeSpent INTEGER,
            isHintUsed TEXT,
            examYear INTEGER,
            newExamYearQuestionIndex INTEGER,
            vocabularyList TEXT,
            copyrightId TEXT,
            copyrightText TEXT,
            frequentHighlights TEXT,
            totalWeight TEXT,
            weightScored TEXT,
            maxAnswerSelection INTEGER,
            scoreTypeId TEXT,
); 

"""

create_flashcards_table = """
CREATE TABLE flashcards (
             flashCardId   INTEGER PRIMARY KEY,
             deckId   INTEGER,
             deckName   TEXT,
             deckColor   TEXT,
             questionIndex   INTEGER,
             abstractId   INTEGER,
             frontText   TEXT, 
             frontMedia   TEXT,
             backText   TEXT,
             backMedia   TEXT,
             tags   TEXT,
             subjectId   INTEGER,
             subject   TEXT,
             systemId   INTEGER,
             system   TEXT ,
             sectionId   INTEGER,
             section   TEXT,
             sequenceId   INTEGER,
             isCorrect   TEXT,
             isMarked   TEXT,
             dateCreated   TEXT,
             updateDateCreated   TEXT,
             isLocked   TEXT,
             topicId   INTEGER,
             isDeleted   TEXT,
             markId   TEXT,
             studyStatusId   TEXT,
             studyStepCount   TEXT,
             studyDueDate   TEXT,
             studyPreviousInterval   TEXT,
             isCustomStudyDeck   TEXT,
             customStudyDeckSettings   TEXT,
             subscriptionId   INTEGER,
);

"""


generate_new_test_uri = 'https://www.uworld.com/clientapp/webapi/QbankClient/GenerateNewTest/'
previous_test_uri = 'https://www.uworld.com/clientapp/webapi/QbankClient/GetTestRecords/2/0'

def post_request(url, headers, cookies, json_data):
    response = requests.post(url, headers=headers, cookies=cookies, json=json_data)
    print(response.text)
    response = json.loads(response.text)
    return response

def get_request(url, headers, cookies):
    response = requests.get(url, headers=headers, cookies=cookies)
    print(response.text)
    response = json.loads(response.text)
    return response

def create_connection(db_path):
    connection = sqlite3.connect(db_path)
    return connection

def execute_sql(connection, sql_execute_statement, sql_entries):
    cursor = connection.cursor()
    cursor.execute(sql_execute_statement, sql_entries)
    connection.commit()


db_path = '/home/zuplex/Argon/uworld/build/.local/share/uworld/db/usmle-data.db'

sql_insert_question = "INSERT OR IGNORE INTO questions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
sql_insert_flashcard = "INSERT OR IGNORE INTO flashcards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

connection = create_connection(db_path)


# Get the test id by sending a request to test generator uri
# test_id = {'testId': 247338154, 'possibleQuestionCounts': None}


# Create a new uri by adding the test id

def insert_from_test_id(test_id):
    test_url = 'https://www.uworld.com/clientapp/webapi/QbankClient/getTest/{}/null/null/undefined'.format(test_id)

    # Get the flashcard and question list by sending a get request to test uri

    test_uri_response = get_request(test_url, headers, cookies)
    question_list = test_uri_response['questionList']
    flashcard_list = test_uri_response['flashCardList']

    # questionList = [{},{},{} .... ]
    # flashCardList = [{},{},{} .... ]



    for value in question_list:
        exhibits = value['exhibits'] 
        sequenceId = value['sequenceId']
        questionId = value['questionId'] 
        questionIndex = value['questionIndex']
        questionText = value['questionText']
        questionHeader = value['questionHeader'] 
        explanationText = value['explanationText']
        abstractId = value['abstractId']
        qbankId = value['qbankId']
        sectionId = value['sectionId']
        section = value['section']
        subjectId = value['subjectId']
        subject = value['subject']
        secondarySubjectId = value['secondarySubjectId']
        secondarySubject = value['secondarySubject']
        systemId = value['systemId']
        system = value['system']
        topicId = value['topicId']
        topic = value['topic']
        titleId = value['titleId']
        title = value['title']
        topicAttributeId = value['topicAttributeId']
        topicAttribute = value['topicAttribute']
        correctAnswer = value['correctAnswer']
        userAnswer = value['userAnswer']
        parentQuestionId = value['parentQuestionId'] 
        subParentQuestionId = value['subParentQuestionId']
        questionSetSequenceId = value['questionSetSequenceId']
        questionSetCount = value['questionSetCount']
        questionToAnswerBeforeThis = value['questionToAnswerBeforeThis']
        answerChoiceList = json.dumps(value['answerChoiceList']) 
        formatTypeId = value['formatTypeId'] 
        questionTypeId = value['questionTypeId']
        highlights = value['highlights']
        isCorrect = value['isCorrect']
        isIncorrect = value['isIncorrect']
        isMarked = value['isMarked']
        isOmitted = value['isOmitted']
        isQuestionDirty = value['isQuestionDirty']
        isAnswerChoiceDisabled = value['isAnswerChoiceDisabled']
        isQuestionDisabled = value['isQuestionDisabled']
        questionMappingReferencesList = json.dumps(value['questionMappingReferencesList'])
        questionMedia = json.dumps(value['questionMedia'])
        timeSpent = value['timeSpent']
        othersAvgTimeSpent = value['othersAvgTimeSpent']
        notes = value['notes']
        peopleTaken = value['peopleTaken']
        hotspotImageUrl= value['hotspotImageUrl']
        lastUpdatedDate = value['lastUpdatedDate']
        correctPercentile = value['correctPercentile']
        isSubmitted = value['isSubmitted'] 
        isActive = value['isActive']
        activeStatusId = value['activeStatusId']
        hint = value['hint'] 
        allowCalculator = value['allowCalculator']
        difficultyLevelId = value['difficultyLevelId']
        additionalText = value['additionalText']
        mobileExcerpt = value['mobileExcerpt']
        passageExcerpt = value['passageExcerpt']
        confSurveyValue = value['confSurveyValue'] 
        timePerQuestionInMilliSec = value['timePerQuestionInMilliSec'] 
        answerHeader = value['answerHeader']
        standards = value['standards']
        totalTimeSpentReview = value['totalTimeSpentReview']
        dailyTimeSpentReview = value['dailyTimeSpent']
        dailyTimeSpent = value['dailyTimeSpent']
        isHintUsed = value['isHintUsed']
        examYear = value['examYear']
        newExamYearQuestionIndex = value['newExamYearQuestionIndex']
        vocabularyList = value['vocabularyList']
        copyrightId = value['copyrightId']
        copyrightText = value['copyrightText']
        frequentHighlights = value['frequentHighlights']
        totalWeight = value['totalWeight']
        weightScored = value['weightScored']
        maxAnswerSelection = value['maxAnswerSelection']
        scoreTypeId = value['scoreTypeId']
        sql_entries =  (
                exhibits ,
                sequenceId ,
                questionId,
                questionIndex ,
                questionText , 
                questionHeader ,
                explanationText , 
                abstractId ,
                qbankId ,
                sectionId ,
                section ,
                subjectId ,
                subject ,
                secondarySubjectId ,
                secondarySubject ,
                systemId ,
                system ,
                topicId ,
                topic ,
                titleId ,
                title ,
                topicAttributeId ,
                topicAttribute ,
                correctAnswer ,
                userAnswer ,
                parentQuestionId ,
                subParentQuestionId ,
                questionSetSequenceId ,
                questionSetCount ,
                questionToAnswerBeforeThis ,
                answerChoiceList ,
                formatTypeId ,
                questionTypeId ,
                highlights ,
                isCorrect ,
                isIncorrect ,
                isMarked ,
                isOmitted ,
                isQuestionDirty ,
                isAnswerChoiceDisabled ,
                isQuestionDisabled ,
                questionMappingReferencesList ,
                questionMedia ,
                timeSpent ,
                othersAvgTimeSpent ,
                notes ,
                peopleTaken ,
                hotspotImageUrl ,
                lastUpdatedDate ,
                correctPercentile  ,
                isSubmitted ,
                isActive ,
                activeStatusId ,
                hint ,
                allowCalculator ,
                difficultyLevelId ,
                additionalText ,
                mobileExcerpt ,
                passageExcerpt ,
                confSurveyValue ,
                timePerQuestionInMilliSec ,
                answerHeader ,
                standards ,
                totalTimeSpentReview ,
                dailyTimeSpentReview ,
                dailyTimeSpent ,
                isHintUsed ,
                examYear ,
                newExamYearQuestionIndex ,
                vocabularyList ,
                copyrightId ,
                copyrightText ,
                frequentHighlights ,
                totalWeight ,
                weightScored ,
                maxAnswerSelection ,
                scoreTypeId ,
    ) 
        execute_sql(connection, sql_insert_question, sql_entries)



    try:
        for value in flashcard_list: 
            flashCardId = value['flashCardId'] 
            deckId = value['deckId'] 
            deckName = value['deckName']
            deckColor = value['deckColor']
            questionIndex = value['questionIndex'] 
            abstractId = value['abstractId'] 
            frontText = value['frontText'] 
            frontMedia = value['frontMedia']
            backText = value['backText'] 
            backMedia = value['backMedia']
            tags = value['tags']
            subjectId = value['subjectId']
            subject = value['subject'] 
            systemId = value['systemId']
            system = value['system'] 
            sectionId = value['sectionId']
            section = value['section']
            sequenceId = value['sequenceId']
            isCorrect = value['isCorrect']
            isMarked = value['isMarked'] 
            dateCreated = value['dateCreated']
            updateDateCreated = value['updateDateCreated']
            isLocked = value['isLocked'] 
            topicId = value['topicId'] 
            isDeleted = value['isDeleted']
            markId = value['markId']
            studyStatusId = value['studyStatusId']
            studyStepCount = value['studyStatusId'] 
            studyDueDate = value['studyDueDate']
            studyPreviousInterval = value['studyPreviousInterval']
            isCustomStudyDeck = value['isCustomStudyDeck'] 
            customStudyDeckSettings = value['customStudyDeckSettings']
            subscriptionId = value['subscriptionId'] 
            sql_entries =  (
                     flashCardId,
                     deckId,
                     deckName,
                     deckColor,
                     questionIndex,
                     abstractId,
                     frontText, 
                     frontMedia,
                     backText,
                     backMedia,
                     tags,
                     subjectId,
                     subject,
                     systemId,
                     system ,
                     sectionId,
                     section,
                     sequenceId,
                     isCorrect,
                     isMarked,
                     dateCreated,
                     updateDateCreated,
                     isLocked,
                     topicId,
                     isDeleted,
                     markId,
                     studyStatusId,
                     studyStepCount,
                     studyDueDate,
                     studyPreviousInterval,
                     isCustomStudyDeck,
                     customStudyDeckSettings,
                     subscriptionId,
        )
            execute_sql(connection, sql_insert_flashcard, sql_entries)
    except:
            pass


def generate_new_test():
    test_id = post_request(generate_new_test_uri, headers, cookies, json_create_test_data)
    test_id = test_id['testId']
    return(test_id)
   
def get_previous_test():
    previous_test_uri_response = get_request(previous_test_uri, headers, cookies)
    for i in previous_test_uri_response:
        test_id = i['id']
        insert_from_test_id(test_id)

        
    
get_previous_test()
