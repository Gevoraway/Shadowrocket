import re

# Загрузка списка доменов из файла
with open("domains.txt", "r", encoding="utf-8") as f:
    domains = f.readlines()

# Очистка и нормализация доменов
cleaned_domains = set()
for domain in domains:
    domain = domain.strip().lower()
    domain = re.sub(r"^www\.", "", domain)  # Удаляем "www."
    parts = domain.split(".")
    if len(parts) > 2:  # Преобразуем в домен второго уровня
        domain = ".".join(parts[-2:])
    cleaned_domains.add(domain)

# Добавление префикса
processed_domains = sorted(f"domain-suffix,{domain}" for domain in cleaned_domains)

# Запись в новый файл
with open("processed_domains.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(processed_domains))

print(f"Обработано {len(processed_domains)} доменов.")
