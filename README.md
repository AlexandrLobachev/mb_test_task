# Задание №1

## Библиотека Geametria.

Основными возможнастями являеться расчет площади треугольника по длине трех сторон и расчет площади круга по радиусу.

### Примеры работы:

#### Треугольник:
```
# создаем экземляр класса, где 6, 6, 10 - это длины сторон.
triangle = Triangle(6, 6, 10)

# метод get_area() возвращает площадь фигуры.
area = triangle.get_area()
```
Проверить являеться ли экземляр класса Triangle прямууголным треугольником возможно методом is_right_triangle()
```
# метод is_right_triangle() возвращает значение типа bool.
triangle.is_right_triangle()

```

#### Круг:
```
# создаем экземляр класса, где 10 - это радиус круга.
circle = Circle(10)

# метод get_area() возвращает площадь фигуры.
area = circle.get_area()
```

# Задание№2

Метод get_products() возвращает в одном датафрейме все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.

### Пример работы:
Входные данные три DataFrame: product, category, relations
```
# DataFrame product
+----------+------------+  
|product_id|product_name|
+----------+------------+
|         1|    Product1|
|         2|    Product2|
|         3|    Product3|
|         4|    Product4|
|         5|    Product5|
|         6|    Product6|
|         7|    Product7|
+----------+------------+

# DataFrame category
+-----------+-------------+
|category_id|category_name|
+-----------+-------------+
|          1|        Cat_1|
|          2|        Cat_2|
|          3|        Cat_3|
|          4|        Cat_4|
+-----------+-------------+

# DataFrame relations
+----------+-----------+
|product_id|category_id|
+----------+-----------+
|         1|          1|
|         2|          2|
|         3|          1|
|         3|          2|
|         3|          3|
|      NULL|          4|
|         4|       NULL|
|         5|          1|
+----------+-----------+


```
Пример вызова метода:

```
df = get_products(product, category, relations)
df.show(10)
```
DataFrame возвращенный методом:
```
+----------------+
|         Results|
+----------------+
|Product5 - Cat_1|
|Product3 - Cat_1|
|Product1 - Cat_1|
|Product3 - Cat_2|
|Product2 - Cat_2|
|Product3 - Cat_3|
|        Product7|
|        Product6|
+----------------+
```

## Автор:

[Александр Лобачев](https://github.com/AlexandrLobachev/)