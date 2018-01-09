[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> 
``` first_wgt_hist = thinkstats2.Hist(firsts.totalwgt_lb, label='first') </br>
other_wgt_hist = thinkstats2.Hist(others.totalwgt_lb, label='other')</br>
thinkplot.Hist(first_wgt_hist)</br>
thinkplot.Config(xlabel='weight (lbs)', ylabel='Count')</br>
thinkplot.Hist(other_wgt_hist)</br>
thinkplot.Config(xlabel='weight (lbs)', ylabel='Count')</br>
firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()</br>
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb) ```</br>
The difference in means is -0.089
