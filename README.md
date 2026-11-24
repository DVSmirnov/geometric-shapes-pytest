# geometric-shapes-pytest

Небольшая учебная библиотека геометрических фигур на Python и набор тестов к ней на pytest.
Проект из курса по автоматизации тестирования (Python), доведённый до аккуратного состояния.

## Что умеет

Фигуры: `Circle`, `Rectangle`, `Square`, `Triangle`. У каждой есть:

- `area` — площадь;
- `perimeter` — периметр;
- `add_area(other)` — сумма площадей с другой фигурой.

Некорректные данные отклоняются: стороны и радиус должны быть больше нуля,
треугольник должен существовать (сумма двух сторон строго больше третьей).
Если в `add_area` передать не фигуру, будет `TypeError`.

## Пример

```python
from shapes import Circle, Rectangle, Triangle

rect = Rectangle(2, 5)
print(rect.area)       # 10
print(rect.perimeter)  # 14

triangle = Triangle(3, 4, 5)
print(triangle.area)   # 6.0

print(rect.add_area(triangle))  # 16.0
```

## Структура

```
shapes/            # код: Figure (абстрактный класс) и конкретные фигуры
tests/             # тесты pytest
  conftest.py      # фикстуры с эталонными площадями (посчитаны вручную)
  test_*.py        # по файлу на фигуру + test_figure.py для общего поведения
pytest.ini         # настройки pytest
.github/workflows  # автозапуск тестов в GitHub Actions
```

## Запуск тестов

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Что проверяют тесты

- площадь и периметр каждой фигуры на конкретных значениях;
- отклонение некорректных данных (ноль, отрицательные, вырожденный треугольник);
- `add_area` для всех 16 пар фигур, коммутативность и ошибка на «не фигуре»;
- что `Figure` нельзя создать напрямую (абстрактный класс).
