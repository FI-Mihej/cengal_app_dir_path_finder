import os
from cengal_app_dir_path_finder import AppDirectoryType, AppDirPath

app_dir_path: AppDirPath = AppDirPath()
local_data_dir_path: str = app_dir_path(AppDirectoryType.local_data, 'MyApplicationName')
settings_json_path: str = os.path.join(local_data_dir_path, 'settings.json')
print(settings_json_path)  # Will print full path to the `~/.local/state/MyApplicationName/local/data/settings.json`
with open(settings_json_path, 'w') as file:
    file.write('string with my settings')
