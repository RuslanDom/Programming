import re
from typing import List, Optional
from flask import Flask,request

app = Flask(__name__)

# Тестовый запрос:
# http://127.0.0.1:5000/search/?cell_tower_id=1&date_from=2022.12.1&phone_prefix=995*&phone_prefix=903*&protocol=2G&signal_level=-100

@app.route("/search/", methods=["GET"])
def search():
    cell_tower_ids: List[int] = request.args.getlist('cell_tower_id', type=int)

    if not cell_tower_ids:
        return f"Вы должны указать хотя бы один cell_tower_id", 400

    pattern_date = '^[0-9]{2,4}+\.[0-9]{,2}+\.[0-9]{,2}$'
    date_from: Optional[str] = request.args.get('date_from', type=str, default=None)
    if date_from:
        if not re.match(pattern=pattern_date, string=date_from):
            return "Дата указана не верно",400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")
    pattern_prefix = '^[0-9]{3}+\*$'
    for i in range(len(phone_prefixes)):
        if not re.match(pattern_prefix, phone_prefixes[i]):
            return f"Не верно указан префикс: {phone_prefixes[i]}", 400

    protocols: List[str] = request.args.getlist('protocol')
    pattern_protocol = '[2G3G4G]'
    for i in range(len(protocols)):
        if not re.match(pattern_protocol, protocols[i]):
            return f'Не верно указан протокол: {protocols[i]}', 400
    signal_level: Optional[float] = request.args.get('signal_level', type=float, default=None)

    return (
        f"Search for {cell_tower_ids} cell towers. Search criteria:"
        f"date_from={date_from},"
        f"phone_prefixes={phone_prefixes},"
        f"protocol s={protocols},"
        f"signal_level={signal_level}"
    )

# Полученный ответ будет:
# Search for [1] cell towers. Search criteria:date_from=2022.12.1,phone_prefixes=['995*', '903*'],protocol s=['2G'],signal_level=-100.0

if __name__ == "__main__":
    app.run(debug=True)




