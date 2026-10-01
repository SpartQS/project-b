# Project B — Utils

Библиотека вспомогательных функций для использования в других проектах.

## Возможности

Project B содержит модули для:

* работы с датами;
* работы со строками;
* работы с файлами;
* логирования.

## Модули

### date_utils

Функции для работы с датами.

### string_utils

Функции для обработки строк:

* разворот строки;
* преобразование слов;
* подсчёт количества слов.

### file_utils

Функции для работы с файлами:

* чтение файла;
* запись файла.

### logger_utils

Функции для создания и настройки логирования.

## Установка

Установить библиотеку локально:

```powershell
pip install -e .
```

## Использование в Project A

Project A подключает Project B как Python-пакет:

```powershell
pip install -e ../project-b
```

После установки функции библиотеки можно импортировать в приложении:

```python
from project_b_utils.date_utils import get_current_date
from project_b_utils.string_utils import reverse_string
from project_b_utils.file_utils import read_file, write_file
from project_b_utils.logger_utils import get_logger
```

## Тестирование

Запустить тесты:

```powershell
pytest
```

## Версия

Текущая версия библиотеки: `1.0.1`.
