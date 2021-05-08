import os

print(os.path.join("data", f) for f in os.listdir("data"))