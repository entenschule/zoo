import os
import sys
from bottle import template
from datetime import datetime


# command line arguments
path_string, name = sys.argv[1:3]
path_list = path_string.split('.')

this_folder = os.path.dirname(__file__)
proj_folder = os.path.dirname(os.path.dirname(this_folder))

# target folder, where the files will be created
target_folder_list = [proj_folder] + path_list + ['properties', name]
target_folder = os.path.join(*target_folder_list)
os.mkdir(target_folder)

# target files
target_init_file = os.path.join(target_folder, '__init__.py')
target_work_file = os.path.join(target_folder, 'work.py')
target_test_file = os.path.join(target_folder, '_test.py')

success_file = os.path.join(this_folder, 'SUCCESS.md')

init_view = os.path.join(this_folder, 'views', 'code.tpl')
work_view = os.path.join(this_folder, 'views', 'work.tpl')
test_view = os.path.join(this_folder, 'views', 'test.tpl')
success_view = os.path.join(this_folder, 'views', 'success.tpl')


# create target files ##################################################################################################

context = {
    'name': name,
    'class_name': path_list[-1].title(),  # class name should be folder name in title case
    'path_dots': path_string,
    'path_slashes': path_string.replace('.', '/'),
    'time': datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
}

with open(target_init_file, 'x') as f:
    f.write(
        template(init_view, context)
    )

with open(target_work_file, 'x') as f:
    f.write(
        template(work_view)
    )

with open(target_test_file, 'x') as f:
    f.write(
        template(test_view, context)
    )

try:
    os.remove(success_file)
except OSError:
    pass

with open(success_file, 'x') as f:
    f.write(
        template(success_view, context)
    )
