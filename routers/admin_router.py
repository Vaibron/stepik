from fastapi import APIRouter

admin_router = APIRouter()


@admin_router.get("/admin/courses")
def get_admin_courses():
    # Здесь вы можете реализовать логику для получения административных данных курсов
    return {"courses": "Course 1"}


@admin_router.get("/admin/users")
def get_admin_users():
    # Здесь вы можете реализовать логику для получения административных данных пользователей
    return {"users": "User 1"}


@admin_router.get("/admin/settings")
def get_admin_settings():
    # Здесь вы можете реализовать логику для получения административных настроек
    return {"settings": "Setting 1"}
