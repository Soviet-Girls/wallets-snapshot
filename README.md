# wallets-snapshot
Скрипт для получения списка кошельков владельцев NFT из коллекции.

## Установка
Клонируйте этот репозиторий. Создайте виртуальное окружение и активируйте его:
```sh
git clone https://github.com/Soviet-Girls/wallets-snapshot.git
python -m venv venv
. ./venv/bin/activate       # Unix
.\venv\Scripts\activate     # Windows CMD
.\venv\Scripts\activate.ps1 # Windows PS
```
Установите необходимые зависимости:
```sh
pip install -r requirements.txt
```
## Использование
Получить кошельки владельцев Soviet Girls:
```sh
python main.py
```

## Параметры запуска

| Аргумент     | Описание                                                                         |
| -------------| ---------------------------------------------------------------------------------|
| `--contract` | Адрес контракта в сети Polygon. По умолчанию указан адрес коллекции Soviet Girls |
| `--max`      | Сколько новых NFT может заминтить каждый владелец. По умолчаню 1.                |
| `--abi`      | JSON файл с ABI. По умолчанию thirdweb.json                                      |
| `--output`   | Название выходного файла                                                         |