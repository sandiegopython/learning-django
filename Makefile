.PHONY: clean

all:
	mkdir -p out
	rst2pdf 01-introduction.rst -b1 -s assets/styles/slides.style -o out/01-introduction.pdf

clean:
	rm -rf out/
