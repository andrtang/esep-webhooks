class InMemoryDB:
    def __init__(self):
        self.db = {}
        self.current = {}
        self.transaction_started = False

    def get(self, key):
        if key in self.db:
            return self.db[key]
        return None

    def put(self, key, value):
        if not self.transaction_started:
            raise Exception("No transaction in progress")
        self.current[key] = value

    def begin_transaction(self):
        if self.transaction_started:
            raise Exception("A transaction is already in progress")
        self.transaction_started = True

    def commit(self): # commit current to db
        if not self.transaction_started:
            raise Exception("No transaction in progress")

        self.db.update(self.current)
        self.current = {}
        self.transaction_started = False

    def rollback(self): # erase current
        if not self.transaction_started:
            raise Exception("No transaction in progress")

        self.current = None
        self.transaction_started = False

