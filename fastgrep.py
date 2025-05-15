import ctypes
import sys
import os

#loading shared lib
lib_path = os.path.join(os.path.dirname(__file__), "c_lib", "fastgrep.so")
lib = ctypes.CDLL(lib_path)

lib.searchFile.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.searchFile.restype = ctypes.c_int

def search(filename: str, pattern: str) -> int:
    """Search filename for pattern, ret 0 on success"""
    return lib.search_file(filename.encode('utf-8'), pattern.encode('utf-8'))

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <filepath> <filename> <pattern>")
        print(f"For example: {sys.argv[0]} data example.txt world")
        sys.exit(1)
    
    hit = search(f"{sys.argv[1]}/{sys.argv[2]}", sys.argv[3])
    if hit:
        print("Check file, filename, or path", file=sys.stderr)
        sys.exit(hit)

if __name__ == "__main__":
    main()
