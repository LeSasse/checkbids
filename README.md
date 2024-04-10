# checkbids
Wrapper to run the [bids validator](https://pypi.org/project/bids-validator/)
from command line and validate each file in a root directory.

# Install

```bash
pip install git+https://github.com/LeSasse/checkbids.git
```

# Run

Run the bids validator from command line. It takes one argument: The root
directory of a bids dataset. It then traverses all files in that dataset
and checks if they are valid BIDS files.

```bash
checkbids path/to/BIDS_dataset
```
