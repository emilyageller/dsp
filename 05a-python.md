# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

**How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?**

Similarities:
- They are both sequences of values, which can be of any type.
- They are both indexed by integers

Differences:
- tuples are immutable, while lists are mutable


The fact that tuples are immutable allow them to be used as keys in dictionaries. 

---

### Q2. Lists &amp; Sets

**How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?**

Similarities:
- both are types that can contain other types

Differences:
- sets can't have duplicate values, while lists can
- sets are unordered


Performance is much better when looking for an element in sets than in lists. This is because a hash lookup is used for sets.

Lists are nice to use when order is important, while sets are nice when you don't want duplicates and you don't care about order.

Example:
- list:   [1,2,3]
- set:    {1, 2, 3}

---

### Q3. Lambda Function

**Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.**

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

**Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.**

List comprehensions can be used instead of for loops when manipulating lists. Rather than writing a for loop, a list comprehension can be written on one line inside `[` and `]`.  They include the elements of the list and the `for` condition.  **You can't put a `print()` inside of a list comprehension, so they shouldn't be used unless the operation is relatively simple**

A `map` is an operation that "maps" a function onto each of the elements in a sequence. (Eg `capitalize_all()`)
A `filter` is an operation that selects some of the elements from a list and returns a sublist. (Eg `only_upper()`)
A `reduce` is an operation that combines a sequence of elements into a single value. (Eg. `sum()`)

Examples:
Problem: capitalize all elements in a list `t`.
1. List comprehension:
      `[s.capitalize() for s in t]`
2. `Map` and `Filter`
      ``res = []
        for s in t: # this is the filter
          res.append(s.capitalize()) # capitalize is the map`` 
3. Set comprehension:
  `{s.capitalize() for s in t}`
4. Dict comprehension:
  `{s: s.capitalize() for s in t}`
        

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





