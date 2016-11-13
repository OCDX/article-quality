library(ggplot2)
wsme <- read.csv("women-scientists-monthly-edits.csv", 
                 colClasses=c(month="character", edits="character"))

for (i in nrow(wsme))
{
  
#  print(wsme$month)
  
  wsme$theYear <- substr(as.character(wsme$month),1,4)
  wsme$theMonth <- substr(as.character(wsme$month),5,6)
  
}

qplot(edits, data=wsme, geom="histogram")
