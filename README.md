# ym
Data type that handles year and month values.

[![Build Status](https://travis-ci.org/hoto17296/python-ym.svg)](https://travis-ci.org/hoto17296/python-ym)

## Usage

### Import
```
from ym import ym
```

### Initialize
from year, month

``` python
ym(2020, 4)  #=> ym(2020, 4)
```

from current month

``` python
ym.current()  #=> ym(2020, 7)
```

from string

``` python
ym.parse("2020-04")  #=> ym(2020, 4)
```

from date or datetime object

``` python
from datetime import date

ym.parse(date.today())  #=> ym(2020, 7)
```

### Get year, month
``` python
current = ym.current()  #=> ym(2020, 7)
current.y  #=> 2020
current.m  #=> 7
```

### Add, Sub
``` python
ym(2020, 4) + 10  #=> ym(2021, 2)
ym(2020, 4) - 10  #=> ym(2019, 6)
```

``` python
ym(2020, 7) - ym(2020, 4)  #=> 3
```


### Compare
``` python
ym(2020, 7) < ym(2020, 4)  #=> False
ym(2020, 7) > ym(2020, 4)  #=> True
ym(2020, 7) == ym(2020, 4)  #=> False
```

### Range
``` python
ym(2020, 4).to(2020, 7)  #=> [ym(2020, 4), ym(2020, 5), ym(2020, 6)]
```

``` python
current = ym.current()  #=> ym(2020, 7)
current.to(current + 6)  #=> [ym(2020, 7), ym(2020, 8), ym(2020, 9), ym(2020, 10), ym(2020, 11), ym(2020, 12)]
```
