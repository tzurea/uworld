# Generated by Django 3.2.11 on 2022-03-12 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcards',
            name='abstractId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='backMedia',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='backText',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='customStudyDeckSettings',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='dateCreated',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='deckColor',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='deckId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='deckName',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='frontMedia',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='frontText',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='isCorrect',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='isCustomStudyDeck',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='isDeleted',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='isLocked',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='isMarked',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='markId',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='questionIndex',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='section',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='sectionId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='sequenceId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='studyDueDate',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='studyPreviousInterval',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='studyStatusId',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='studyStepCount',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='subject',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='subjectId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='subscriptionId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='system',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='systemId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='tags',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='topicId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='updateDateCreated',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='abstractId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='activeStatusId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='additionalText',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='allowCalculator',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answerChoiceList',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answerHeader',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='confSurveyValue',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='copyrightId',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='copyrightText',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='correctAnswer',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='correctPercentile',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='dailyTimeSpent',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='dailyTimeSpentReview',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='difficultyLevelId',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='examYear',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='exhibits',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='explanationText',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='formatTypeId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='frequentHighlights',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='highlights',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='hint',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='hotspotImageUrl',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isActive',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isAnswerChoiceDisabled',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isCorrect',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isHintUsed',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isIncorrect',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isMarked',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isOmitted',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isQuestionDirty',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isQuestionDisabled',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='isSubmitted',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='lastUpdatedDate',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='maxAnswerSelection',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='mobileExcerpt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='newExamYearQuestionIndex',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='othersAvgTimeSpent',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='parentQuestionId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='passageExcerpt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='peopleTaken',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='qbankId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionHeader',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionIndex',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionMappingReferencesList',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionMedia',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionSetCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionSetSequenceId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionText',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionToAnswerBeforeThis',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionTypeId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='scoreTypeId',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='secondarySubject',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='secondarySubjectId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='section',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='sectionId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='sequenceId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='standards',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='subParentQuestionId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='subject',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='subjectId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='system',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='systemId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='timePerQuestionInMilliSec',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='timeSpent',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='titleId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='topic',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='topicAttribute',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='topicAttributeId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='topicId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='totalTimeSpentReview',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='totalWeight',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='userAnswer',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='vocabularyList',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='weightScored',
            field=models.TextField(null=True),
        ),
    ]
