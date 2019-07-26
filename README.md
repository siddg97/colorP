# colorP
<br><br>
This package is a small and simple utility for printing colored strings on consoles. `colorP` supports 9 diffeerent formatting styles and several foreground and background colors!
<br><br>
You can install it ~~Lorem ipsum dolor sit amet, consectetur iusmod~~.
<br><br>

## Usage:
The library currently has 2 methods :-
#### `pPrint(args,text,br=?)`:
- `args`: is a dictionary object, which needs atleast one of `s`,`fg` or `bg` defined with the corresponding values as strings.
```python
args = {'s':'bold','fg':'red','bg':'white'}
```
- `text`: is the string to be printed with the given styling
- `br`: __[OPTIONAL ARGUMENT: default value= `True`]__, can set it to `False` if you need no linebreak after ouput. 
<br><br>
#### `Eg()`:
- prints out examples of a few colors and styles for user visualization.
