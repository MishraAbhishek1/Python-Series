# 14️⃣ Caching Logic

cache = {}

def get_cached_data(key, fetch_func):
    if key in cache:
        return cache[key]
    data = fetch_func()
    cache[key] = data
    return data

print(get_cached_data("user1", lambda: "DB call done"))
print(cache["user1"])