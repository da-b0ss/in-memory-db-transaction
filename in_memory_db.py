class TransactionNotInProgressError(Exception):
    """Exception raised when trying to modify the database without an active transaction."""
    pass

class NoActiveTransactionError(Exception):
    """Exception raised when trying to commit or rollback without an active transaction."""
    pass

class TransactionAlreadyInProgressError(Exception):
    """Exception raised when trying to start a transaction when one is already in progress."""
    pass

class InMemoryDB:
    def __init__(self):
        # Main database state
        self._data = {}
        # Track if a transaction is in progress
        self._transaction_in_progress = False
        # Track changes made within the current transaction
        self._transaction_changes = {}
    
    def get(self, key):
        """
        Returns the value associated with the key or None if the key doesn't exist.
        This method can be called anytime, even when a transaction is not in progress.
        
        Args:
            key (str): The key to look up
            
        Returns:
            int or None: The value associated with the key, or None if the key doesn't exist
        """
        # If there's a transaction in progress and the key was modified in it
        # we should return None until the transaction is committed
        if self._transaction_in_progress and key in self._transaction_changes:
            return None
        
        # Otherwise, return from the main database state
        return self._data.get(key, None)
    
    def put(self, key, val):
        """
        Creates a new key with the provided value if the key doesn't exist.
        Otherwise, updates the value of an existing key.
        This method can only be called when a transaction is in progress.
        
        Args:
            key (str): The key to create or update
            val (int): The value to associate with the key
            
        Raises:
            TransactionNotInProgressError: If called when a transaction is not in progress
        """
        if not self._transaction_in_progress:
            raise TransactionNotInProgressError("Cannot put key-value pair without an active transaction")
        
        # Store the key-value pair in the transaction changes
        self._transaction_changes[key] = val
    
    def begin_transaction(self):
        """
        Starts a new transaction. At a time only a single transaction may exist.
        
        Raises:
            TransactionAlreadyInProgressError: If called when a transaction is already in progress
        """
        if self._transaction_in_progress:
            raise TransactionAlreadyInProgressError("A transaction is already in progress")
        
        self._transaction_in_progress = True
        self._transaction_changes = {}
    
    def commit(self):
        """
        Applies changes made within the transaction to the main state.
        This ends the current transaction.
        
        Raises:
            NoActiveTransactionError: If called when no transaction is in progress
        """
        if not self._transaction_in_progress:
            raise NoActiveTransactionError("No transaction is in progress to commit")
        
        # Apply all changes from the transaction to the main database
        for key, value in self._transaction_changes.items():
            self._data[key] = value
        
        # End the transaction
        self._transaction_in_progress = False
        self._transaction_changes = {}
    
    def rollback(self):
        """
        Aborts all changes made within the transaction.
        This ends the current transaction.
        
        Raises:
            NoActiveTransactionError: If called when no transaction is in progress
        """
        if not self._transaction_in_progress:
            raise NoActiveTransactionError("No transaction is in progress to rollback")
        
        # Simply discard all transaction changes
        self._transaction_in_progress = False
        self._transaction_changes = {}