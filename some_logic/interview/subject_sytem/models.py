from django.db import models


class ModelMixin(object):
    def format(self):
        pass

    def __str__(self):
        return self.format()

    def __unicode__(self):
        return self.format()


class Student(ModelMixin, models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名")

    def format(self):
        return self.name


class Teacher(ModelMixin, models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名")

    def format(self):
        return self.name


class SubjectTime(ModelMixin, models.Model):
    start_time = models.TimeField(verbose_name="上课时间")
    end_time = models.TimeField(verbose_name="下课时间")

    def format(self):
        return "{start}--{end}".format(start=self.start_time.isoformat(),
                                       end=self.end_time.isoformat())


class Subject(ModelMixin, models.Model):
    name = models.CharField(max_length=50, verbose_name="课程名称")
    time = models.ForeignKey(SubjectTime,
                             verbose_name="上课时间",
                             on_delete=models.SET_NULL,
                             null=True)
    teacher = models.ForeignKey(Teacher,
                                verbose_name="教师姓名",
                                on_delete=models.SET_NULL,
                                null=True)

    def format(self):
        return "{name}--{time}--{teacher}".format(name=self.name,
                                                  time=self.time,
                                                  teacher=self.teacher)


class RelationStudentSubject(ModelMixin, models.Model):
    student = models.ForeignKey(Student, verbose_name="学生姓名")
    subject = models.ForeignKey(Subject, verbose_name="课程名称")
    time = models.DateField(verbose_name="上课日期")
    create_time = models.DateTimeField(verbose_name="创建日期")

    def format(self):
        return "{student}--{subject}--{time}".format(student=self.student,
                                                     subject=self.subject,
                                                     time=self.time.isoformat())
