from datetime import datetime, timezone

# 方法 2：使用带时区的 UTC 时间（更推荐，避免本地时区影响）
# utc_time_with_tz = datetime.now(timezone.utc)
# timestamp2 = utc_time_with_tz.timestamp()
# print(timestamp2)


# 方法 1：使用 utcnow() 获取 UTC 时间，再转换为时间戳（不带时区信息）
utc_time = datetime.utcnow()
timestamp1 = utc_time.timestamp()

print(timestamp1)

utc_time = datetime.utcfromtimestamp(timestamp1)
formatted_utc = utc_time.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_utc)

print(1+2+3+4)
