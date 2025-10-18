# 11️⃣ Pagination Logic

def paginate(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end]

print(paginate([1,2,3,4,5,6,7,8], 2, 3))  # [4,5,6]
