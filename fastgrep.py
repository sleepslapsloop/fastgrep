import ctypes
import sys
import os

#loading shared lib
lib_path = os.path.join(os.path.dirname(__file__), "c_lib", "fastgrep.so")
lib = ctypes.CDLL(lib_path)

lib.search_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.search_file.restype = ctypes.c_int

def search(filename: str, pattern: str) -> int:
    """Search filename for pattern, ret 0 on success"""
    return lib.search_file(filename.encode('utf-8'), pattern.encode('utf-8'))

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <filename> <pattern>")
        sys.exit(1)

    hit = search(sys.argv[1], sys.argv[2])
    if hit:
        print("Check file, filename, or path", file=sys.stderr)
        sys.exit(hit)

if __name__ == "__main__":
    main()
