[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> 
```
resp = nsfg.ReadFemResp()
resp.numkdhh.value_counts()

numkdhh_pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')
thinkplot.Pmf(numkdhh_pmf)
thinkplot.Config(xlabel='numkdhh', ylabel='Pmf')

numkdhh_biased_pmf = BiasPmf(numkdhh_pmf, label='observed')
thinkplot.Pmf(numkdhh_biased_pmf)
thinkplot.Config(xlabel='numkdhh_biased', ylabel = 'pmf')

numkdhh_pmf.Mean()
numkdhh_biased_pmf.Mean()
```
