#makefile for C
#compiler and flags
CC = gcc
FLAGS = -fPIC -O2 -fpermissive -Wall -Wextra

all: $(TARGET)

$(TARGET): fastgrep.c
	$(CC) $(FLAGS) -shared -o $(TARGET) fastgrep.c

clean:
	rm -f $(TARGET)
