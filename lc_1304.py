class Solution:
    def sumZero(self, n: int) -> List[int]:
        result_array = []
        num_pairs = n // 2

        generated_numbers = set()
        for _ in range(num_pairs):
            while True:
               
                rand_num = random.randint(1, 1000)
                
               
                if rand_num not in generated_numbers and -rand_num not in generated_numbers:
                    generated_numbers.add(rand_num)
                    generated_numbers.add(-rand_num)
                    result_array.append(rand_num)
                    result_array.append(-rand_num)
                    break
    
    
        if n % 2 != 0:
        
            if 0 not in result_array:
                result_array.append(0)

    
        random.shuffle(result_array)
    
        return result_array
                

