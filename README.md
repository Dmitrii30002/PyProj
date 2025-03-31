# PyProj
# TF-IDF Analyzer Web Application

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Веб-приложение для анализа текстовых файлов с вычислением TF-IDF метрик. Позволяет загружать текстовые документы и получать статистику по 50 наиболее значимым словам.

## 🚀 Особенности

- 📁 Загрузка текстовых файлов (.txt)
- 🔍 Анализ текста с вычислением TF (Term Frequency)
- 📊 Расчет IDF (Inverse Document Frequency)
- 🎯 Сортировка результатов по убыванию IDF
- 💻 Чистая архитектура с разделением на модули

## 📦 Структура проекта
PyP/
├── app.py # Основной файл приложения
├── config.py # Конфигурация
├── requirements.txt # Зависимости
│
├── static/ # Статические файлы
│
├── templates/ # HTML шаблоны
│ ├── upload.html # Форма загрузки
│ └── results.html # Таблица результатов
│
├── utils/ # Вспомогательные утилиты
│ ├── file_handlers.py # Работа с файлами
│ └── text_processing.py # Обработка текста
│
└── services/ # Бизнес-логика
├── tfidf_service.py # Вычисления TF-IDF
└── analysis_service.py # Сервис анализа

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/tfidf-analyzer.git
cd tfidf-analyzer
```
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3.Создайте папку для загрузок:
```bash
mkdir uploads
```
## Запуск
```bash
python app.py
```
