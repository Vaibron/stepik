from fastapi import APIRouter

course_router = APIRouter()


@course_router.get("/courses")
def get_courses():
    # Здесь вы можете реализовать логику для получения курсов
    return {"courses": "Python"}


@course_router.get("/courses/{course_id}")
def get_course(course_id: int):
    # Здесь вы можете реализовать логику для получения курса по id
    return {"course": "Python"}


@course_router.get("/courses/{course_id}/lessons")
def get_lessons(course_id: int):
    # Здесь вы можете реализовать логику для получения уроков курса
    return {"lessons": "Lesson 1"}
