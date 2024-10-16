import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiter = ',|\n'  
        
        if numbers.startswith('//'):
            custom_delimiter, numbers = numbers[2:].split('\n', 1)
            delimiter = re.escape(custom_delimiter)
        
        num_list = re.split(delimiter, numbers)
        
        negatives = []
        total = 0
        for num in num_list:
            if num:
                n = int(num)
                if n < 0:
                    negatives.append(n)
                total += n
        
        if negatives:
            raise Exception(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
        
        return total
