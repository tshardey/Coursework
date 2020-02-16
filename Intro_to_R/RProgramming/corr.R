corr <- function(directory, threshold = 0) {
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'threshold' is a numeric vector of length 1 indicating the
  ## number of completzely observed observations (on all
  ## variables) required to compute the correlation between
  ## nitrate and sulfate; the default is 0
  
  ## Return a numeric vector of correlations
  ## NOTE: Do not round the result!
  
  setwd("~/Documents/Coursera/Rprogram")
  ## Sets present working directory to the specified directory
  setwd(paste(getwd(),"/",directory,sep=""))
  # get the complete table
  complete_table <- complete("specdata", 1:332)
  nobs <- complete_table$nobs
  # find the valid ids
  ids <- complete_table$id[nobs > threshold]
  ## Finds all the ".csv" files in the current folder
  temp <- as.character(list.files(pattern="*.csv"))
  ## Gets the length of the ID vector
  lenID <- length(ids)
  corrVector <- rep(0, lenID)
  ## Finds the relevent files in the specdata folder
  k <- 1
  for(i in ids) {
    current_file <- read.csv(temp[i], header=T, sep=",")
    corrVector[k] <- cor(current_file$sulfate, current_file$nitrate, use="complete.obs")
    k <- k + 1
  }
  result <- corrVector
  return(result)
}

# tests
cr <- corr("specdata", 150)
head(cr)
cr <- corr("specdata", 400)
head(cr)
cr <- corr("specdata", 5000)
summary(cr)
