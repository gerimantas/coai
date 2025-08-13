"""
Data processing module with various issues for testing COAI
"""

import json
import csv
import datetime

class DataProcessor:
    def __init__(self):
        self.data = []
        self.processed_count = 0
    
    def load_from_file(self, filename):
        # Missing error handling and type validation
        with open(filename, 'r') as f:
            data = json.load(f)
        self.data = data
        return len(data)
    
    def filter_data(self, condition):
        # Inefficient implementation - should use list comprehension
        filtered = []
        for item in self.data:
            if condition(item):
                filtered.append(item)
        return filtered
    
    def transform_dates(self):
        # Bug: assumes all items have 'date' field
        for item in self.data:
            date_str = item['date']  # Will crash if 'date' key doesn't exist
            item['parsed_date'] = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return self.data
    
    def calculate_averages(self, field):
        # No validation if field exists or contains numeric values
        values = [item[field] for item in self.data]
        return sum(values) / len(values)
    
    def export_to_csv(self, filename, fields=None):
        # Missing error handling for file operations
        if fields is None:
            fields = self.data[0].keys()  # Assumes data exists and not empty
        
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(self.data)
    
    def merge_datasets(self, other_data, key_field):
        # Inefficient O(n²) algorithm
        for item in self.data:
            for other_item in other_data:
                if item[key_field] == other_item[key_field]:
                    item.update(other_item)
                    break
    
    def validate_data(self):
        # Incomplete validation logic
        errors = []
        for i, item in enumerate(self.data):
            if not isinstance(item, dict):
                errors.append(f"Item {i} is not a dictionary")
            # Should validate more fields, data types, required fields, etc.
        return errors

# Test data and usage
if __name__ == "__main__":
    processor = DataProcessor()
    
    # Sample data for testing
    test_data = [
        {"id": 1, "name": "John", "age": 30, "salary": 50000},
        {"id": 2, "name": "Jane", "age": 25, "salary": 45000},
        {"id": 3, "name": "Bob", "age": 35}  # Missing salary field
    ]
    
    processor.data = test_data
    
    # This will work
    print("Average age:", processor.calculate_averages("age"))
    
    # This will crash - missing salary field for Bob
    # print("Average salary:", processor.calculate_averages("salary"))
    
    # This will crash - no date field
    # processor.transform_dates()
