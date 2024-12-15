
from users.schemas import CreateUser

#Отдельный помошник который будет создавать пользователя
def create_user(user_in: CreateUser) -> dict:
    #model_dump распакуем в словарь
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }

