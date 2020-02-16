complete <- function(directory, id = 1:332){
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'id' is an integer vector indicating the monitor ID numbers
  ## to be used
  
  ## Return a data frame of the form:
  ## id nobs
  ## 1  117
  ## 2  1041
  ## ...
  ## where 'id' is the monitor ID number and 'nobs' is the
  ## number of complete cases
  
  setwd("~/Documents/Coursera/Rprogram")
  ## Sets present working directory to the specified directory
  setwd(paste(getwd(),"/",directory,sep=""))
  ## Finds all the ".csv" files in the current folder
  temp <- as.character(list.files(pattern="*.csv"))
  ## Gets the length of the ID vector
  lenID <- length(id)
  completeData <- rep(0, lenID)
  ## Finds the relevent files in the specdata folder
  k <- 1
  for(i in id) {
    current_file <- read.csv(temp[i], header=T, sep=",")
    completeData[k] <- sum(complete.cases(current_file))
    k <- k + 1
  }
  result <- data.frame(id = id, nobs = completeData)
  return(result)
}
# tests
complete("specdata", 1)
complete("specdata", c(2, 4, 8, 10, 12))
complete("specdata", 30:25)
complete("specdata", 3)