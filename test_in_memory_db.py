# Test script for InMemoryDB
from in_memory_db import InMemoryDB

def run_tests():
    print("Testing InMemoryDB implementation...\n")
    
    # Create a new instance of InMemoryDB
    db = InMemoryDB()
    
    # Test 1: Get a non-existent key
    print("Test 1: Get a non-existent key")
    result = db.get("A")
    print(f"get('A') => {result}")
    assert result is None
    print("Test passed\n")
    
    # Test 2: Put without an active transaction
    print("Test 2: Put without an active transaction")
    try:
        db.put("A", 5)
        print("Test failed: Expected an exception")
    except Exception as e:
        print(f"Expected error: {e}")
        print(" Test passed\n")
    
    # Test 3: Begin a transaction and put a key-value pair
    print("Test 3: Begin a transaction and put a key-value pair")
    db.begin_transaction()
    db.put("A", 5)
    print(" Test passed\n")
    
    # Test 4: Key should not be visible until committed
    print("Test 4: Key should not be visible until committed")
    result = db.get("A")
    print(f"get('A') => {result}")
    assert result is None
    print(" Test passed\n")
    
    # Test 5: Update the value within the transaction
    print("Test 5: Update the value within the transaction")
    db.put("A", 6)
    result = db.get("A")
    print(f"get('A') => {result}")
    assert result is None
    print(" Test passed\n")
    
    # Test 6: Commit the transaction
    print("Test 6: Commit the transaction")
    db.commit()
    result = db.get("A")
    print(f"get('A') => {result}")
    assert result == 6
    print(" Test passed\n")
    
    # Test 7: Commit without an active transaction
    print("Test 7: Commit without an active transaction")
    try:
        db.commit()
        print("  Test failed: Expected an exception")
    except Exception as e:
        print(f"Expected error: {e}")
        print(" Test passed\n")
    
    # Test 8: Rollback without an active transaction
    print("Test 8: Rollback without an active transaction")
    try:
        db.rollback()
        print("  Test failed: Expected an exception")
    except Exception as e:
        print(f"Expected error: {e}")
        print(" Test passed\n")
    
    # Test 9: Check for a non-existent key
    print("Test 9: Check for a non-existent key")
    result = db.get("B")
    print(f"get('B') => {result}")
    assert result is None
    print(" Test passed\n")
    
    # Test 10: Test transaction rollback
    print("Test 10: Test transaction rollback")
    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    result = db.get("B")
    print(f"get('B') => {result}")
    assert result is None
    print(" Test passed\n")
    
    # Test 11: Multiple operations in a transaction
    print("Test 11: Multiple operations in a transaction")
    db.begin_transaction()
    db.put("C", 15)
    db.put("D", 20)
    db.commit()
    assert db.get("C") == 15
    assert db.get("D") == 20
    print(" Test passed\n")
    
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()