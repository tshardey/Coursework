## Else - If
if(x>3){
  y<-10
}else{
  y<-0
}
y <- if(x>3){
  10
}else{
  0
}

## For loops
x<-c("a","b","c","d")
for(i in 1:4){
  print(x[i])
}
for(i in seq_along(x)){
  print(x[i])
}
for(letter in x){
  print(letter)
}
for(i in 1:4) print(x[i]) ## only valid for a single expression

## While loops

count <- 0 
while(count<10){
  print(count)
  count<- count+1
}

while(z >=3 && z<=10){
  print(z)
  coin<-rbinom(1,1,0.5)
  if(coin==1){
    z<-z+1
  }else{
    z<-z-1
  }
}

##REPEAT
## Executes and infite loop, the only way to exit is to call break

x0<-1
tol <- 1e-08
repeat{
  x<- computeEstimate()
  if(abs(x1-x0)<tol){
    break
  }else{
    x0<-x1
  }
}##requires an algorithm that is guarenteed to converge, may take a long time

##NEXT
## Used to skip an iteration
for(i in 1:100){
  if(i<=20){
    next
  }else{
    ## do something here
  }
}
##return signals a function should exit and returns a given value

## FUNCTIONS
## Arguments of function can be specified by position or by name
## Arguments can be partially matched
## 1. exact match
## 2. partial match
## 3. positional match
## Arguments to functions are evaluatied "lazily", only as needed
## "..." used to indicate a variable number of arguments that are usuall passed on to other functions

myplot<- function(x,y, type="1",...){
  plot(x,y,tupe=tepe,...)
}
## Lexical Scoping
## the values of free variables are searched for in the environment in which the function was defined
## Can define global variables 
## you can have functions defined inside other functions
# Example
make.power <- function(n){
  pow<- function(x){
    x^n
  }
  pow
}
cube<- make.power(3)
square <- make.power(2)
ls(environment(func))
get(arg, environment(func))

## Dates and Times
## Dates are represented by the "date" class
## Times are represented by the "POSIXct" (times are represented as very large integers) or the "POSIXlt" (stores a bunch of other useful information)
## weekdays, months, quarters functions
# Ex.
x<- as.Date("1970-01-01")
x<- Sys.time()
p <- as.POSIXlt(x)
names(unclass(p))
## in case dates are written in a different format
x <-striptime(datestring,"%B %d, %Y")
## Mathematical operations on dates and times (+ or -), as well as comparisons
