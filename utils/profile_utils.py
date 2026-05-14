from utils.data_manager import DataManager

DEFAULT_PROFILE = {
    "name": "",
    "first_name": "",
    "gender": "Female",
    "weight": 60,
    "height": 1.70
}


def load_profile(username):
    data_manager = DataManager(
        fs_protocol="webdav",
        fs_root_folder="caffeine_calculator_app"
    )

    return data_manager.load_user_data(
        "profile.json",
        initial_value=DEFAULT_PROFILE
    )


def save_profile(username, profile_data):
    data_manager = DataManager(
        fs_protocol="webdav",
        fs_root_folder="caffeine_calculator_app"
    )

    data_manager.save_user_data(
        profile_data,
        "profile.json"
    )