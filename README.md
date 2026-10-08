# w3-weather
用python requests/open-meteo/rich 练手的小天气查询器

## 环境要求
    -Python 3.10+
    -依赖：rich、requests、python-dotenv

## 运行方式
**cmd**
```
pip install -r requirements.txt
python w3/day5.py 广州
```

**git bash**
```angular2html
pip install -r requirements.txt
python w3/day5.py 广州
```

## 目录结构
- **Day1** requests 入门：看懂 `fetch_weather` 怎么发请求、拿响应
- **Day2** JSON 解析：自己 `print(data)` 看结构，手动从 `current` 取字段
- **Day3** 错误处理 + 重试：把 `get_json` 升级成 `safe_get`（加 `timeout=5` + 重试 3 次）
- **Day4** 密钥/配置管理：把 `LAT/LON/CITY` 抽到 `.env`，用 `python-dotenv` 读
- **Day5** 组合成完整工具：支持多城市 / 命令行参数

## 文件说明
| 文件 | 作用 |
|---|---|
| `weather_card.py` | 主脚本：fetch + render 天气卡片（Day2 动手） |
| `requirements.txt` | 依赖清单（requests / rich） |
| `.gitignore` | 忽略 `venv/`、`.env`、`__pycache__` |
|`w3/`|每日主要完成内容|