from jarvis_sdk.ingest import IngestClient
from jarvis_sdk.indykite.ingest.v1beta1 import model_pb2
from jarvis_sdk.indykite.objects.v1beta1 import struct_pb2

""" Test Ingest Client """

client = IngestClient()

config_id = "gid:AAAAFBtaAlxjDE8GuIWAPEFoSPs"
data = {
    "key1": struct_pb2.Value(string_value="val1"),
    "key2": struct_pb2.Value(string_value="val2")
}
record = model_pb2.Record(id="1", external_id="external", data=data)

response_iterator = client.stream_records(config_id, [record])

client.read_stream_response(response_iterator)
