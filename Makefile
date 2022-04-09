CLEAN_LIST := foo.o libfoo.so

# 64 bit - - - - - - - - - - - - - - - 
.PHONY: all
all: libfoo.so

foo.o: foo.c foo.h
	gcc -fPIC -c foo.c -o foo.o

libfoo.so: foo.o
	gcc foo.o -shared -o libfoo.so
# - - - - - - - - - - - - - - - - - - -


# 32 bit - - - - - - - - - - - - - - - 
.PHONY: 32bit
32bit: libfoo_32.so

foo_32.o: foo.c foo.h
	gcc -m32 -fPIC -c foo.c -o foo.o

libfoo_32.so: foo_32.o
	gcc -m32 foo.o -shared -o libfoo.so
# - - - - - - - - - - - - - - - - - - -


# clean - - - - - - - - - - - - - - - - 
.PHONY: clean
clean:
	rm -f $(CLEAN_LIST)
# - - - - - - - - - - - - - - - - - - -