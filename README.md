### Hexlet tests and linter status:
[![Actions Status](https://github.com/Sgaliley/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Sgaliley/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/4fab0988a10920c3d66d/maintainability)](https://codeclimate.com/github/Sgaliley/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4fab0988a10920c3d66d/test_coverage)](https://codeclimate.com/github/Sgaliley/python-project-50/test_coverage)
## Описание
Вычислитель отличий – программа, которая определяет разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество онлайн-сервисов, например, jsondiff. Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменений в конфигурационных файлах.

Возможности утилиты:
* Поддержка разных входных форматов: yaml, json
* Генерация отчета в виде plain text, stylish и json

Пример использования:

```
gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```

## Установка

Перед установкой пакета необходимо убедиться, что у вас установлен Python версии 3.11 или выше:
```bash
# Linux:
>> python3 --version # or python -V
Python 3.11.0+
```
обновить
```
>> sudo apt-get update && sudo apt-get upgrade python3.X
```
установить
```
>> sudo apt update && sudo apt-get install python3.X
```
Установить PIP и Poetry и make

```
>> sudo apt-get install python3-pip
>> sudo apt-get install python3-poetry
>> sudo apt-get install make
```

Клонируем проект
```
# clone via HTTPS:
>> git clone https://github.com/Sgaliley/python-project-50.git
```
Переходим в проект и устанавливаем пакет
```
>> cd python-project-lvl1
>> make build
>> make package-install

```
Запуск
```
>> gendiff -h
>> gendiff file1.json file2.yml
>> gendiff -f stylish file3.json file4.yml
>> gendiff -f plain file3.json file4.yml
>> gendiff -f json file3.json file4.yml
```

### Демонстрация Gendiff

[![asciicast](https://asciinema.org/a/UjcJxapaONTMCJEFqvb14B8LQ.svg)](https://asciinema.org/a/UjcJxapaONTMCJEFqvb14B8LQ)