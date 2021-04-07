"""
├── draft_code
|   ├── pending
|   └── complete
├── includes
├── layouts
|   ├── default
|   └── post
|       └── posted
└── site

"""
#I am not clear on where the PROJECT_ROOT is being created my suggestion is to use a
#real path

import os
PROJECT_ROOT = "C:\Test" # like pwd
os.makedirs(os.path.join(PROJECT_ROOT, 'draft_code'), exist_ok = True)
os.makedirs(os.path.join(PROJECT_ROOT, 'draft_code', 'pending'), exist_ok = True)
os.makedirs(os.path.join(PROJECT_ROOT, 'draft_code', 'complete'), exist_ok = True)
os.makedirs(os.path.join(PROJECT_ROOT, 'includes'), exist_ok = True)
os.makedirs(os.path.join(PROJECT_ROOT, 'default', 'layouts'), exist_ok = True)
os.makedirs(os.path.join(PROJECT_ROOT, 'post', 'layouts'), exist_ok = True)
os.makedirs(os.path.join(PROJECT_ROOT, 'post', 'posted', 'layouts'), exist_ok = True)
os.makedirs(os.path.join(PROJECT_ROOT, 'site'), exist_ok = True)
# print(os.path.isdir(PROJECT_ROOT))

import shutil
for dir_or_file in os.listdir(PROJECT_ROOT):
    print(dir_or_file)

shutil.rmtree(PROJECT_ROOT, ignore_errors=True)

# This didn't work for me. Likely due to an issue with isdir, solution is jsut to run rmtree on the PROJECT_ROOT

# for root, dirs, files in os.walk(PROJECT_ROOT, topdown=False):
#     print(root)
#     print(dirs)
#     print(files)
#     print('------')

# # for root, dirs, files in os.walk(top, topdown=False):
# #     for name in files:
# #         os.remove(os.path.join(root, name))
# #     for name in dirs:
# #         os.rmdir(os.path.join(root, name))


# # for files in os.listdir(PROJECT_ROOT):
# #     if os.path.isdir(files) is True:
# #         print(os.path.join(PROJECT_ROOT,files))
# #         os.rmdir(os.path.join(PROJECT_ROOT,files))
# #         # print(files)
# # for 
