#makefile for C
#compiler and flags
#CC = gcc
#FLAGS = -fPIC -O2 -Wall -Wextra

all: fastgrep.so

fastgrep.o: fastgrep.c
	@gcc fastgrep.c -O2 -fPIC -Wextra -c fastgrep.o

fastgrep.so: fastgrep.o
	@gcc fastgrep.o -shared -o fastgrep.so
	@rm -rf fastgrep.o

clean: fastgrep.so
	@rm -rf fastgrep.so
