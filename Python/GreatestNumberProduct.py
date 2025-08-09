def greatest_product_equal_to_element(arr):
    arr_set=set(arr)
    max_product=-1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                product=arr[i] * arr[j]
                if product in arr_set:
                    max_product=max(max_product,product)
    return max_product
        
ARR = [1, 2, 3, 6, 12]
ans=greatest_product_equal_to_element(ARR)
print(ans)