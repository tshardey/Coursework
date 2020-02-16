pollutantmean <- function(directory, pollutant, id = 1:332){
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'pollutant' is a character vector of length 1 indicating
  ## the name of the pollutant for which we will calculate the
  ## mean; either "sulfate" or "nitrate".
  
  ## 'id' is an integer vector indicating the monitor ID numbers
  ## to be used
  
  ## Return the mean of the pollutant across all monitors list
  ## in the 'id' vector (ignoring NA values)
  ## NOTE: Do not round the result!
  
  ## Sets present working directory to the default
  setwd("~/Documents/Coursera/Rprogram")
  ## Sets present working directory to the specified directory
  setwd(paste(getwd(),"/",directory,sep=""))
  ## Finds all the ".csv" files in the current folder
  temp <- as.character(list.files(pattern="*.csv"))
  ## Initializes a vector to hold the pollutant data
  meanVector <- c()
  ## Finds the relevent files in the specdata folder
  for(i in id) {
    current_file <- read.csv(temp[i], header=T, sep=",")
    head(current_file)
    pollutant
    naRemoved <- current_file[!is.na(current_file[, pollutant]), pollutant]
    meanVector <- c(meanVector, naRemoved)
  }
  ## Calculates the mean value
  result <- mean(meanVector)
  return(round(result, 3)) 
}
