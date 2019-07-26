# colorP

This package is a small and simple utility for printing colored strings on consoles. `colorP` supports 9 different formatting styles and several foreground and background colors!

You can install it by issuing the following command on a UNIX terminal:<br>

```bash
sudo pip install -i colorp
```

## Usage:

Methods :-

#### `pPrint(args,text,br=?)`:

- `args`: is a dictionary object, which needs atleast one of `s`,`fg` or `bg` defined with the corresponding values as strings.

```python
args = {'s':'bold','fg':'red','bg':'white'}
```
- `text`: is the string to be printed with the given styling
- `br`: __[OPTIONAL ARGUMENT: default value= `True`]__, can set it to `False` if you need no linebreak after ouput. 

#### `Eg()`:
- prints out examples of a few colors and styles for user visualization.

### Styling and Formatting:
- The `args` object decides how the text will be formatted. Each key in `args` can be one of certain pre-defined values. They are listed below:
- **`'s'`**: Text style

| __Value__ | __Description__ |
| --- | --- |
| `'plain'` | Formats the text as plain text |
| `'bold'` | Bolds the text |
| `'dim'` | Dims the text |
| `'italic'` | Italicizes the text |
| `'underline'` | Underlines the text |
| `'blink'` | Blinks the text repeatedly |
| `'reverse'` | Swaps foreground and background values |
| `'hidden'` | Hides the text on display |
| `'striked'` | Strikes off the desired text |

- **`'fg'`**: Font color

| __Value__ |
| --- |
| `'black'` |
| `'red'`   |
| `'green'` |
| `'yellow'` |
| `'blue'` |
| `'magenta'` |
| `'cyan'` |
| `'lightgray'` |
| `'darkgray'` |
| `lightred'` |
| `'lightgreen'` |
| `'lightyellow'` |
| `'lightblue'` |
| `'lightmagenta'` |
| `'lightcyan'` |
| `'white'` |
| `'default'` |


- **`'bg'`**: Background color


| __Value__ |
| --- |
| `'black'` |
| `'red'`   |
| `'green'` |
| `'yellow'` |
| `'blue'` |
| `'magenta'` |
| `'cyan'` |
| `'lightgray'` |
| `'darkgray'` |
| `lightred'` |
| `'lightgreen'` |
| `'lightyellow'` |
| `'lightblue'` |
| `'lightmagenta'` |
| `'lightcyan'` |
| `'white'` |
| `'default'` |

##### NOTE:
- `'bg'` has the same possible values as `'fg'`.