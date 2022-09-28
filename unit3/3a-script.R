sales <- df$Sales
sales_ts <- ts(sales, frequency = 12, start=c(2010, 2, 5))

tsdM <- decompose(sales_ts, "multiplicative")
plot(tsdM)

h <- HoltWinters(sales_ts)
h
plot(h)

m <- hw(sales_ts, alpha=0.2859494, beta=0.01948335, gamma=0.1002303, h=100, seasonal = "multiplicative")
plot(m)