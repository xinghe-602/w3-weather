import requests
def safe_get(url,retries=3):
    for i in range(1,retries+1):
        try:
            r = requests.get(url,timeout=5)
            r.raise_for_status()
            return r.json()
        except (requests.exceptions.RequestException,ValueError) as e:
            print(f"第{i}次请求失败:{e}")
            if i < retries:
                print("准备重试....")
            else:
                print("已达到最大重试次数，请求放弃")
    return None

if __name__ == "__main__":
    data = safe_get("https://api.github.com/users/xinghe-602")
    print(type(data), data["public_repos"])
    bad = safe_get("https://this-domain-does-not-exist-xyz.invalid")
    print(bad)