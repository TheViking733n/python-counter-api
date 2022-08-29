# python-counter-api
This is a simple light weight python wrapper for the free counter api - https://countapi.xyz/



```python
from python_counter_api import CounterApi
```


```python
myvar = CounterApi("myvar", "mysite.com")      # Declaring the variable
```


```python
print(myvar)            # None value means that this variable has not been used
```

    myvar: None
    


```python
myvar.create()          # Creating the variable in the server database, and initialising with zero
```




    0




```python
myvar.hit()             # Incrementing the value by 1 and return new value
```




    1




```python
myvar.increment(5)      # Incrementing the value by 5  and return new value
```




    6




```python
myvar.reset(-2)         # Resetting the value of variable to -2, this functions returns the previous value
```




    6




```python
myvar.value()           # Fetching current value
```




    -2




```python
print(myvar)            # Same as myvar.value(), instead of returning it prints the value
```

    myvar: -2
    


```python

```
