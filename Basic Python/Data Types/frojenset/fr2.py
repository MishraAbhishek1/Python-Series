# 2️⃣ Try adding element (will raise error)

fs = frozenset([1, 2, 3])
try:
    fs.add(4)
except AttributeError:
    print("❌ Frozenset is immutable!")