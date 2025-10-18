# 15️⃣ Logging Error Details

import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)

try:
    x = 10 /0
    x = 1 / 0
except Exception as e:
    logging.error("An error occured", e)