# from csv import reader
# from datetime import datetime
# from domain.aggregated_data import AggregatedData
#
# class FileDatasource:
#     def __init__(self, accelerometer_filename: str, gps_filename: str) -> None:
#         pass
#
#     def read(self) -> AggregatedData:
#     """Метод повертає дані отримані з датчиків"""
#
#     def startReading(self, *args, **kwargs):
#     """Метод повинен викликатись перед початком читання даних"""
#
#     def stopReading(self, *args, **kwargs):
#     """Метод повинен викликатись для закінчення читання даних"""

from csv import reader
from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.aggregated_data import AggregatedData
import config

class FileDatasource:
    def __init__(
        self,
        accelerometer_filename: str,
        gps_filename: str,
    ) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename

    def read(self) -> AggregatedData:
        """The method returns data received from the sensors"""
        accelerometer_data = self._read_accelerometer_data()
        gps_data = self._read_gps_data()
        return AggregatedData(
            accelerometer_data,
            gps_data,
            datetime.now(),
            config.USER_ID,
        )

    def _read_accelerometer_data(self) -> Accelerometer:
        with open(self.accelerometer_filename, 'r') as file:
            csv_reader = reader(file)
            next(csv_reader)  # Skip header if present
            row = next(csv_reader)
            x, y, z = map(int, row)
            return Accelerometer(x, y, z)

    def _read_gps_data(self) -> Gps:
        with open(self.gps_filename, 'r') as file:
            csv_reader = reader(file)
            next(csv_reader)  # Skip header if present
            row = next(csv_reader)
            longitude, latitude = map(float, row)
            return Gps(longitude, latitude)

    def startReading(self, *args, **kwargs):
        """The method must be called before reading data"""
        pass

    def stopReading(self, *args, **kwargs):
        """The method should be called to stop reading data"""
        pass
