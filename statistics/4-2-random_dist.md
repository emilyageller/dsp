[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 
```
rand = np.random.random(1000)
pmf = thinkstats2.Pmf(rand, label='random')

thinkplot.Pmf(pmf)

cdf = thinkstats2.Cdf(rand)
thinkplot.Cdf(cdf)
```
Yes, the distribution is uniform.
