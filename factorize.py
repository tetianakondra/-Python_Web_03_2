from multiprocessing import Pool, cpu_count
from time import time



def factorize(int_number):
    
    div_list = []
    for i in range(1, int_number+1):
        if int_number % i == 0:
            div_list.append(i)
    print(f"{div_list}")
    return div_list


if __name__ == "__main__":

    timer = time()
    check_list = [32, 114, 128, 255, 99999, 10651060]
    for el in check_list:
        factorize(el)
    print(f'Done as sync function: {round(time() - timer, 4)}')
    
    timer = time()
    with Pool(cpu_count()) as p:
        p.map_async(
            factorize,
            check_list,
        )
        p.close() 
        p.join()  
    print(f'Done by {cpu_count()} processes: {round(time() - timer, 4)}')