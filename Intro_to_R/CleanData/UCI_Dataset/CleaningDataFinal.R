## Navigate to correct working directory
setwd(paste(getwd(), "/", "test", sep= ""))
## read the X_test data set
XTest <- read.table("X_test.txt")
## read the y_test data set
yTest <- read.table("y_test.txt")
## read the subject_test data set
subTest <- read.table("subject_test.txt")
## merge the three data frames together into one 
mergedTest <- cbind(subTest, yTest, XTest)