import numpy as np
import statistics


class GridData:

    def __init__(self):
        self.__raw_data = []
        self.__2x2 = np.zeros(shape=(2, 2))
        self.__4x4 = np.zeros(shape=(4, 4))
        self.__8x8 = np.zeros(shape=(8, 8))
        self.__16x16 = np.zeros(shape=(16, 16))
        self.__grid_statistics = {}

    def _convert_string_list_to_float_list(self, raw_data: str):
        return list(map(float, raw_data.split(',')))

    def _convert_list_to_ndarray(self, data_list: list) -> np.ndarray:
        return np.reshape(data_list, (32, 32))

    def _resized_grid_calculation(self, columns_per_grid: int, rows_per_grid: int, current_column: int, current_row: int) -> float:

        return round(statistics.mean([self.__raw_data[(
            current_column * columns_per_grid) + tg_col_n][(current_row * rows_per_grid) + tg_row_n]
            for tg_col_n in range(columns_per_grid)
            for tg_row_n in range(rows_per_grid)]), 2)

    def _resize_matrix(self, column: int, row: int) -> list:

        columns_per_grid = int(32 / column)
        rows_per_grid = int(32 / row)

        return [self._resized_grid_calculation(
            columns_per_grid=columns_per_grid,
            rows_per_grid=rows_per_grid,
            current_column=res_col_n,
            current_row=res_row_n)
            for res_col_n in range(column)
            for res_row_n in range(row)]

    def raw_data(self, data: str):
        data_list = self._convert_string_list_to_float_list(
            raw_data=data)

        self.__grid_statistics = {
            "mean_temp": round(statistics.mean(data_list), 3),
            "max_temp": round(max(data_list), 3),
            "min_temp": round(min(data_list), 3),
            "median_temp": round(statistics.median(data_list), 3)
        }

        self.__raw_data = self._convert_list_to_ndarray(data_list=data_list)

        return self

    @property
    def get_grid_statistics(self) -> dict:
        return self.__grid_statistics

    @property
    def convert_to_2x2(self) -> np.ndarray:
        self.__2x2 = np.reshape(self._resize_matrix(column=2, row=2), (2, 2))
        return self.__2x2

    @property
    def convert_to_4x4(self) -> np.ndarray:
        self.__4x4 = np.reshape(self._resize_matrix(column=4, row=4), (4, 4))
        return self.__4x4

    @property
    def convert_to_8x8(self) -> np.ndarray:
        self.__8x8 = np.reshape(self._resize_matrix(column=8, row=8), (8, 8))
        return self.__8x8

    @property
    def convert_to_16x16(self) -> list:
        self.__16x16 = np.reshape(
            self._resize_matrix(column=16, row=16), (16, 16))
        return self.__16x16
