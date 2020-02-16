add2 <- function(x,y){
  x+y
}

above10 <- function(x) {
  use <- x >10
  x[use]
}

above <- function(x,n=10 ) {
  ##default value if not specified
  use <- x > n
  x[use]
}

columnMean <-function(y, removeNA = TRUE){
  nc <- ncol(y)
  means <- numeric(nc)
  for(i in 1:nc){
    means[i] <- mean(y[,i], na.rm = removeNA)
  }
  means ## last value of the function is the return value
}

cube <- function(x,n){
  x^3
}

x <- 1:10
if(x>5){
  x<-0
}

h <- function(x, y = NULL, d = 3L) {
  z <- cbind(x, d)
  if(!is.null(y))
    z <- z + y
  else
    z <- z + f
  g <- x + y / z
  if(d == 3L)
    return(g)
  g <- g + 10
  g
}
