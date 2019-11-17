import os

exclude = ["helpers"]
apps = []
for ele in os.listdir("."):
    if os.path.isdir(ele) and ele not in exclude:
        apps.append(ele)
