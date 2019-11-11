import os

apps = []
for ele in os.listdir("."):
    if os.path.isdir(ele):
        apps.append(ele)
