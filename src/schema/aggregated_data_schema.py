
from accelerometer_schema import AccelerometerSchema
from gps_schema import GpsSchema
from ..domain.aggregated_data import AggregatedData
from marshmallow import Schema, fields
class AggregatedDataSchema(Schema):
    accelerometer = fields.Nested(AccelerometerSchema)
    gps = fields.Nested(GpsSchema)
    time = fields.DateTime('iso')