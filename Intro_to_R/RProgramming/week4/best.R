best <- function(state, outcome) {
  ## Read outcome data
  outcomeTable <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  ## Check that state and outcome are valid
  ## Return hospital name in that state with lowest 30-day death rate
  # Making a new data frame that only contains the desired data
  md   <- as.data.frame(cbind(outcomeTable[, 2],   # hospital
                              outcomeTable[, 7],   # state
                              outcomeTable[, 11],  # heart attack
                              outcomeTable[, 17],  # heart failure
                              outcomeTable[, 23]), # pneumonia
                        stringsAsFactors = FALSE)
  # naming the columns of the new data frame
  colnames(md) <- c("hospital", "state", "heart attack", "heart failure", "pneumonia")
  
  # creating a unique list of all the States in the study
  unqState <- unique(outcomeTable$State)
  # The three possible types of death in the study
  possDeath <- c("heart attack", "heart failure", "pneumonia")
  
  # Checking the validity of the entered state
  if(!state %in% unqState){stop("Invalid State")}
  # Checking the validity of the entered outcome
  else if(!outcome %in% possDeath){stop("Invalid Outcome")}
  # If both the State and out come are valid then the else will execute
  else{
    # Looking through all rows and the State column to see which match the entered state
    si <- which(md[, "state"] == state)
    ts <- md[si, ]    # extracting data for the called state
    # Coecing to numerics the data for the called outcome
    oi <- as.numeric(ts[, eval(outcome)])
    # Calculating the min value, with removal of NAs
    min_val <- min(oi, na.rm = TRUE)
    # Getting the name of the hospital that equals the minimum value 
    result  <- ts[, "hospital"][which(oi == min_val)]
    # Ordering the results by alphabetical order in case of a tie.
    output  <- result[order(result)]
  }
return(output)

}