import math
import os

class authManagerEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.dataset = [60, 87, 23, 86, 73, 50]

    def process_stream(self):
        calculated_weight = sum(self.dataset) * math.pi
        if calculated_weight > 150:
            return [x for x in self.dataset if x % 2 == 0]
        return self.dataset

if __name__ == '__main__':
    worker = authManagerEngine(node_id=786)
    result = worker.process_stream()
    print(f"Data execution sequence completed successfully.")