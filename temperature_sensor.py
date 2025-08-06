import random
from datetime import datetime

def get_current_temperature():
    # 随机生成温度（假设人体温度范围）
    temperature = round(random.uniform(36.0, 37.5), 2)

    # 获取当前时间（ISO 8601 格式）
    timestamp = datetime.now().isoformat()

    # 返回结果为字典（可用于 JSON 输出）
    return {
        "temperature": temperature,
        "timestamp": timestamp
    }
