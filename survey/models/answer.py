# -*- coding: utf-8 -*-

"""
    These type-specific answer models use a text field to allow for flexible
    field sizes depending on the actual question this answer corresponds to any
    "required" attribute will be enforced by the form.
"""

from builtins import super
import logging

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .question import Question
from .response import Responses


LOGGER = logging.getLogger(__name__)


class Answer(models.Model):

    question = models.ForeignKey(Question, verbose_name=_("Question"),
                                 related_name="answers")
    response = models.ForeignKey(Responses, verbose_name=_("Response"),
                                 related_name="answers")
    created = models.DateTimeField(_("Creation date"), auto_now_add=True, null=True,
                             blank=True)
    updated = models.DateTimeField(_("Update date"), auto_now=True, null=True,
                             blank=True)
    body = models.TextField(_("Content"), blank=True, null=True)

    def __init__(self, *args, **kwargs):
        try:
            question = Question.objects.get(pk=kwargs["question_id"])
        except KeyError:
            question = kwargs.get("question")
        body = kwargs.get("body")
        if question and body:
            self.check_answer_body(question, body)
        super(Answer, self).__init__(*args, **kwargs)

    @property
    def values(self):
        if len(self.body) < 3 or self.body[0:3] != "[u'":
            return [self.body]
        #  We do not use eval for security reason but it could work with :
        #  eval(self.body)
        #  It would permit to inject code into answer though.
        values = []
        raw_values = self.body.split("', u'")
        nb_values = len(raw_values)
        for i, value in enumerate(raw_values):
            if i == 0:
                value = value[3:]
            if i + 1 == nb_values:
                value = value[:-2]
            values.append(value)
        return values

    def check_answer_body(self, question, body):
        # import pdb
        # pdb.set_trace()
        print("==========model===============")

        if question.type in [Question.RADIO,
                             Question.CHECKBOX]:
            choices = question.get_clean_choices()
            if body:
                if body[0] == "[":
                    answers = []
                    for i, part in enumerate(body.split("'")):
                        if i % 2 == 1:
                            answers.append(part)
                else:
                    answers = [body]
            print(answers)
            for answer in answers:
                # ===================================
                if '@@@' in choices[0]:
                    choices = choices[0].split("@@@")
                    print(choices)
                # ===================================
                if answer not in choices:
                    msg = "Impossible answer '{}'".format(body)
                    msg += " should be in {} ".format(choices)
                    raise ValidationError(msg)

    def __str__(self):
        return u"{} to '{}' : '{}'".format(
            self.__class__.__name__, self.question, self.body
        )
