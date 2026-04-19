def calculate_output(x, count):
    results = []
    for _ in range(count):
        if x % 2 == 0:
            x = (1/2) * x
        else:
            x = x - 5
        results.append(x)
    return results

def main():
    initial_x = 2
    repeat_count = int(input("Please enter the number of repeats: "))
    
    all_results = calculate_output(initial_x, 2024)
    
    if len(all_results) >= 2024:
        print(f"The results of the 2024th output are: {all_results[2023]}")
    else:
        print("The number of repetitions is insufficient to calculate the result of the 2024th.")

if __name__ == "__main__":
    main() 