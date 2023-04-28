 
import os

# Define the project directory
PROJECT_DIR = "realtime_data_viz"

# Create the project directory if it does not exist
if not os.path.exists(PROJECT_DIR):
    os.mkdir(PROJECT_DIR)

# Create the subdirectories for the project
subdirs = ["data", "visualization", "streamlit"]
for subdir in subdirs:
    path = os.path.join(PROJECT_DIR, subdir)
    if not os.path.exists(path):
        os.mkdir(path)

# Create empty files in each subdirectory
data_files = ["stream_data.py", "process_data.py"]
viz_files = ["plot_data.py"]
streamlit_files = ["app.py"]

for filename in data_files:
    file_path = os.path.join(PROJECT_DIR, "data", filename)
    if not os.path.exists(file_path):
        open(file_path, 'w').close()
        
for filename in viz_files:
    file_path = os.path.join(PROJECT_DIR, "visualization", filename)
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

for filename in streamlit_files:
    file_path = os.path.join(PROJECT_DIR, "streamlit", filename)
    if not os.path.exists(file_path):
        open(file_path, 'w').close()
