# Generated by Django 3.2.11 on 2022-03-12 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcards',
            fields=[
                ('flashCardId', models.IntegerField(primary_key=True, serialize=False)),
                ('deckId', models.IntegerField()),
                ('deckName', models.TextField()),
                ('deckColor', models.TextField()),
                ('questionIndex', models.IntegerField()),
                ('abstractId', models.IntegerField()),
                ('frontText', models.TextField()),
                ('frontMedia', models.TextField()),
                ('backText', models.TextField()),
                ('backMedia', models.TextField()),
                ('tags', models.TextField()),
                ('subjectId', models.IntegerField()),
                ('subject', models.TextField()),
                ('systemId', models.IntegerField()),
                ('system', models.TextField()),
                ('sectionId', models.IntegerField()),
                ('section', models.TextField()),
                ('sequenceId', models.IntegerField()),
                ('isCorrect', models.TextField()),
                ('isMarked', models.TextField()),
                ('dateCreated', models.TextField()),
                ('updateDateCreated', models.TextField()),
                ('isLocked', models.TextField()),
                ('topicId', models.IntegerField()),
                ('isDeleted', models.TextField()),
                ('markId', models.TextField()),
                ('studyStatusId', models.TextField()),
                ('studyStepCount', models.TextField()),
                ('studyDueDate', models.TextField()),
                ('studyPreviousInterval', models.TextField()),
                ('isCustomStudyDeck', models.TextField()),
                ('customStudyDeckSettings', models.TextField()),
                ('subscriptionId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('exhibits', models.TextField()),
                ('sequenceId', models.IntegerField()),
                ('questionId', models.IntegerField(primary_key=True, serialize=False)),
                ('questionIndex', models.IntegerField()),
                ('questionText', models.TextField()),
                ('questionHeader', models.TextField()),
                ('explanationText', models.TextField()),
                ('abstractId', models.IntegerField()),
                ('qbankId', models.IntegerField()),
                ('sectionId', models.IntegerField()),
                ('section', models.TextField()),
                ('subjectId', models.IntegerField()),
                ('subject', models.TextField()),
                ('secondarySubjectId', models.IntegerField()),
                ('secondarySubject', models.TextField()),
                ('systemId', models.IntegerField()),
                ('system', models.TextField()),
                ('topicId', models.IntegerField()),
                ('topic', models.TextField()),
                ('titleId', models.IntegerField()),
                ('title', models.TextField()),
                ('topicAttributeId', models.IntegerField()),
                ('topicAttribute', models.TextField()),
                ('correctAnswer', models.TextField()),
                ('userAnswer', models.TextField()),
                ('parentQuestionId', models.IntegerField()),
                ('subParentQuestionId', models.IntegerField()),
                ('questionSetSequenceId', models.IntegerField()),
                ('questionSetCount', models.IntegerField()),
                ('questionToAnswerBeforeThis', models.IntegerField()),
                ('answerChoiceList', models.TextField()),
                ('formatTypeId', models.IntegerField()),
                ('questionTypeId', models.IntegerField()),
                ('highlights', models.IntegerField()),
                ('isCorrect', models.TextField()),
                ('isIncorrect', models.TextField()),
                ('isMarked', models.TextField()),
                ('isOmitted', models.TextField()),
                ('isQuestionDirty', models.TextField()),
                ('isAnswerChoiceDisabled', models.TextField()),
                ('isQuestionDisabled', models.TextField()),
                ('questionMappingReferencesList', models.TextField()),
                ('questionMedia', models.TextField()),
                ('timeSpent', models.IntegerField()),
                ('othersAvgTimeSpent', models.IntegerField()),
                ('notes', models.TextField()),
                ('peopleTaken', models.IntegerField()),
                ('hotspotImageUrl', models.TextField()),
                ('lastUpdatedDate', models.TextField()),
                ('correctPercentile', models.IntegerField()),
                ('isSubmitted', models.TextField()),
                ('isActive', models.TextField()),
                ('activeStatusId', models.IntegerField()),
                ('hint', models.TextField()),
                ('allowCalculator', models.TextField()),
                ('difficultyLevelId', models.TextField()),
                ('additionalText', models.TextField()),
                ('mobileExcerpt', models.TextField()),
                ('passageExcerpt', models.TextField()),
                ('confSurveyValue', models.IntegerField()),
                ('timePerQuestionInMilliSec', models.IntegerField()),
                ('answerHeader', models.TextField()),
                ('standards', models.TextField()),
                ('totalTimeSpentReview', models.IntegerField()),
                ('dailyTimeSpentReview', models.IntegerField()),
                ('dailyTimeSpent', models.IntegerField()),
                ('isHintUsed', models.TextField()),
                ('examYear', models.IntegerField()),
                ('newExamYearQuestionIndex', models.IntegerField()),
                ('vocabularyList', models.TextField()),
                ('copyrightId', models.TextField()),
                ('copyrightText', models.TextField()),
                ('frequentHighlights', models.TextField()),
                ('totalWeight', models.TextField()),
                ('weightScored', models.TextField()),
                ('maxAnswerSelection', models.IntegerField()),
                ('scoreTypeId', models.TextField()),
            ],
        ),
    ]
