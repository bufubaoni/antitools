from django.contrib import admin
from subject_system.models import (Student, Subject,
                                   SubjectTime, Teacher, RelationStudentSubject)

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SubjectTime)
admin.site.register(Teacher)
admin.site.register(RelationStudentSubject)

# Register your models here.
