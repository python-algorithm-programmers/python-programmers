import pickle
import binascii

# 16진수 문자열
hex_str = "0x8004952A000000000000008C086461746574696D65948C086461746574696D65949394430A07E8071F140B2409723E94859452942E"

# "0x"를 제거하고 바이트로 변환
byte_data = binascii.unhexlify(hex_str[2:])

# 역직렬화
unpickled_data = pickle.loads(byte_data)

print(unpickled_data)
