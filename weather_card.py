"""
W3 练习骨架：open-meteo 天气卡片
================================
目标：用 requests 调公开 API，用 rich 把返回的 JSON 渲染成一张好看的天气卡片。
特点：open-meteo 免密钥，不注册任何账号也能把本周跑完。

本周你会在不同 Day 往这个骨架里填东西（见每个函数上方的注释）：
- Day1：requests 入门，能发出请求、拿到响应            → 看 fetch_weather / get_json
- Day2：JSON 解析，从嵌套 dict 取 temperature_2m 等字段 → 看 render_card
- Day3：错误处理 + 重试，把 get_json 换成带超时和重试的 safe_get
- Day4：把城市坐标抽到 .env，用 python-dotenv 读        → 见底部 TODO

运行（Git Bash）：
    source venv/Scripts/activate
    python weather_card.py
"""

import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# ---- 配置（Day4 会改成从 .env 读）----
LAT, LON = 23.13, 113.26   # 广州番禺
CITY = "广州"
URL = "https://api.open-meteo.com/v1/forecast"

# WMO weather_code -> 中文描述（open-meteo 用这套编码，不是文字而是数字）
WEATHER_DESC = {
    0: "晴", 1: "大致晴朗", 2: "局部多云", 3: "阴",
    45: "雾", 48: "雾凇",
    51: "小毛雨", 53: "毛雨", 55: "大毛雨",
    61: "小雨", 63: "中雨", 65: "大雨",
    71: "小雪", 73: "中雪", 75: "大雪",
    80: "阵雨", 81: "强阵雨", 82: "暴雨",
    95: "雷阵雨", 96: "雷阵雨伴冰雹", 99: "雷阵雨伴强冰雹",
}


def get_json(url: str, params: dict) -> dict:
    """Day1 最简版：发 GET，返回解析好的 dict。

    Day3 你要在这里加：
      - timeout=5                      防止网络卡死一直等
      - 失败重试 3 次（for 循环 + try/except）
    把它升级成 safe_get(url, params)。
    """
    resp = requests.get(url, params=params)
    resp.raise_for_status()          # HTTP 非 2xx 时抛异常（Day3 要 catch 它）
    return resp.json()


def fetch_weather(lat: float, lon: float) -> dict:
    """组装参数、发请求、返回 current 那段数据。"""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,weather_code",
        "timezone": "Asia/Shanghai",
    }
    data = get_json(URL, params)
    # 返回的 JSON 长这样：
    #   {"latitude": 23.13, "longitude": 113.26, "current": {"time":..., "temperature_2m": 30.5, "weather_code": 0}, ...}
    # Day2 练习：自己 print(data) 看完整结构，再手动取出 current。
    # print(data)
    # print(data['current']['temperature_2m'])
    return data["current"]


def render_card(city: str, current: dict) -> None:
    """把 current 里的字段渲染成 rich 卡片。"""
    temp = current["temperature_2m"]
    code = current["weather_code"]
    desc = WEATHER_DESC.get(code, f"未知天气(code={code})")

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_row("🌡 气温", f"{temp} °C")
    table.add_row("☁ 天气", desc)

    panel = Panel(
        table,
        title=f"🌏 {city} 实时天气",
        subtitle="数据来源：open-meteo（免密钥）",
        border_style="cyan",
    )
    console.print(panel)


def main() -> None:
    current = fetch_weather(LAT, LON)
    render_card(CITY, current)


if __name__ == "__main__":
    main()
