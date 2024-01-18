# Python Import Mechanism

If you are developing python package and don't want to release a pypi version of it yet, then you might be heavily relying on local functions or helper functions for your scripts.

You might often find errors like: `No module named <xxxx>` when trying to import those functions, even when namings of packages are right and the paths to them.

---

This repo stores a minimalist example that shows why adding an empty "__init__.py" into your desired directory that contains functions makes them available in other scripts as imports.

In order to do this, simply create a similar directory structure like below:

```bash
# All functions from FUN_1.py and FUN_n.py is available to import
------ GOOD_DIR/
      |______ __init__.py
      |______ FUN_1.py
      |______ FUN_n.py

# No functions here could be imported, because the __init__.py is missing
------ BAD_DIR/
      |_______ FUN_2.py
      |_______ FUN_m.py

# Then from this script, we could import functions from GOOD_DIR but NOT from BAD_DIR
# from GOOD_DIR.FUN_1 import fun_x, fun_y, fun_z 
# from GOOD_DIR.FUN_n import fun_a, fun_b, fun_c
______ main.py 
```

A similar example could be at the main [run.py](run.py) script located in the root directory of this repo

Author: Tony Liang
