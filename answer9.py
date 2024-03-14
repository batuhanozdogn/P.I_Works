import pandas as pd
import re

data = {'Device_Type': ['AXO145', 'BTO231', 'AXO145', 'CTZ789'],
    'Stats_Access_Link': ['https://xcd32112.smart_meter.com/stats', 'http://bce45678.smart_meter.com/stats', 'https://xyz98765.smart_meter.com/stats', 'http://abc12345.smart_meter.com/stats']}
df = pd.DataFrame(data)
def extract_url(device_type, access_link):
    pattern = device_type + r'\.smart_meter\.com\/([a-zA-Z0-9_.]+)'
    match = re.search(pattern, access_link)
    if match:
        return match.group(0)
    else:
        return None

df['Pure_URL'] = df.apply(lambda row: extract_url(row['Device_Type'], row['Stats_Access_Link']), axis=1)
print(df)
