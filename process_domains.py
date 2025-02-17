import re
from datetime import datetime

# Читаем список доменов
with open("domains.txt", "r", encoding="utf-8") as f:
    domains = f.readlines()

# Обрабатываем: убираем дубликаты, оставляем только домены второго уровня
cleaned_domains = set()
for domain in domains:
    domain = domain.strip().lower()
    domain = re.sub(r"^www\.", "", domain)  # Удаляем "www."
    parts = domain.split(".")
    if len(parts) > 2:  # Преобразуем в домен второго уровня
        domain = ".".join(parts[-2:])
    cleaned_domains.add(domain)

# Формируем список с префиксом в верхнем регистре
processed_domains = sorted(f"DOMAIN-SUFFIX,{domain}" for domain in cleaned_domains)

# Добавляем дату и время обновления
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
header = [
    f"# Обновлено: {timestamp}",
    f"# Количество доменов: {len(processed_domains)}",
    ""
]

# Итоговый список с заголовком
final_output = "\n".join(header + processed_domains)

# Записываем в новый файл
output_file = "domains_refilter.list"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_output)

print(f"Обработано {len(processed_domains)} доменов. Файл сохранен как {output_file}.")
