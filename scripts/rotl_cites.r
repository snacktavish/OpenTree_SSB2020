library(devtools)
install_github("McTavishLab/rotl")
# you can also install the dev versio of the package from a branch with:
# devtools::install_github("McTavishLab/rotl", ref = "citations_doc")
library(rotl)

tol_induced_subtree(c(292466, 267845, 316878, 102710), write_citations = TRUE)
tol_induced_subtree(c(292466, 267845, 316878, 102710), file = "test", write_citations = TRUE)
