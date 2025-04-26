def ordseleccion(arr):
    for mano in range(len(arr)-1):
        posmin = mano
        for ojo in range(mano + 1, len(arr)):
            if arr[ojo] < arr[posmin]:
                posmin = ojo
            arr[mano], arr[posmin] = arr[posmin], arr[mano]
    
def ordinsercion(arr):
    for actual in range(1, len(arr)):
        sig=actual
        while sig >0 and arr[sig-1]>arr[sig]:
            arr[sig],arr[sig-1]=arr[sig-1],arr[sig]
            sig=sig-1
    
a = [2,8,5,3,9,4,1]
#ordseleccion(a)
ordinsercion(a)
print(a)