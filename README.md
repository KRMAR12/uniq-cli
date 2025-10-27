uniq-cli-CLI-утиліта на Python, що працює подібно до Unix-команди uniq.
--file, -f	Шлях до файлу для читання 
--ignore-case, -i	Ігнорувати регістр при порівнянні рядків
--ucount, -c	Показати кількість повторів кожного рядка
--lines, -l	Прочитати лише перші N рядків

Приклади
# Вивести унікальні рядки
docker run --rm -v "${PWD}:/app" mariakravchuk/uniq-cli -f /app/ex1.txt

# Ігнорувати регістр
docker run --rm -v "${PWD}:/app" mariakravchuk/uniq-cli -f /app/ex1.txt -i

# Показати кількість повторів
docker run --rm -v "${PWD}:/app" mariakravchuk/uniq-cli -f /app/ex1.txt -c

# Показати лише перші 10 рядків
docker run --rm -v "${PWD}:/app" mariakravchuk/uniq-cli -f /app/ex1.txt -l 10

Завантажити
docker pull mariakravchuk/uniq-cli:latest
Використовувати
docker run --rm -v "${PWD}:/app" mariakravchuk/uniq-cli --file /app/ex1.txt --ucount --ignore-case

