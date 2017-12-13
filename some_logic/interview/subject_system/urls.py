#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from subject_system.api_views import TestView, StudentAddSubjectView, StudentSelectSubjectView, SubjectListView

urlpatterns = [
    url(r'^test/$', TestView.as_view()),
    url(r'add/$', StudentAddSubjectView.as_view()),
    url(r'student/$', StudentSelectSubjectView.as_view()),
    url(r'subjects/', SubjectListView.as_view())
]
