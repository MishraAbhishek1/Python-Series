# 13️⃣ Environment Variable Access

import os

def get_db_url():
    return os.getenv('DATABASE_URL', 'sqlite:///:memory:')

print(get_db_url())