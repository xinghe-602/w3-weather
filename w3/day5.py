import os
import sys
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from day3 import safe_get

load_dotenv()
MY_API_KEY = os.getenv("MY_API_KEY")

CITY_COORDS = {
    "广州":(23.13,113.26),
    "北京":(39.90,116.40),
    "上海":(31.23,121.47)
}

def get_coords(city_name):
    return CITY_COORDS.get(city_name)

def fetch_weather(lat,lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code&timezone=Asia/Shanghai"
    data = safe_get(url)
    if not data:
        return None,None
    return data["current"]["temperature_2m"], data["current"]["weather_code"]

def display_weather(city,temp,weather_code):
    wmo_map = {
        0:"晴",1:"少云",2:"多云",3:"阴",
        45:"雾",48:"霜雾",51:"毛毛雨",53:"毛毛雨",55:"毛毛雨",
        61:"小雨",63:"中雨",65:"大雨",
        71:"小雪",73:"中雪",75:"大雪",
        80:"阵雨",81:"阵雨",82:"强阵雨",
        95:"雷阵雨",96:"雷阵雨伴冰雹",99:"雷阵雨伴冰雹"
    }
    weather_desc = wmo_map.get(weather_code,"未知天气")

    console = Console()
    content = f"[bold cyan]城市:[/] {city}\n[bold yellow]温度:[/] {temp}\n[bold green]天气:[/] {weather_desc}"
    console.print(Panel(content,title= "今日天气",expand = False))

def main():
    if len(sys.argv) > 1:
        city = sys.argv[1]
    else:
        city = input("请输入城市名(默认广州):").strip()
        if not city:
            city = "广州"

    coords = get_coords(city)
    if not coords:
        print(f"查不到城市[{city}],请检查输入或预用的城市。")
        return

    lat,lon = coords
    print(f"正在查询{city}的天气...")
    temp,code = fetch_weather(lat,lon)

    if temp is None:
        print("抱歉，天气获取失败，请检查网络后重试。")
        return

    display_weather(city,temp,code)

if __name__ == "__main__":
    main()