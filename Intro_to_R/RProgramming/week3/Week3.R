# Week 3 Video Lecture Notes
# lapply: loop over a list and evaluate a function on each element
## (3 arguments: a list x, a function, other arguments)
## make heavy use of anonymous functions
# sapply: same as lapply but try to simplify the result
## If the result is a list where every element is length 1, then a vector is returned
## if the result is a list where every element is a vector of the same length, a matrix is returned
# apply: Apply a function over the margins of an array
## It is most often used to apply a function to the rows or columns of a matrix
## it can be used with general arrays, e.g. taking the average of an array of matrices
## apply(X, MARGIN, FUN, ...) Arguments: X is an array, MARGIN is an interger vector indicating which margins should be retained,
## FUN is a function to be applied to X
# tapply: Apply a function over subsets of a vector 
## tapply(X, INDEX, FUN)  
# mapply: Multivariate version of lapply

mapply(rep, 1:4, 4:1)

# split: an auxiliary function used in conjunction with lapply

x <- list(a =1:5, b=rnorm(10))
lapply(x,mean)
apply(x,2,mean) # Preserves the columns and collapses the rows
apply(x,1,mean) # Preserves the rows and collapes the columns

# rowSums = apply(x, 1, sum)
# rowMeans = apply(x, 1, mean)
# colSums = apply(x, 2, sum)
# colMeans = apply(x, 2, mean)

x <- matrix(rnorm(200), 20, 10)
apply(x, 1, quantile, probs = c(0.25, 0.75)) # calulates the 25th and the 75th percentile for each row

# split(X, f, drop =FALSE, ...) 
## X is a vector, list or data frame; f is a factor or a list of factors; drop indicates whether empty factor levels should be dropped

## Debugging
# message: a generic notification/diagnostic message, execution of the dunction continues
# warning: an indication that something is wrong but not necessarily fatal
# error: an indication that a fatal problem has occured: execution stops
# condition: a generic concept for indicating that something unexpected can occur

invisible(x) # prevents auto-printing

# traceback: prints out the function call stack after an error occurs
# debug: flags a function for "debug" mode which allows you to step through execution of a function one line at a time
# browser: suspends the execution of a function wherever it is called and puts the function in debug mode
# trace: allows you to insert debugging code into a function a specific places
# recover: allows you to modify the error behavior so that you can browse the function call stack
