import numpy as np
from math import sqrt
from textwrap import dedent


class GridProcessing:

    def _incorrect_ratio_message(self, original_size: tuple, converted_size: tuple) -> str:

        original_column, original_row = original_size
        resized_column, resized_row = converted_size

        return dedent(f"""            Grid conversion ratio is incorrect.
              Converted grid size (column, row): ({resized_column},{resized_row})
              Original grid size (column, row): ({original_column},{original_row})
              
              Requirements:
                - Converted grid size must be smaller than original grid size.
                - The original grid size must be divisible by converted grid size.

              Examples:
                .---------------.------------------------------.
                | Original Size |   Accepted Converted Sizes   |
                '---------------'------------------------------'
                |    (32,32)    | (16,16), (8,8), (4,4), (2,2) |
                |    (16,16)    | (8,8), (4,4), (2,2)          |
                |     (8,8)     | (4,4), (2,2)                 |
                |     (4,4)     | (2,2)                        |
                '---------------'------------------------------'
            """)

    def _incorrect_length_message(self, current_length: int) -> str:
        return dedent(f"""            Data length is incorrect.
              Current length:
                {current_length}

              Requirements:
                - The length must be equal to column x row, where column = row.
                - The length must be equal to 2^(n+2), where n is an even number and n>=0 (0,2,4,...)
                - The square root of length must be equal to round number.
              
              Examples:
                .----------------------.----------------------.
                | Accepted Data Length |  (Column, Row) Size  |
                '----------------------'----------------------'
                |          4096        |       (64,64)        |
                |          1024        |       (32,32)        |
                |           256        |       (16,16)        |
                |            64        |         (8,8)        |
                |            16        |         (4,4)        |
                |             4        |         (2,2)        |
                '----------------------'----------------------'
                """)

    def _convert_string_list_to_ndarray(self, raw_data: list) -> np.ndarray:

        flat_list = list(map(float, raw_data.split(',')))

        dim = int(sqrt(len(flat_list)))
        if len(flat_list) != dim**2:
            raise ValueError(
                self._incorrect_length_message(current_length=len(flat_list)))

        return np.reshape(flat_list, (dim, dim))

    def _check_ndarray_size(self, column: int, row: int,
                            resized_column: int, resized_row: int) -> bool:

        if (resized_column > column) or (resized_row > row) or (column % resized_column != 0) or (row % resized_row != 0):
            raise ValueError(
                self._incorrect_ratio_message(original_size=(column, row), converted_size=(resized_column, resized_row)))

        return True

    def _resized_grid_calculation(self,
                                  array_2d: np.ndarray, columns_per_grid: int, rows_per_grid: int,
                                  current_column: int, current_row: int) -> float:

        return round(np.mean([array_2d[(
            current_column * columns_per_grid) + tg_col_n][(current_row * rows_per_grid) + tg_row_n]
            for tg_col_n in range(columns_per_grid)
            for tg_row_n in range(rows_per_grid)]), 2)

    def _resize_matrix(self, array_2d: np.ndarray, column: int, row: int) -> list:

        columns_per_grid = int(32 / column)
        rows_per_grid = int(32 / row)

        return [self._resized_grid_calculation(
            array_2d=array_2d,
            columns_per_grid=columns_per_grid,
            rows_per_grid=rows_per_grid,
            current_column=res_col_n,
            current_row=res_row_n)
            for res_col_n in range(column)
            for res_row_n in range(row)]

    def grid_statistics(self, array: np.ndarray) -> dict:
        return {
            # "ref_temp": round(float(sensor_data["ref_temp"]), 3),
            "mean": round(np.mean(array), 3),
            "max": round(np.max(array), 3),
            "min": round(np.min(array), 3),
            "median": round(np.median(array), 3)
        }

    def _convert(self, raw_data: str, resized_column: int, resized_row: int) -> np.ndarray:
        array_2d = self._convert_string_list_to_ndarray(raw_data)
        column, row = np.shape(array_2d)
        self._check_ndarray_size(
            column=column, row=row, resized_column=resized_column, resized_row=resized_row)

        return np.reshape(
            self._resize_matrix(array_2d=array_2d,
                                column=resized_column, row=resized_row),
            (resized_column, resized_row))

    def convert_to_2x2(self, raw_data: str) -> np.ndarray:
        return self._convert(raw_data=raw_data, resized_column=2, resized_row=2)

    def convert_to_4x4(self, raw_data: str) -> np.ndarray:
        return self._convert(raw_data=raw_data, resized_column=4, resized_row=4)

    def convert_to_8x8(self, raw_data: str) -> np.ndarray:
        return self._convert(raw_data=raw_data, resized_column=8, resized_row=8)

    def convert_to_16x16(self, raw_data: str) -> np.ndarray:
        return self._convert(raw_data=raw_data, resized_column=16, resized_row=16)
