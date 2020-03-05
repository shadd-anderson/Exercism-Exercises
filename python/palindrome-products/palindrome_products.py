import math
import multiprocessing
from multiprocessing import Queue


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Minimum factor is larger than max factor")

    product_factors = products(min_factor, max_factor)
    product_list = sorted(product_factors.keys(), reverse=True)
    for num in product_list:
        if is_palindrome(num):
            return num, product_factors[num]

    return None, []


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Minimum factor is larger than max factor")

    product_factors = products(min_factor, max_factor)
    product_list = sorted(product_factors.keys())
    for num in product_list:
        if is_palindrome(num):
            return num, product_factors[num]

    return None, []


def add_factors_to_dict(nums1, nums2, output_q):
    outdict = dict()
    for index, mult1 in enumerate(nums1):
        for mult2 in nums2[index:]:
            factors = outdict.setdefault(mult1 * mult2, [])
            factors.append([mult1, mult2])
    output_q.put(outdict)


def products(num1, num2):
    num2 = num2 + 1
    num_count = len(range(num1, num2))

    cpus = multiprocessing.cpu_count()
    num_procs = num_count if num_count < cpus else cpus
    chunksize = math.ceil(num_count / num_procs)
    out_q = Queue()
    procs = []

    for i in range(num_procs):
        p = multiprocessing.Process(
            target=add_factors_to_dict,
            args=(range(num1, num2)[chunksize * i:chunksize * (i + 1)],
                  range(num1, num2),
                  out_q))
        procs.append(p)
        p.start()
    product_factors = dict()
    for i in range(num_procs):
        product_factors.update(out_q.get())

    for p in procs:
        p.join()

    return product_factors


def is_palindrome(number):
    number = str(number)
    return number == number[::-1]
