#!/usr/bin/env Rscript






print("R script: converting .sav to .csv")

library(foreign)

write.table(read.spss("C:/Users/Ziemek/Documents/GitHub/Analize-DataBases/Lab2/CommanFiles/pew.sav"), file="pawConverted.csv", quote = TRUE, sep = '`')

