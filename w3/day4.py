import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("MY_API_KEY")
print("获取到的是：",key)