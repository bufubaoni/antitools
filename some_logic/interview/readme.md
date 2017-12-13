学生管理系统
## 开发环境
django 2.0
python 3.6.2
未在其余环境运行

## 后台管理
地址: /admin/
用户名 alex
密码 123456

## api说明
###　基本信息返回信息
|   参数名称     |   是否必填          | 备注    |
|-------|-------|-------|
| status  | 必填  | 状态码 |
| msg  | 必填  | 返回说明 |
| data  | 必填  | 数据返回 |

### 学生选课
|   url     |    方法          | 备注    |
|-------|-------|-------|
| /subject_system/add/  | post  | 学生选课 |
请求参数
|   参数名称     |   是否必填          | 备注    |
|-------|-------|-------|
| student_id  | 必填  | 学生id |
| subject_id  | 必填  | 科目id |
| date  | 必填  | 上课日期 |
成功后返回参数为空
示例
```python
import requests

url = "http://127.0.0.1:8000/subject_system/add/"

payload = "{\"student_id\":1,\"subject_id\":6,\"date\":\"2017-12-13\"}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
```

返回示例
```json
{
  "msg": "选课不可超过5门",
  "status": "-1",
  "data": {}
}
```
### 课程列表
|   url     |    方法          | 备注    |
|-------|-------|-------|
| /subject_system/subjects/  | get  | 课程列表 |
返回参数
|   参数名称     |   数据类型          | 备注    |
|-------|-------|-------|
| subject_id  | int  | 科目id |
| subject_name  | string  | 科目名称 |
| start_time  | string  | 开始时间 |
| end_time  | string  | 结束日期 |
| teacher_name  | string  | 教师姓名 |
示例

请求示例
```python
import requests

url = "http://127.0.0.1:8000/subject_system/subjects/"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
```
返回示例
```json
{
  "msg": "ok",
  "status": "1",
  "data": [
    {
      "subject_id": 1,
      "subject_name": "数学",
      "start_time": "08:00:00",
      "end_time": "09:00:00",
      "teacher_name": "数学老师"
    },
    {
      "subject_id": 2,
      "subject_name": "英语",
      "start_time": "08:00:00",
      "end_time": "09:00:00",
      "teacher_name": "英语老师"
    },
    {
      "subject_id": 3,
      "subject_name": "数学",
      "start_time": "09:00:00",
      "end_time": "10:00:00",
      "teacher_name": "数学老师"
    },
    {
      "subject_id": 4,
      "subject_name": "数学",
      "start_time": "11:00:00",
      "end_time": "12:00:00",
      "teacher_name": "数学老师"
    },
    {
      "subject_id": 5,
      "subject_name": "英语",
      "start_time": "14:00:00",
      "end_time": "15:00:00",
      "teacher_name": "英语老师"
    },
    {
      "subject_id": 6,
      "subject_name": "英语",
      "start_time": "15:00:00",
      "end_time": "16:00:00",
      "teacher_name": "英语老师"
    }
  ]
}
```
### 学生选择列表
|   url     |    方法          | 备注    |
|-------|-------|-------|
| /subject_system/student/  | post  | 课程列表 |
请求参数
|   参数名称     |   是否必填          | 备注    |
|-------|-------|-------|
| student_id  | 必填  | 学生id |

返回参数
|   参数名称     |   数据类型          | 备注    |
|-------|-------|-------|
| subject_name  | string  | 科目名称 |
| start_time  | string  | 开始时间 |
| end_time  | string  | 结束日期 |
| teacher_name  | string  | 教师姓名 |
| date  | string  | 上课日期 |
示例

请求示例
```python
import requests

url = "http://127.0.0.1:8000/subject_system/student/"

payload = "{\"student_id\":1}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
```
返回示例
```json
{
  "msg": "ok",
  "status": "1",
  "data": [
    {
      "subject_name": "数学",
      "start_time": "08:00:00",
      "end_time": "09:00:00",
      "teacher_name": "数学老师",
      "date": "2017-12-13"
    },
    {
      "subject_name": "数学",
      "start_time": "11:00:00",
      "end_time": "12:00:00",
      "teacher_name": "数学老师",
      "date": "2017-12-13"
    },
    {
      "subject_name": "数学",
      "start_time": "09:00:00",
      "end_time": "10:00:00",
      "teacher_name": "数学老师",
      "date": "2017-12-13"
    },
    {
      "subject_name": "英语",
      "start_time": "14:00:00",
      "end_time": "15:00:00",
      "teacher_name": "英语老师",
      "date": "2017-12-13"
    },
    {
      "subject_name": "英语",
      "start_time": "15:00:00",
      "end_time": "16:00:00",
      "teacher_name": "英语老师",
      "date": "2017-12-13"
    }
  ]
}
```

精力有限，为了减少部署依赖，未能完成异常处理部分，测试环境搭建，日志分析等生产必要组件。

`subject_system_relationsstudentsubject` 为累积记录表，可针对time,student_id 建立索引，提高查询速度，其余静态数据表可加载到内存中以提高查询速度。

由于主键采用int类型，水平切分比较复杂。

并未做兼容性考虑，仅此表示抱歉。
