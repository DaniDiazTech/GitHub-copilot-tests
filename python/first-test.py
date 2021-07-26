# Function that computes the average of a dataset
def compute_average(dataset):
    total = 0
    for x in dataset:
        total += x
    return total / len(dataset)

# Implement the function using the splitted input of the user
def main():
    dataset = [int(x) for x in input("Enter the dataset: ").split()]
    print("Average:", compute_average(dataset))

# Call the main function
if __name__ == "__main__":
    main()