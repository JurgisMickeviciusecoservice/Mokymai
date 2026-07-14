import json
import csv
from pathlib import Path

src = Path(r"c:\Users\jurgis.mickevicius\AppData\Roaming\Code\User\workspaceStorage\d1f373f677853a6bb6fde35a075c269a\GitHub.copilot-chat\chat-session-resources\d6a84035-9a84-48cf-a7d0-636e994008f0\call_cDaIqkApH0TgdrorAjHYiR1O__vscode-1783925847654\content.json")
out = Path(r"c:\Users\jurgis.mickevicius\OneDrive - UAB Ecoservice\Desktop\Jurgis_Mickevicius_task\2026_07-13_test\bill_contractmessage_export.csv")

with src.open('r', encoding='utf-8') as fh:
    data = json.load(fh)

print('keys', list(data.keys())[:10])
if isinstance(data, dict):
    rows = data.get('rows')
    column_info = data.get('columnInfo', [])
    columns = [c.get('columnName') for c in column_info]
    if not rows:
        raise SystemExit('No rows found in exported JSON payload')
else:
    raise SystemExit('Unexpected JSON structure')

with out.open('w', encoding='utf-8-sig', newline='') as fh:
    writer = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(columns)
    for row in rows:
        writer.writerow(row)

print('WROTE', out)
print('ROWS', len(rows))
print('COLUMNS', columns)
