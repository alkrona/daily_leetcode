#! /bin/bash

#!/bin/bash

for date in "$@"
do
    mkdir "$date"
    cd "$date"

    touch "$date.py"

    # Using a heredoc for test.py contents, ensuring Python syntax
    cat > test.py << EOF
#!/usr/bin/env python3

# Import libraries for Python
import numpy as np
import matplotlib.pyplot as plt

# Your Python code for test.py starts here

# Example: Generate some data and plot a simple graph
x = np.linspace(0, 5, 11)
y = x ** 2

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Square function plot for $date")
plt.show()
EOF

    touch "__init__.py"

    # Inform about Python-specific content
    echo "Created the files, including test.py with Python code (NumPy and Matplotlib imported)."
done