from django.db import models
from django.utils import timezone

class Questions(models.Model):
    exhibits = models.TextField(null=True)
    sequenceId = models.IntegerField(null=True)
    questionId = models.IntegerField(primary_key=True)
    questionIndex = models.IntegerField(null=True)
    questionText = models.TextField(null=True) 
    questionHeader = models.TextField(null=True)
    explanationText = models.TextField(null=True) 
    abstractId = models.IntegerField(null=True)
    qbankId = models.IntegerField(null=True)
    sectionId = models.IntegerField(null=True)
    section = models.TextField(null=True)
    subjectId = models.IntegerField(null=True)
    subject = models.TextField(null=True)
    secondarySubjectId = models.IntegerField(null=True)
    secondarySubject = models.TextField(null=True)
    systemId = models.IntegerField(null=True)
    system = models.TextField(null=True)
    topicId = models.IntegerField(null=True)
    topic = models.TextField(null=True)
    titleId = models.IntegerField(null=True)
    title = models.TextField(null=True)
    topicAttributeId = models.IntegerField(null=True)
    topicAttribute = models.TextField(null=True)
    correctAnswer = models.TextField(null=True)
    userAnswer = models.TextField(null=True)
    parentQuestionId = models.IntegerField(null=True)
    subParentQuestionId = models.IntegerField(null=True)
    questionSetSequenceId = models.IntegerField(null=True)
    questionSetCount = models.IntegerField(null=True)
    questionToAnswerBeforeThis = models.IntegerField(null=True)
    answerChoiceList = models.TextField(null=True)
    formatTypeId = models.IntegerField(null=True)
    questionTypeId = models.IntegerField(null=True)
    highlights = models.IntegerField(null=True)
    isCorrect = models.TextField(null=True)
    isIncorrect = models.TextField(null=True)
    isMarked = models.TextField(null=True)
    isOmitted = models.TextField(null=True)
    isQuestionDirty = models.TextField(null=True)
    isAnswerChoiceDisabled = models.TextField(null=True)
    isQuestionDisabled = models.TextField(null=True)
    questionMappingReferencesList = models.TextField(null=True)
    questionMedia = models.TextField(null=True)
    timeSpent = models.IntegerField(null=True)
    othersAvgTimeSpent = models.IntegerField(null=True)
    notes = models.TextField(null=True)
    peopleTaken = models.IntegerField(null=True)
    hotspotImageUrl = models.TextField(null=True)
    lastUpdatedDate = models.TextField(null=True)
    correctPercentile = models.IntegerField(null=True)
    isSubmitted = models.TextField(null=True)
    isActive = models.TextField(null=True)
    activeStatusId = models.IntegerField(null=True)
    hint = models.TextField(null=True)
    allowCalculator = models.TextField(null=True)
    difficultyLevelId = models.TextField(null=True)
    additionalText = models.TextField(null=True)
    mobileExcerpt = models.TextField(null=True)
    passageExcerpt = models.TextField(null=True)
    confSurveyValue = models.IntegerField(null=True)
    timePerQuestionInMilliSec = models.IntegerField(null=True)
    answerHeader = models.TextField(null=True)
    standards = models.TextField(null=True)
    totalTimeSpentReview = models.IntegerField(null=True)
    dailyTimeSpentReview = models.IntegerField(null=True)
    dailyTimeSpent = models.IntegerField(null=True)
    isHintUsed = models.TextField(null=True)
    examYear = models.IntegerField(null=True)
    newExamYearQuestionIndex = models.IntegerField(null=True)
    vocabularyList = models.TextField(null=True)
    copyrightId = models.TextField(null=True)
    copyrightText = models.TextField(null=True)
    frequentHighlights = models.TextField(null=True)
    totalWeight = models.TextField(null=True)
    weightScored = models.TextField(null=True)
    maxAnswerSelection = models.IntegerField(null=True)
    scoreTypeId = models.TextField(null=True)

class Flashcards(models.Model):
    flashCardId = models.IntegerField(primary_key=True)
    deckId   = models.IntegerField(null=True)
    deckName   = models.TextField(null=True)
    deckColor   = models.TextField(null=True)
    questionIndex   = models.IntegerField(null=True)
    abstractId   = models.IntegerField(null=True)
    frontText   = models.TextField(null=True) 
    frontMedia   = models.TextField(null=True)
    backText   = models.TextField(null=True)
    backMedia   = models.TextField(null=True)
    tags   = models.TextField(null=True)
    subjectId   = models.IntegerField(null=True)
    subject   = models.TextField(null=True)
    systemId   = models.IntegerField(null=True)
    system   = models.TextField(null=True)
    sectionId   = models.IntegerField(null=True)
    section   = models.TextField(null=True)
    sequenceId   = models.IntegerField(null=True)
    isCorrect   = models.TextField(null=True)
    isMarked   = models.TextField(null=True)
    dateCreated   = models.TextField(null=True)
    updateDateCreated   = models.TextField(null=True)
    isLocked   = models.TextField(null=True)
    topicId   = models.IntegerField(null=True)
    isDeleted   = models.TextField(null=True)
    markId   = models.TextField(null=True)
    studyStatusId   = models.TextField(null=True)
    studyStepCount   = models.TextField(null=True)
    studyDueDate   = models.TextField(null=True)
    studyPreviousInterval   = models.TextField(null=True)
    isCustomStudyDeck   = models.TextField(null=True)
    customStudyDeckSettings   = models.TextField(null=True)
    subscriptionId   = models.IntegerField(null=True)   

class Sessions(models.Model):
    id = models.IntegerField(primary_key=True)
    createdTime = models.DateTimeField(auto_now=True)
    timeLimit = models.IntegerField(null=True)
    divisionIds = models.TextField(null=True)
    maxQuestionCount = models.IntegerField(null=True, default=40)
    questionIdList = models.TextField(null=True)
    questionList = models.TextField(null=True)
    