# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: job.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tjob.proto\"j\n\rJobSubmission\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x17\n\ntimeout_ms\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x15\n\rworkflow_type\x18\x03 \x01(\t\x12\x0c\n\x04\x65sdl\x18\x04 \x01(\x0c\x42\r\n\x0b_timeout_ms\"z\n\tJobResult\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12*\n\x0bresult_type\x18\x02 \x01(\x0e\x32\x15.JobResult.ResultType\"3\n\nResultType\x12\r\n\tSUCCEEDED\x10\x00\x12\x0b\n\x07TIMEOUT\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"3\n\x11JobProgressUpdate\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x10\n\x08progress\x18\x02 \x01(\x01\"e\n\x0fJobStatusUpdate\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"D\n\tJobStatus\x12\x0e\n\nREGISTERED\x10\x00\x12\x0c\n\x08\x45NQUEUED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0c\n\x08\x46INISHED\x10\x03\"\x19\n\tJobCancel\x12\x0c\n\x04uuid\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'job_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_JOBSUBMISSION']._serialized_start=13
  _globals['_JOBSUBMISSION']._serialized_end=119
  _globals['_JOBRESULT']._serialized_start=121
  _globals['_JOBRESULT']._serialized_end=243
  _globals['_JOBRESULT_RESULTTYPE']._serialized_start=192
  _globals['_JOBRESULT_RESULTTYPE']._serialized_end=243
  _globals['_JOBPROGRESSUPDATE']._serialized_start=245
  _globals['_JOBPROGRESSUPDATE']._serialized_end=296
  _globals['_JOBSTATUSUPDATE']._serialized_start=298
  _globals['_JOBSTATUSUPDATE']._serialized_end=399
  _globals['_JOBSTATUSUPDATE_JOBSTATUS']._serialized_start=331
  _globals['_JOBSTATUSUPDATE_JOBSTATUS']._serialized_end=399
  _globals['_JOBCANCEL']._serialized_start=401
  _globals['_JOBCANCEL']._serialized_end=426
# @@protoc_insertion_point(module_scope)
