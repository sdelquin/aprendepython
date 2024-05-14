from __future__ import annotations

DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
DAYS_OF_WEEK = (
    'Domingo',
    'Lunes',
    'Martes',
    'Miércoles',
    'Jueves',
    'Viernes',
    'Sábado',
)
MONTHS_IN_YEAR = (
    'enero',
    'febrero',
    'marzo',
    'abril',
    'mayo',
    'junio',
    'julio',
    'agosto',
    'septiembre',
    'octubre',
    'noviembre',
    'diciembre',
)
MIN_YEAR_LIMIT = 1900
MAX_YEAR_LIMIT = 2050


class Date:
    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos."""
        self.year = year if MIN_YEAR_LIMIT <= year <= MAX_YEAR_LIMIT else MIN_YEAR_LIMIT
        self.month = month if 0 < month < 12 else 1
        self.day = day if 0 < day < self.days_in_month else 1

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    @staticmethod
    def get_days_in_month(month: int, year: int) -> int:
        if month == 2 and Date.is_leap_year(year):
            return 29
        else:
            return DAYS_IN_MONTH[month - 1]

    @staticmethod
    def get_days_in_year(year: int) -> int:
        return 366 if Date.is_leap_year(year) else 365

    def get_delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        delta = self.day - 1
        for month in range(1, self.month):
            delta += Date.get_days_in_month(month, self.year)
        for year in range(MIN_YEAR_LIMIT, self.year):
            delta += Date.get_days_in_year(year)
        return delta

    @property
    def days_in_month(self) -> int:
        return Date.get_days_in_month(self.month, self.year)

    @property
    def weekday(self) -> int:
        return (self.get_delta_days() + 1) % 7

    @property
    def is_weekend(self) -> bool:
        return self.weekday in (0, 6)

    @property
    def day_name(self) -> str:
        return DAYS_OF_WEEK[self.weekday]

    @property
    def month_name(self) -> str:
        """Los meses del año, 0 para enero, 11 para diciembre"""
        return MONTHS_IN_YEAR[self.month - 1]

    @property
    def short_date(self) -> str:
        """02/09/2003"""
        return f'{self.day:02d}/{self.month:02d}/{self.year}'

    def __str__(self):
        """MARTES 2 DE SEPTIEMBRE DE 2003"""
        return (f'{self.day_name} {self.day} de {self.month_name} de {self.year}').upper()

    def __add__(self, days_to_add: int) -> Date:
        """Sumar un número de días a la fecha"""
        if isinstance(days_to_add, int):
            added_years, days_to_add = divmod(days_to_add, 365)
            new_year = self.year + added_years
            for year in range(self.year, new_year):
                if Date.is_leap_year(year):
                    first_leap_year = year
                    days_to_add += (new_year - first_leap_year) // 4
                    break
            for century in range(self.year // 100, new_year // 100):
                if (century * 100) % 400 != 0:
                    days_to_add -= 1
            remaining_days_month = Date.get_days_in_month(self.month, new_year) - self.day
            if (days_to_add - remaining_days_month) > 0:
                new_month = self.month + 1
                if new_month == 13:
                    new_year += 1
                    new_month = 1
                added_days = remaining_days_month
                while True:
                    added_days += Date.get_days_in_month(new_month, new_year)
                    if added_days < days_to_add:
                        new_month += 1
                        if new_month == 13:
                            new_month = 1
                            new_year += 1
                    else:
                        new_day = (
                            days_to_add + Date.get_days_in_month(new_month, new_year) - added_days
                        )
                        break
            else:
                new_month = self.month
                new_day = self.day + days_to_add
            if new_year > MAX_YEAR_LIMIT:
                print('Warning: max year limit reached')
                return Date(31, 12, MAX_YEAR_LIMIT)
            return Date(new_day, new_month, new_year)
        else:
            print('ERROR: se deben indicar los días a sumar como un entero.')
            return None

    def __sub__(self, other: Date | int) -> int | Date:
        """Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha"""
        if isinstance(other, int):
            sub_years, days_to_sub = divmod(other, 365)
            new_year = self.year - sub_years
            for year in range(new_year, self.year):
                if Date.is_leap_year(year):
                    first_leap_year = year
                    days_to_sub += (self.year - first_leap_year) // 4
                    break
            for century in range(new_year // 100, self.year // 100):
                if (century * 100) % 400 != 0:
                    days_to_sub -= 1
            if (days_to_sub - self.day) > 0:
                new_month = self.month - 1
                if new_month == 0:
                    new_year -= 1
                    new_month = 12
                substracted_days = self.day
                while True:
                    substracted_days += Date.get_days_in_month(new_month, new_year)
                    if substracted_days < days_to_sub:
                        new_month -= 1
                        if new_month == 0:
                            new_year -= 1
                            new_month = 12
                    else:
                        new_day = substracted_days - days_to_sub
                        break
            else:
                new_month = self.month
                new_day = self.day - days_to_sub
            if new_year < MIN_YEAR_LIMIT:
                print('Warning: min year limit reached')
                return Date(1, 1, MIN_YEAR_LIMIT)
            return Date(new_day, new_month, new_year)
        elif isinstance(other, Date):
            return self.get_delta_days() - other.get_delta_days()
        else:
            error = 'Error: solo esta soportada la resta de fechas o días.'
            return False, error

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Date):
            return self.get_delta_days() == other.get_delta_days()
        raise ValueError('Sólo está soportada la comparación entre fechas')

    def __gt__(self, other: Date) -> bool:
        if isinstance(other, Date):
            return self.get_delta_days() > other.get_delta_days()
        raise ValueError('Sólo está soportada la comparación entre fechas')

    def __lt__(self, other: Date) -> bool:
        if isinstance(other, Date):
            return self.get_delta_days() < other.get_delta_days()
        raise ValueError('Sólo está soportada la comparación entre fechas')
