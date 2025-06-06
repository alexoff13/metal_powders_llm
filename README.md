# metal_powders_llm
## Общее описание

Этот проект предназначен для сбора, обработки и анализа данных о металлопорошковых материалах из открытых источников. Проект включает в себя:

1. Парсинг данных с веб-сайтов
2. Обработку текстовых описаний с использованием языковых моделей
3. Преобразование данных в структурированный JSON-формат
4. Сравнение результатов работы разных языковых моделей

## Файлы проекта

### `parser_html.py`
- **Описание**: Модуль для парсинга данных с веб-сайтов о металлопорошковых материалах.
- **Функционал**:
  - Получение списка категорий материалов
  - Сбор ссылок на страницы с описаниями материалов
  - Извлечение и очистка текстовых описаний материалов
- **Зависимости**: `requests`, `BeautifulSoup`

### `consts.py`
- **Описание**: Содержит шаблон PROMPT для языковых моделей с описанием требуемого JSON-формата.
- **Функционал**: Предоставляет стандартизированный запрос для обработки текстовых описаний.

### `gemini_llm.py`
- **Описание**: Модуль для обработки текстовых описаний с использованием модели Gemini от Google.
- **Функционал**:
  - Настройка подключения к API Gemini
  - Генерация структурированных JSON-данных на основе текстовых описаний
  - Сохранение результатов в файл
- **Зависимости**: `google.generativeai`

### `mistral.py`
- **Описание**: Модуль для обработки текстовых описаний с использованием модели Mistral (Zephyr-7b-beta).
- **Функционал**:
  - Загрузка и настройка локальной модели
  - Генерация JSON-структур на основе текстовых описаний
  - Обработка ошибок парсинга
- **Зависимости**: `transformers`

### `to_IACPC_format.py`
- **Описание**: Модуль для преобразования сырых JSON-данных в стандартизированный формат IACPC.
- **Функционал**:
  - Трансформация структуры данных
  - Объединение информации о материалах
  - Сохранение результата в файл

### `compare_llm.py`
- **Описание**: Модуль для сравнения результатов работы моделей Gemini и Mistral.
- **Функционал**:
  - Сравнение структур JSON
  - Анализ различий в конкретных значениях
  - Подсчет ошибок парсинга

## Как запустить проект

1. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Обработка данных с помощью языковых моделей**:
   - Для Gemini (требуется API-ключ):
     ```bash
     python gemini_llm.py
     ```
   - Для Mistral:
     ```bash
     python mistral.py
     ```
     
5. **Сравнение результатов** (опционально):
   - Для сравнения результатов работы разных моделей:
     ```bash
     python compare_llm.py
     ```
     
4. **Преобразование данных**:
   - После получения результатов от языковых моделей, преобразуйте их в стандартный формат:
     ```bash
     python to_IACPC_format.py
     ```



## Требования

- Python 3.8+
- API-ключ для Gemini (для `gemini_llm.py`)
- Достаточные вычислительные ресурсы для работы с локальной моделью Mistral
- Запуск производился на MAC OS 15.4.1. Процессор Apple M1 Pro. Видеокарта - нет.

## Выходные данные

- `output.txt` - сырые результаты от Gemini
- `output_mistral.txt` - сырые результаты от Mistral
- `output.json` - финальный структурированный файл в формате IACPC