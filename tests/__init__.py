import os
import sys

project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
app_path = os.path.join(project_path, 'app')
sys.path.append(app_path)
