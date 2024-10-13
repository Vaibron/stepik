from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/user/profile")
def get_profile():
    # Здесь вы можете реализовать логику для получения профиля пользователя
    return {"user": "Profile data"}


@user_router.get("/user/settings")
def get_settings():
    # Здесь вы можете реализовать логику для получения настроек пользователя
    return {"settings": "User settings"}

