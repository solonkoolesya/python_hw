### Создание виртуального окружения

```
python -m venv env
```

### Активация виртуального окружения

```
(OSX/Linux) . env/bin/activate
(Windows)   . env/Scripts/activate.bat
```

### Установка зависимостей

```
pip install -r requirements.txt
```

### Запуск тестов

```
pytest test_homeworkNN.py
```
Опционально, если задание содержит doctest:

```
python homeworkNN.py
```