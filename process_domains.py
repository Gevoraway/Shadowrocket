import re

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

# Добавляем префикс в верхнем регистре
processed_domains = sorted(f"DOMAIN-SUFFIX,{domain}" for domain in cleaned_domains)

# Записываем в новый файл
output_file = "domains_refilter.list"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(processed_domains))

print(f"Обработано {len(processed_domains)} доменов. Файл сохранен как {output_file}.")
