

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")


def get_user_input():
    nums = []
    x = input()
    x = x.split(",")

    for stringedNums in x:
        nums.append(float(stringedNums))
    return nums


def cal_average_temp(nums):
    average = 0
    for x in nums:
        average = average + x
    average = average / len(nums)
    return average


def calc_min_max_temperature(nums):
    return [int(min(nums)), int(max(nums))]

def calc_median_temperature(nums):
    import statistics
    return statistics.median(nums)
def temperature_ascend(nums):
    return sorted(nums)
if __name__ == "__main__":
    main()
    display_main_menu()
    lists = get_user_input()
    print(cal_average_temp(lists))
    print(calc_min_max_temperature(lists))
    print(temperature_ascend(lists))
    print(calc_median_temperature(lists))