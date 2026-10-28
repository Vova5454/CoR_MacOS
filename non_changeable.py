import os


save_folder = os.path.expanduser("~/Library/Application Support/CoR")
save_folder = os.path.join(save_folder, "CoR")
os.makedirs(save_folder, exist_ok=True)