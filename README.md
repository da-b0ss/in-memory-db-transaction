# in-memory-db-transaction

# In-Memory Database with Transaction Support

This project implements an in-memory key-value database with transaction support as specified in the assignment. The implementation is done in Python and provides all the required functionality:

- begin_transaction()
- put(key, value)
- get(key)
- commit()
- rollback()

## Features

- Keys are strings and values are integers
- put(key, val) creates a new key or updates an existing one
- get(key) returns the value associated with the key or None if it doesn't exist
- Transactions provide "all or nothing" updates
- Changes made within a transaction are only visible after commit
- Rollback discards all changes made within a transaction

## Setup and Running

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/in-memory-db.git
cd in-memory-db
```

2. No additional dependencies are required as the implementation uses only Python standard libraries.

### Running the Tests

To run the tests, execute:
```
python test_in_memory_db.py
```

This will run a series of tests to verify the implementation meets all the requirements.

### Usage Example

```python
from in_memory_db import InMemoryDB

# Create a new database instance
db = InMemoryDB()

# Should return None because A doesn't exist yet
print(db.get("A"))  # None

try:
    # Should throw an error because transaction is not in progress
    db.put("A", 5)
except Exception as e:
    print(f"Error: {e}")

# Start a transaction
db.begin_transaction()

# Set key A's value to 5
db.put("A", 5)

# Should return None because the transaction is not committed yet
print(db.get("A"))  # None

# Update A's value to 6
db.put("A", 6)

# Commit the transaction
db.commit()

# Now it should return 6
print(db.get("A"))  # 6

# Start another transaction
db.begin_transaction()

# Set key B's value to 10
db.put("B", 10)

# Rollback the transaction
db.rollback()

# Should return None because the transaction was rolled back
print(db.get("B"))  # None
```

## Assignment Improvement Suggestions

For this assignment to become an "official" assignment in the future, I would suggest the following improvements:

1. Add explicit requirements for error handling and custom exceptions for better clarity on what should happen in edge cases.

2. Include additional test cases that cover concurrent transactions or nested transactions to expand the challenge (though the current requirement specifies only one transaction at a time).

3. Consider adding a requirement for a method to list all keys or values to make testing and verification easier.

4. Clarify the return type of get() when a key doesn't exist - the instructions say "return null" but in many languages null and None are different concepts.

5. Add performance benchmarks or constraints to challenge students to optimize their solutions.