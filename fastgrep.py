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
    return lib.searchFile(filename.encode('utf-8'), pattern.encode('utf-8'))

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <filepath> <filename> <pattern>")
        print(f"For example: {sys.argv[0]} data example.txt world")
        sys.exit(1)

    if len(sys.argv) < 3:
        print("Fatal Error: Insufficient Arguments")
        print("Terminating with exit code: 1")
        sys.exit(1)
    elif len(sys.argv) == 3:
        hit = search(f"data/{sys.argv[1]}", sys.argv[2])
    elif len(sys.argv) == 5 and sys.argv[2] == "-p":
        hit = search(f"{sys.argv[3]}/{sys.argv[1]}", sys.argv[4])
    else:
        print("Fatal Error: wrong order of arguments or excess or insufficient arguments")
    
    if hit:
        print("Check file, filename, or path", file=sys.stderr)
        sys.exit(hit)

if __name__ == "__main__":
    main()
