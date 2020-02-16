# makeCache Matrix creates a special "matrix," which is really a list containing a function to
# 1) set the value of the matrix
# 2) get the value of the matrix
# 3) set the value of the inverse
# 4) get the value of the inverse

makeCacheMatrix <- function(x = matrix()) {
  inverse <- NULL # initializes the inverse matrix value
  
  # sets the value of the matrix
  set <- function(y) {
    x <<- y
    inverse <<- NULL
  }
  
  # gets the value of the matrix
  get <- function() x
  
  # sets the value of the matrix
  setInverse <- function(inverseInput) inverse <<- inverseInput
  
  # gets the value of the matrix
  getInverse <- function() inverse
  
  # returns a list of the created functions
  list(set = set, get = get,
       setInverse = setInverse,
       getInverse = getInverse)
}

# casheSolve calculates the inverse of special vector created with makeCacheMatrix.
# It first checks to see if the inverse has already been calculated.
# If so, it gets the inverse from the cache and skips the computation.
# Otherwise, it calculates the inverse of the matrix and sets the value of the mean in the cache.  

cacheSolve <- function(x, ...) {
  # Checking to see if the inverse is already cached.
  inverse <- x$getInverse()
  # If it is, the iverse is taken directly from the cache.
  if(!is.null(inverse)) {
    message("Getting cached data")
    return(inverse)
  }
  # If not, the matrix if fetched
  data <- x$get()
  # The inverse of the matrix is calculated
  inverse <- solve(data, ...)
  # The inverse of the matrix is cached 
  x$setInverse(inverse)
  # result is returned
  inverse
}
