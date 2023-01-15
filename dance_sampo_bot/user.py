

def get_user_info(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_username = message.from_user.username
    user_info = {
        "user_id": user_id,
        "user_name": user_name,
        "user_username": user_username,
        "user_last_name": last_name
    }
    return user_info