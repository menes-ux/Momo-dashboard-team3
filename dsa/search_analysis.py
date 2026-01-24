import time
import uuid
import random

class SearchAnalyzer:
    def __init__(self):
        self.data = self._generate_mock_data(1000)
        self.lookup_table = self._build_lookup_table()

    def _generate_mock_data(self, count):
        print(f"Generating {count} mock transactions for testing...")
        data = []
        for _ in range(count):
            data.append({
                "transactionId": str(uuid.uuid4()),
                "amount": random.uniform(100.0, 50000.0),
                "status": "SUCCESS"
            })
        return data

    def _build_lookup_table(self):
        """
        Convert list to dictionary for O(1) access.
        Key = transactionId, Value = Transaction Object
        """
        table = {}
        for t in self.data:
            table[t["transactionId"]] = t
        return table

    def linear_search(self, target_id):
        """
        Scan through the list one by one.
        Complexity: O(n)
        """
        for transaction in self.data:
            if transaction["transactionId"] == target_id:
                return transaction
        return None

    def dictionary_search(self, target_id):
        """
        Look up directly by key.
        Complexity: O(1) Average Case
        """
        return self.lookup_table.get(target_id)

    def run_comparison(self):
        target_record = self.data[500] 
        target_id = target_record["transactionId"]
        
        print(f"\n--- Searching for ID: {target_id} ---")


        start_time = time.perf_counter()

        for _ in range(1000):
            self.linear_search(target_id)
        end_time = time.perf_counter()
        linear_duration = (end_time - start_time)
        print(f"Linear Search (1000 runs): {linear_duration:.6f} seconds")


        start_time = time.perf_counter()
        for _ in range(1000):
            self.dictionary_search(target_id)
        end_time = time.perf_counter()
        dict_duration = (end_time - start_time)
        print(f"Dictionary Search (1000 runs): {dict_duration:.6f} seconds")


        if dict_duration > 0:
            speedup = linear_duration / dict_duration
            print(f"\nResult: Dictionary lookup is {speedup:.2f}x faster than Linear Search.")
        
if __name__ == "__main__":
    analyzer = SearchAnalyzer()
    analyzer.run_comparison()