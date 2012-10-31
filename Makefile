.PHONY: clean
.PHONY: all

RST2PDF=rst2pdf
OUTDIR=out
FLAGS=-b1 -s assets/styles/slides.style

SOURCES=$(wildcard [0-9]*.rst)
OBJECTS=$(SOURCES:%.rst=$(OUTDIR)/%.pdf)

all: $(OUTDIR) $(OBJECTS)
	@echo "Done"

$(OUTDIR)/%.pdf: %.rst 
	$(RST2PDF) $< $(FLAGS) -o $@

$(OUTDIR):
	mkdir $@


clean:
	rm -rf out/
