from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from hmac import compare_digest,new

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    is_teacher = db.Column(db.Boolean)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
#     first_name = db.Column(db.String(100), nullable=False)
#     last_name = db.Column(db.String(100), nullable=False)
#     #is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def check_password(self, password):
        return compare_digest(password, "password")

    def create(self):
        db.session.add(self)
        db.session.commit()
        return 'success'
        
    def update(self,password):
        self.password=password
        db.session.commit()
        return 'success'

    def __repr__(self):
        return f'<User {self.email}>'

    def serializeUser(self):
        return {
            "id": self.id,
            "email": self.email,
            # generate_password_hash("password"): self.password,
            "password": self.password,
            "is_teacher": self.is_teacher,
#             "first_name": self.first_name,
#             "last_name": self.last_name,
#             # do not serialize the password, its a security breach
        }


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    avatar = db.Column(db.String, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    subjects1 = db.Column(db.String(100), nullable=False)
    subjects2 = db.Column(db.String(100))
    subjects3 = db.Column(db.String(100))
    subjects4 = db.Column(db.String(100))
    why_you_teach = db.Column(db.String(200), nullable=False) 
    years_experience = db.Column(db.Integer, nullable=False)
    fun_info = db.Column(db.String(100), nullable=False)
    lessons = db.relationship('Lesson_Content', backref='teacher', lazy=True)
    
#     #is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<Teacher {self.first_name} {self.last_name}>'

    def serializeTeacher(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "avatar": self.avatar,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "subjects1": self.subjects1,
            "subjects2": self.subjects2,
            "subjects3": self.subjects3,
            "subjects4": self.subjects4,
            "why_you_teach": self.why_you_teach,
            "years_experience": self.years_experience,
            "fun_info": self.fun_info,
            # "lessons": self.lessons,

        }

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String, unique=True)


    def __reprStudents__(self):
        return f'<Students {self.title}>'

    def serializeStudent(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "avatar": self.avatar,

        }

class Lesson_Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer) #ForeignKey
    # db.relatinship() (relação de 1 para muitos)
    # teachers_name = id para buscar o nome
    title = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    introduction = db.Column(db.String(2000), nullable=False)
    written_content = db.Column(db.String(5000), nullable=False)
    summary = db.Column(db.String(1250), nullable=False)
    key_word1 = db.Column(db.String (30)) # nullable whem change the frontend
    key_word2 = db.Column(db.String (30))
    key_word3 = db.Column(db.String (30))
    question1 = db.Column(db.String (500))
    question2 = db.Column(db.String (500))
    question3 = db.Column(db.String (500))
    question4 = db.Column(db.String (500))
    image = db.Column(db.String(50000))
    date = db.Column(db.String (30))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

    def __reprLessons__(self):
        return f'<Lesson_Content {self.title}>'

    def serializeLessons(self):
        return {
            "id": self.id,
            "title": self.title,
            "subject": self.subject,
            "introduction": self.introduction,
            "written_content": self.written_content,
            "summary": self.summary,
            "image": self.image,
            "date": self.date,
            "key_word1": self.key_word1,
            "key_word2": self.key_word2,
            "key_word3": self.key_word3,
            "question1": self.question1,
            "question2": self.question2,
            "question3": self.question3,
            "question4": self.question4,
            "teacher_id": self.teacher_id,
        }
