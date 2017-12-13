#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from subject_system.base_views import ApiView, ValidatorsMixin
from subject_system.models import RelationStudentSubject, Subject, Student


class TestView(ApiView):
    ALLOWED_METHOD = ["get"]

    def get(self, request):
        return {"test": "test"}


class StudentAddSubjectView(ValidatorsMixin, ApiView):
    ALLOWED_METHOD = ['post']
    SCHEMA = {
        "student_id": {"type": "int", "required": True},
        "subject_id": {"type": "int", "required": True},
        "date": {"type": "date", "required": True}
    }

    def post(self, request):
        if not self.cleaned():
            return u"参数错误"

        is_checked, msg = self.data_checked()
        if not is_checked:
            return msg

        relation_student_subject = RelationStudentSubject(student=self.student,
                                                          subject=self.subject,
                                                          time=self.date,
                                                          create_time=datetime.now())
        relation_student_subject.save()
        return {}

    def data_checked(self):
        student_id = self.form.cleaned_data.get("student_id")
        subject_id = self.form.cleaned_data.get("subject_id")
        date = self.form.cleaned_data.get("date")

        student = Student.objects.filter(id=student_id).first()
        if not student:
            return False, u"学生不在此系统"

        current_subjects = RelationStudentSubject.objects.filter(student_id=student_id,
                                                                 time=date)

        count_current_subjects = current_subjects.count()
        if count_current_subjects >= 5:
            return False, u"选课不可超过5门"

        subject = Subject.objects.filter(id=subject_id).first()

        if not subject:
            return False, u"课程编号不存在"

        time_period = [item.subject.time_id for item in current_subjects]
        if subject.time_id in time_period:
            return False, u"时段重复"

        self.student = student
        self.subject = subject
        self.date = date
        return True, ""


class StudentSelectSubjectView(ValidatorsMixin, ApiView):
    ALLOWED_METHOD = ['post']
    SCHEMA = {
        "student_id": {"type": "int", "required": True}
    }

    def post(self, request):
        if not self.cleaned():
            return u"参数错误"
        is_checked, msg = self.data_checked()
        if not is_checked:
            return msg

        return list(self.data_serializer())

    def data_checked(self):
        student_id = self.form.cleaned_data.get("student_id")

        student = Student.objects.filter(id=student_id).first()
        if not student:
            return False, u"学生不在此系统"
        self.student = student
        return True, ""

    def data_serializer(self):
        current_subjects = RelationStudentSubject.objects.filter(student=self.student).order_by("time")
        for item in current_subjects:
            yield {
                "subject_name": item.subject.name,
                "start_time": item.subject.time.start_time.isoformat(),
                "end_time": item.subject.time.end_time.isoformat(),
                "teacher_name": item.subject.teacher.name,
                "date": item.time.isoformat()
            }


class SubjectListView(ApiView):
    ALLOWED_METHOD = ['get']

    def get(self, request):
        return list(self.data_serializer())

    def data_serializer(self):
        subjects = Subject.objects.all()
        for item in subjects:
            yield {
                "subject_id":item.pk,
                "subject_name": item.name,
                "start_time": item.time.start_time.isoformat(),
                "end_time": item.time.end_time.isoformat(),
                "teacher_name": item.teacher.name
            }