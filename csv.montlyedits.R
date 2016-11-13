library(ggplot2)
library(zoo)

wsme <- read.csv("women-scientists-monthly-edits.csv", 
                 colClasses=c(month="character", edits="numeric"))

for (i in nrow(wsme))
{
  
#  print(wsme$month)
  
  wsme$theYear <- substr(as.character(wsme$month),1,4)
  wsme$theMonth <- substr(as.character(wsme$month),5,6)
  predate <- paste(as.numeric(wsme$theYear), "-", as.numeric(wsme$theMonth))
  
  #tempy <- c(as.numeric(theMonth),1,as.numeric(theYear))
  #tempy2 <- as.Date(tempy)          
  
  # wsme$date <- as.Date(as.yearmon(paste(as.numeric(wsme$theYear), "-", as.numeric(wsme$theMonth))))
  wsme$date <- as.Date(as.character(as.numeric(wsme$month)), "%Y%m%d%h%m%s")
  as.Date(as.character(as.numeric(wsme$month)), "%Y%m%d%h%m%s")
  
  wsme$date <- as.Date(format(wsme$month, scientific=F), format="%Y%m%d")
  
}

qplot(date, data=wsme, geom="histogram", binwidth=1, xlab=theYear)

ggplot(date, data=wsme,  weight = edits, geom="histogram", binwidth=1) 
  + geom_histogram()

ggplot(data=wsme, mapping=aes(x=date, fill=edits, y=edits)) +
 geom_jitter() +
  labs(x="Year and Month ", y="Edits")  +
  geom_smooth(aes(colour=date)) +
  ggtitle("Sean's Plot")

ggplot(data=wsme, mapping=aes(x=date, fill=edits, y=edits)) +
  geom_line(show.legend = TRUE) +
  labs(x="Year and Month ", y="Edits")  +
  geom_smooth(aes(colour=date)) +
  ggtitle("Sean's Plot") +
  scale_y_sqrt() +
  geom_jitter() +
  geom_text(stat=date)


