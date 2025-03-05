if __name__ == "__main__":
    "Базовый класс Транспорт"
    class Transport:
        def __init__(self, name_transport: str, max_passagers: int, speed: float):
            """
            :param name_transport: название транспорта
            :param max_passagers: максимальное количество пассажиров
            :param speed: максимальная скорость

            Примеры:
            >>> transport = Transport("Boing 777", 500, 900)
            """
            self._name_transport = name_transport
            self._max_passagers = max_passagers
            self._speed = speed


        def __str__(self) -> str:
            return f"Транспорт: {self.name_transport}; Макс. пассажиров: {self.max_passagers}; Макс. скорость: {self.speed};"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name_transport!r}, max_passagers={self.max_passagers!r}, speed={self.speed!r},)"

        @property
        def name_transport(self) -> str:
            return self._name_transport

        @property
        def max_passagers(self) -> int:
            return self._max_passagers

        @property
        def speed(self) -> float:
            return self._speed

        def parametr_transport(self) -> str:
            """
            Метод параметры транспорта возращает параметры транспорта

            :return: str

            >>> transport = Transport("Boing 777", 500, 900)
            >>> transport.parametr_transport()
            """
            return f"""Транспорт: {self.name_transport}; 
            Макс. пассажиров: {self.max_passagers}; 
            Макс. скорость: {self.speed};"""


    "Дочерний класс Самолет унаследован от базового класса Транспорт"
    class Plane(Transport):
        def __init__(self, name_transport: str, max_passagers: int, speed: float, flying_height: float):
            """
            :param name_transport: название транспорта
            :param max_passagers: максимальное количество пассажиров
            :param speed: максимальная скорость
            :param flying_height: высота полета

            Примеры:
            >>> plane = Plane("Boing 777", 500, 900, 10000)
            """
            super().__init__(name_transport, max_passagers, speed)
            self._flying_height = flying_height

        @property
        def flying_height(self) -> float:
            return self._flying_height

        def __str__(self) -> str:
            return f"Транспорт: {self.name_transport}; Макс. пассажиров: {self.max_passagers}; Макс. скорость: {self.speed}; Высота полета: {self.flying_height}"

        def parametr_transport(self) -> str:
            """
            Метод параметры трансорта перегружен для добаления еще одного параметра

            :return: str

            >>> plane = Plane("Boing 777", 500, 900, 10000)
            >>> plane.parametr_transport()
            """
            return f"""{super().parametr_transport()}
            Высота полета: {self.flying_height}"""
