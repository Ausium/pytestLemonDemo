# import roslibpy

# ros = roslibpy.Ros(host='localhost', port=9090)
# ros.run()
# print(ros.is_connected)



from asyncio.windows_events import NULL


def search(arr, target): 
    left = 0
    right = len(arr) - 1
    count = 0
    while(left <= right): 
        
        mid = round((left + right)/2)
        
        if(arr[mid] == target):
            return mid

        if(arr[left] <= arr[mid]):
            print('运行第{}'.format(count))
            # 转折在右半边
            if(arr[left] <= target & arr[mid] > target):
                right = mid - 1
            
            else:
                left = mid + 1
        else:
            # 转折在左半边
            
            if(arr[mid] < target & arr[right] >= target):
                right = mid + 1
            
            else:
                left = mid - 1

    return NULL
        
arr = [4,5,1,2,3]
search(arr, 2)



