import re
from datetime import datetime

# Адрес источника
source_url = "https://raw.githubusercontent.com/1andrevich/Re-filter-lists/main/domains_all.lst"

# Читаем список доменов
with open("domains.txt", "r", encoding="utf-8") as f:
    domains = f.readlines()

# Обрабатываем: убираем дубликаты, удаляем "www" и "wwww", оставляем только домены второго уровня
cleaned_domains = set()
for domain in domains:
    domain = domain.strip().lower()

    # Преобразуем в домен второго уровня
    parts = domain.split(".")
    if len(parts) > 2:
        domain = ".".join(parts[-2:])

    # Удаляем домены, начинающиеся на "www" или "wwww"
    if not domain.startswith(("www", "wwww")):
        cleaned_domains.add(domain)

# Формируем список с префиксом в верхнем регистре
processed_domains = sorted(f"DOMAIN-SUFFIX,{domain}" for domain in cleaned_domains)

# Добавляем дату, количество доменов и источник
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
header = [
    f"# Обновлено: {timestamp}",
    f"# Количество доменов: {len(processed_domains)}",
    f"# Источник: {source_url}",
    ""
]

# Итоговый список с заголовком
final_output = "\n".join(header + processed_domains)

# Записываем в новый файл
output_file = "domains_refilter.list"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_output)

print(f"Обработано {len(processed_domains)} доменов. Файл сохранен как {output_file}.")
