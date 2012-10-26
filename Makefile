.PHONY: clean

RST2PDF=rst2pdf
OUTDIR=out
FLAGS=-b1 -s assets/styles/slides.style

all:
	mkdir -p $(OUTDIR)
	$(RST2PDF) 00-setup.rst        $(FLAGS) -o $(OUTDIR)/00-setup.pdf
	$(RST2PDF) 01-introduction.rst $(FLAGS) -o $(OUTDIR)/01-introduction.pdf
	$(RST2PDF) 02-mvc.rst          $(FLAGS) -o $(OUTDIR)/02-mvc.pdf
	$(RST2PDF) 03-yourfirstapp.rst $(FLAGS) -o $(OUTDIR)/03-yourfirstapp.pdf

clean:
	rm -rf out/
