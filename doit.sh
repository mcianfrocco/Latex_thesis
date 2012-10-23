#! /bin/sh

rm *.aux thesis.nl? thesis-blx.bib thesis.bbl thesis.blg thesis.dvi thesis.lof thesis.log thesis.lot thesis.pdf thesis.run.xml thesis.toc

latex thesis && \
bibtex thesis && \
#makeindex thesis.nlo -s nomencl.ist -o thesis.nls
#makeindex thesis
#makeglossaries thesis
latex thesis
bibtex thesis
#makeglossaries thesis
latex thesis
dvipdf thesis.dvi

# with biblatex, it is only necessary to run latex once after bibtex, not twice.
