from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'


# Курсы
class Course(Base):
    course_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Уникальный идентификатор курса (первичный ключ)
    title: Mapped[str] = mapped_column(String)  # Название курса
    description: Mapped[str] = mapped_column(String)  # Описание курса
    author_id: Mapped[int] = mapped_column(
        ForeignKey('users.user_id'))  # Идентификатор автора курса (внешний ключ к таблице Users)
    category: Mapped[str] = mapped_column(String)  # Категория курса
    duration: Mapped[int] = mapped_column(Integer)  # Длительность курса

    author = relationship("Users", back_populates="courses")


# Пользователи
class User(Base):
    user_id: Mapped[int] = mapped_column(Integer,
                                         primary_key=True)  # Уникальный идентификатор пользователя (первичный ключ)
    email: Mapped[str] = mapped_column(String, unique=True)  # Электронная почта пользователя
    password: Mapped[str] = mapped_column(String)  # Кешированный пароль
    name: Mapped[str] = mapped_column(String)  # Имя пользователя
    role: Mapped[str] = mapped_column(String)  # Роль пользователя (например, студент, преподаватель)

    courses = relationship("Courses", back_populates="author")


# Задания
class Assignment(Base):
    assignment_id: Mapped[int] = mapped_column(Integer,
                                               primary_key=True)  # Уникальный идентификатор задания (первичный ключ)
    title: Mapped[str] = mapped_column(String)  # Название задания
    description: Mapped[str] = mapped_column(String)  # Описание задания
    course_id: Mapped[int] = mapped_column(ForeignKey(
        'courses.course_id'))  # Идентификатор курса, к которому относится задание (внешний ключ к таблице Courses)
    due_date: Mapped[DateTime] = mapped_column(DateTime)  # Срок выполнения задания

    course = relationship("Courses", back_populates="assignments")


# Ответы
class Answer(Base):
    answer_id: Mapped[int] = mapped_column(Integer,
                                           primary_key=True)  # Уникальный идентификатор ответа (первичный ключ)
    assignment_id: Mapped[int] = mapped_column(ForeignKey(
        'assignments.assignment_id'))  # Идентификатор задания, к которому относится ответ (внешний ключ к таблице Assignments)
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.user_id'))  # Идентификатор пользователя, который дал ответ (внешний ключ к таблице Users)
    content: Mapped[str] = mapped_column(String)  # Текст ответа
    score: Mapped[int] = mapped_column(Integer)  # Оценка за ответ

    assignment = relationship("Assignments", back_populates="answers")
    user = relationship("Users", back_populates="answers")


# Оценки
class Grade(Base):
    grade_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Уникальный идентификатор оценки (первичный ключ)
    assignment_id: Mapped[int] = mapped_column(ForeignKey(
        'assignments.assignment_id'))  # Идентификатор задания, к которому относится оценка (внешний ключ к таблице Assignments)
    user_id: Mapped[int] = mapped_column(ForeignKey(
        'users.user_id'))  # Идентификатор пользователя, которому выставлена оценка (внешний ключ к таблице Users)
    score: Mapped[int] = mapped_column(Integer)  # Оценка за задание

    assignment = relationship("Assignments", back_populates="grades")
    user = relationship("Users", back_populates="grades")


# Темы
class Topic(Base):
    topic_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Уникальный идентификатор темы (первичный ключ)
    title: Mapped[str] = mapped_column(String)  # Название темы
    description: Mapped[str] = mapped_column(String)  # Описание темы
    course_id: Mapped[int] = mapped_column(ForeignKey(
        'courses.course_id'))  # Идентификатор курса, к которому относится тема (внешний ключ к таблице Courses)

    course = relationship("Courses", back_populates="topics")


# Материалы
class Material(Base):
    material_id: Mapped[int] = mapped_column(Integer,
                                             primary_key=True)  # Уникальный идентификатор материала (первичный ключ)
    title: Mapped[str] = mapped_column(String)  # Название материала
    content: Mapped[str] = mapped_column(String)  # Текст материала
    course_id: Mapped[int] = mapped_column(ForeignKey(
        'courses.course_id'))  # Идентификатор курса, к которому относится материал (внешний ключ к таблице Courses)

    course = relationship("Courses", back_populates="materials")


# Пользователи-Курсы
class UsersCourse(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'),
                                         primary_key=True)  # Идентификатор пользователя (внешний ключ к таблице Users)
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.course_id'),
                                           primary_key=True)  # Идентификатор курса (внешний ключ к таблице Courses)

    user = relationship("Users", back_populates="courses")
    course = relationship("Courses", back_populates="users")
