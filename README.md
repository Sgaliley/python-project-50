### Hexlet tests and linter status:
[![Actions Status](https://github.com/Sgaliley/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Sgaliley/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b9a35673e6737e98d91c/maintainability)](https://codeclimate.com/github/Sgaliley/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/df66c0cbbeca7d822f23/test_coverage)](https://codeclimate.com/github/hexlet-boilerplates/python-package/test_coverage)

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