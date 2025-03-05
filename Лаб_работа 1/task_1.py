import doctest
# TODO Написать 3 класса с документацией и аннотацией типов


class Box:
    def __init__(self, max_weight: int, number_objects: int, weight_objects: float):
        """
        Создание и подготовка к работе объекта "Коробка"
        :param max_weight: максимальная масса коробки
        :param number_objects: количество предметов в коробке
        :param weight_objects: масса предметов в коробке

        Примеры:
        >>> box = Box(20, 0, 0)  # инициализация экземпляра класса
        """
        if not isinstance(max_weight, int):
            raise TypeError("Макс. масса коробки должна быть типа int")
        if max_weight <= 0:
            raise ValueError("Макс. масса коробки должна быть положительным числом")
        self.max_weight = max_weight

        if not isinstance(number_objects, int):
            raise TypeError("Количество предметов в коробке должна быть типа int")
        if number_objects < 0:
            raise ValueError("Количество предметов в коробке не должно быть отрицательным числом")
        self.number_objects = number_objects

        if not isinstance(weight_objects, (int, float)):
            raise TypeError("Масса предметов в коробке должна быть типа int или float")
        if weight_objects < 0:
            raise ValueError("Масса предметов в коробке не должна быть отрицательным числом")
        self.weight_objects = weight_objects

    def is_empty_box(self) -> bool:
        """
        Функция которая проверяет является ли коробка пустой

        :return: Является ли коробка пустой

        Примеры:
        >>> box = Box(20, 0, 0)
        >>> box.is_empty_box()
        """
        ...

    def add_object_box(self, num_objects: int, weigt_add_object: float) -> None:
        """
        Функция котороя добавляет предметы в коробку
        :param num_objects: Количество добавляемых предметов
        :param weigt_add_object: Вес добавляемых предметов

        :raise ValueError: Если вес добавляемых предметов превышает максимальный вес в коробке, то вызываем ошибку

        Примеры:
        >>> box = Box(20, 0, 0)
        >>> box.add_object_box(2, 5)
        """

        if not isinstance(num_objects, int):
            raise TypeError("Добавляемое количество предметов должно быть типа int")
        if num_objects <= 0:
            raise ValueError("Добавляемое количество предметов должно быть положительным числом")

        if not isinstance(weigt_add_object, (int, float)):
            raise TypeError("Добовляемая масса предметов в коробке должна быть типа int или float")
        if weigt_add_object <= 0:
            raise ValueError("Добовляемая масса предметов в коробке должна быть положительным числом")
        ...


class House:
    def __init__(self, num_apartments: int, apartments_sold: int):
        """
        Создание и подготовка к работе объекта "Коробка"
        :param num_apartments: количество квартир
        :param apartments_sold: проданные квартиры

        Примеры:
        >>> house = House(20, 0)  # инициализация экземпляра класса
        """
        if not isinstance(num_apartments, int):
            raise TypeError("Количество квартир должно быть типа int")
        if num_apartments <= 0:
            raise ValueError("Количество квартир должно быть положительным числом")
        self.num_apartments = num_apartments

        if not isinstance(apartments_sold, int):
            raise TypeError("Проданные квартиры должны быть типа int")
        if apartments_sold < 0:
            raise ValueError("Проданные квартиры должны быть положительным числом")
        self.apartments_sold = apartments_sold

    def is_vacant_apartments(self) -> bool:
        """
        Функция которая проверяет есть ли свободные квартиры

        :return: Имеются ли свободные квартиры

        Примеры:
        >>> house = House(20, 15)
        >>> house.is_vacant_apartments()
        """
        ...

    def apartaments_for_sale(self, apart_sold_num: int) -> None:
        """
        Функция котороя продает квартиры
        :param apart_sold_num: Количество проданных квартир

        :raise ValueError: Если количество проданных квартир превышает количество свободных квартир, то вызываем ошибку

        Примеры:
        >>> house = House(20, 15)
        >>> house.apartaments_for_sale(5)
        """

        if not isinstance(apart_sold_num, int):
            raise TypeError("Количество проданных квартир должно быть типа int")
        if apart_sold_num < 0:
            raise ValueError("Количество проданных квартир должно быть положительным числом")
        ...


class VK:
    def __init__(self, number_users: int, number_users_in_network: int):
        """
        Создание и подготовка к работе объекта "Коробка"
        :param number_users: количество пользователей
        :param number_users_in_network: количество пользователей в сети

        Примеры:
        >>> vk = VK(2120, 0)  # инициализация экземпляра класса
        """
        if not isinstance(number_users, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if number_users <= 0:
            raise ValueError("Количество пользователей должно быть положительным числом")
        self.number_users = number_users

        if not isinstance(number_users_in_network, int):
            raise TypeError("Количество пользователей в сети должно быть типа int")
        if number_users_in_network < 0:
            raise ValueError("Количество пользователей в сети должно быть положительным числом")
        self.number_users_in_network = number_users_in_network

    def is_users_network(self) -> bool:
        """
        Функция которая проверяет есть ли пользователь в сети

        :return: есть ли пользователи в сети

        Примеры:
        >>> vk = VK(123213, 12)
        >>> vk.is_users_network()
        """
        ...

    def add_users_in_network(self, add_users_network: int) -> None:
        """
        Функция котороя продает квартиры
        :param add_users_network: Количество пользователей которые зашли в VK

        Примеры:
        >>> vk = VK(123213, 12)
        >>> vk.add_users_in_network(22)
        """

        if not isinstance(add_users_network, int):
            raise TypeError("Количество пользователей вошедших в VK должно быть типа int")
        if add_users_network < 0:
            raise ValueError("Количество пользователей вошедших в VK должно быть положительным числом")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
