library(devtools)
install_github("McTavishLab/rotl")
library(rotl)

tol_induced_subtree(c(292466, 267845, 316878, 102710), get_citations = TRUE)
tol_induced_subtree(c(292466, 267845, 316878, 102710), file = "test", get_citations = TRUE)
