import zlib, base64, codecs, lzma
def encodatolol(wbh:str):
    wbh=f'3+{base64.b85encode(codecs.encode(base64.b16encode(lzma.compress(wbh.encode())).decode(), "rot13").encode()).decode()}'
    return wbh
