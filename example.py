from dataprocessing import GridProcessing

# Data length is 1024
data = """
        29.6,28.8,28.4,27.7,26.8,28.3,28.1,27.7,27.5,28.3,28.7,29.0,27.7,28.7,27.8,29.2,26.9,28.0,26.6,28.2,28.1,28.1,26.9,27.0,26.8,27.3,27.7,28.0,27.8,27.6,28.1,30.7,
        28.4,27.8,27.7,29.3,28.6,28.6,28.2,27.6,27.4,28.2,26.7,28.5,27.5,28.2,27.8,28.7,27.1,27.7,26.8,28.1,27.9,26.2,27.5,27.9,27.2,27.5,27.6,27.2,27.4,27.2,28.3,28.4,
        28.2,27.2,28.3,27.9,28.3,28.1,27.7,27.3,27.7,26.8,27.5,27.7,27.2,27.4,28.3,27.9,28.0,28.3,28.5,28.3,27.5,27.6,28.2,27.7,28.0,27.7,27.0,27.1,27.7,28.6,27.8,27.1,
        28.2,27.5,28.2,27.9,27.8,28.1,27.4,27.9,27.6,27.8,27.2,28.0,28.9,27.9,27.6,28.0,28.0,28.5,28.3,27.0,27.5,27.7,27.4,27.1,27.1,27.6,26.7,26.5,26.7,27.1,27.4,26.2,
        27.9,27.0,27.0,27.1,27.5,27.6,27.6,28.1,27.2,27.4,28.6,28.1,28.4,27.6,27.0,27.6,27.4,27.5,27.0,27.4,27.1,28.1,27.5,27.8,26.7,26.9,27.7,26.6,26.9,27.5,27.3,27.7,
        28.9,28.2,27.0,26.6,27.3,28.1,27.3,27.4,27.2,27.7,27.5,27.8,27.3,27.9,27.8,27.5,28.4,27.1,28.3,27.3,28.0,27.2,27.4,28.0,27.2,27.3,28.0,27.6,27.3,27.1,26.7,25.9,
        27.8,28.1,27.9,27.5,28.4,27.5,27.6,28.1,28.1,27.9,27.7,28.3,28.3,28.3,27.5,28.2,28.0,27.6,27.9,27.7,27.6,27.3,28.4,27.6,27.6,27.5,26.8,27.1,25.8,26.2,26.2,26.7,
        27.3,27.1,27.2,27.3,26.9,28.6,27.7,28.2,28.5,28.3,27.6,27.8,28.2,28.0,28.7,28.0,28.1,27.8,28.3,27.8,27.4,28.2,26.9,26.8,27.7,26.8,27.5,25.8,26.9,27.1,26.8,26.8,
        27.5,27.5,26.9,27.8,28.1,28.2,27.3,27.6,27.5,27.6,28.3,28.2,27.9,27.8,27.8,27.6,27.5,27.6,27.9,27.9,27.3,27.5,27.1,27.9,27.6,28.0,28.0,27.0,26.1,28.1,26.7,27.2,
        27.7,26.3,26.9,27.7,27.2,28.1,27.5,26.8,26.6,27.8,27.7,27.8,27.2,27.7,27.1,28.0,28.3,27.2,27.5,27.1,27.6,27.8,27.5,27.5,27.2,27.3,27.9,27.6,26.9,27.3,26.7,26.1,
        27.0,27.7,27.6,27.5,28.1,27.4,27.1,26.9,27.8,27.4,27.8,28.0,27.4,27.7,27.3,27.6,27.3,27.6,28.2,28.2,27.4,27.5,27.8,27.5,27.4,27.4,27.0,27.1,26.7,28.0,26.9,24.0,
        27.5,27.4,27.7,27.7,27.9,27.5,27.8,27.9,27.5,27.4,27.0,28.2,27.9,27.3,27.8,27.6,27.8,27.6,28.1,27.8,27.7,27.8,28.6,28.0,27.6,27.3,27.5,26.9,27.4,27.9,28.9,29.4,
        28.0,27.8,27.9,27.5,27.4,27.8,27.7,27.5,27.7,27.0,28.1,27.3,27.7,27.6,26.7,27.7,27.2,27.4,27.2,27.9,28.1,27.7,27.6,27.5,28.0,27.6,27.5,26.5,26.5,27.1,27.0,27.2,
        27.4,27.3,27.4,27.9,28.0,27.2,27.8,27.6,27.7,27.9,27.4,27.6,27.8,27.7,27.5,27.3,27.7,27.9,27.7,27.9,27.6,27.8,28.1,27.6,27.2,27.4,27.2,28.1,28.0,26.8,27.1,27.3,
        26.8,26.8,27.6,27.7,27.5,27.7,27.6,27.9,27.9,27.2,27.3,27.9,27.4,27.5,28.0,28.1,27.8,27.3,28.2,28.3,27.6,28.4,27.8,27.3,27.8,27.2,26.6,26.7,27.4,26.9,25.8,25.6,
        28.3,28.1,27.9,27.4,27.6,26.4,28.2,27.3,27.4,27.7,27.9,27.8,28.4,27.2,27.8,27.7,27.9,27.8,27.7,27.5,28.5,28.2,27.2,27.4,27.5,27.9,26.7,28.0,27.1,26.7,27.8,28.3,
        28.5,28.2,27.6,27.2,27.6,27.4,28.0,27.7,27.3,27.6,27.8,28.3,28.0,27.7,28.1,27.7,27.6,26.7,27.6,27.6,27.6,27.5,27.6,27.6,27.8,27.3,26.9,27.7,26.3,26.6,27.1,27.5,
        27.8,27.6,27.5,27.9,27.9,27.4,27.2,27.8,26.6,27.5,27.8,27.5,27.5,27.5,27.6,28.0,27.3,27.7,27.4,27.8,27.8,27.3,28.3,27.9,28.0,27.0,27.0,27.4,27.1,27.1,26.8,26.9,
        27.1,27.0,27.4,27.2,27.6,27.8,27.5,26.8,27.4,27.3,28.1,27.8,28.0,27.7,27.1,27.3,27.8,27.2,27.3,27.3,27.4,27.7,27.9,27.1,27.1,28.0,26.9,27.3,27.7,26.2,27.1,27.5,
        28.1,27.9,28.0,28.6,27.4,27.4,27.0,27.1,27.3,27.9,27.0,27.7,27.6,27.4,27.5,27.7,27.5,27.0,26.8,27.2,27.2,27.6,27.0,27.3,27.2,27.3,27.2,27.8,27.9,26.2,27.6,28.3,
        28.2,28.1,28.5,27.3,27.8,27.4,27.3,27.5,27.2,27.9,27.6,29.0,27.6,27.4,27.6,27.5,27.8,27.1,27.1,27.3,27.8,27.3,28.3,27.7,27.5,26.8,27.4,26.7,26.9,27.6,28.8,29.3,
        28.2,27.5,27.5,27.5,27.7,28.3,27.7,27.6,27.5,26.9,27.7,27.5,28.1,27.3,27.1,27.6,28.1,27.9,27.4,27.6,28.1,27.8,28.2,27.9,27.3,27.5,27.9,27.5,26.5,27.0,26.5,26.9,
        27.2,28.4,26.3,28.1,27.4,27.1,27.0,27.4,27.1,27.4,27.6,27.5,27.6,27.4,27.5,27.1,28.4,27.0,27.9,27.8,27.8,27.3,27.2,27.2,27.3,27.6,27.0,26.8,27.4,28.2,27.7,26.7,
        26.7,28.1,27.5,28.1,27.6,28.0,27.5,27.4,26.9,27.5,26.8,27.3,27.4,27.9,27.1,27.3,26.4,27.4,27.9,27.7,27.4,28.0,27.7,26.6,27.6,29.3,27.0,27.6,27.7,25.7,26.5,25.7,
        26.4,26.7,26.2,28.3,27.2,28.2,28.1,28.3,27.5,27.2,27.6,28.2,27.4,27.6,27.8,27.3,28.3,27.7,27.3,27.8,26.9,27.6,27.9,27.7,27.0,27.1,27.9,26.9,27.0,27.0,27.4,26.3,
        27.1,26.6,26.7,27.3,27.8,26.8,27.4,27.5,28.0,27.2,27.7,27.1,27.5,27.3,27.9,27.3,27.4,27.8,27.5,27.0,27.2,27.8,28.1,27.5,28.2,27.8,27.9,27.1,26.1,26.7,27.1,27.2,
        26.9,27.2,27.5,27.9,27.2,27.4,26.2,26.8,25.9,26.7,28.1,27.8,27.7,28.1,27.6,27.7,27.9,27.3,27.3,26.2,27.6,27.2,28.0,27.6,27.4,26.9,26.5,27.3,27.0,27.0,27.1,27.1,
        27.2,27.7,27.7,27.0,27.0,27.3,27.2,27.2,27.8,27.2,27.0,28.3,26.4,27.5,27.7,27.1,27.6,28.0,27.4,27.7,27.3,27.6,27.1,28.0,28.0,27.7,26.8,27.4,27.1,27.1,27.2,26.3,
        28.5,27.9,26.7,27.0,27.2,27.6,27.0,26.8,27.2,27.0,26.6,27.5,27.4,27.0,27.6,26.7,28.7,27.1,27.4,27.6,26.7,27.6,26.9,27.2,26.3,26.3,27.1,26.8,27.1,27.5,27.4,26.6,
        29.3,28.5,28.4,27.8,27.6,27.0,27.2,28.1,27.1,27.3,25.7,26.8,26.7,26.7,27.3,28.6,27.7,27.7,27.0,27.4,27.1,26.9,26.7,26.8,27.2,26.7,26.9,27.1,26.5,27.0,26.2,27.0,
        29.5,28.3,26.9,27.8,27.0,27.2,27.1,27.0,26.7,26.0,27.4,27.5,26.6,27.5,26.9,26.2,27.4,27.1,26.6,26.2,26.4,26.2,26.2,25.1,24.7,26.3,27.1,26.9,27.5,26.7,26.9,27.1,
        29.0,28.0,28.4,28.2,26.6,26.9,27.6,27.2,26.4,26.5,26.1,27.9,26.8,28.1,27.1,25.8,27.5,27.3,26.8,26.0,26.4,27.0,27.2,26.6,26.3,25.9,27.6,27.1,27.1,27.8,28.1,29.3
        """

gridprocessing = GridProcessing()

result = gridprocessing.convert_to_2x2(raw_data=data)
print(result)

stat1 = gridprocessing.grid_statistics(array=result)
print(stat1)

arr = [[1, 2], [3, 4]]

stat2 = gridprocessing.grid_statistics(array=arr)
print(stat2)
