import socket
import heapq
import glob

FILEPATH = './home/output/tmp.txt'

def get_n_largest_pairs(dictionary, n):
    # Convert dictionary items to a list of tuples (value, key) for heapq
    heap = [(-value, key) for key, value in dictionary.items()]
    # Convert the list into a max heap
    heapq.heapify(heap)
    
    # Get the n largest pairs
    largest_pairs = []
    for _ in range(n):
        if heap:
            value, key = heapq.heappop(heap)
            largest_pairs.append((key, -value))
        else:
            break
    return largest_pairs

def Merge(dict1, dict2):
    return(dict2.update(dict1))

def countWords(filePath):
    try:
        with open(filePath, 'r') as file:
            wordCounts = {}
            for line in file:
                for word in line.split():
                    if word in wordCounts.keys():
                        wordCounts[word] += 1
                    else:
                        wordCounts[word] = 1
            # print(wordCounts)
            return wordCounts

    except Exception as e:
        print("An Error Occured: ", e)
        

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

try:
    with open(FILEPATH, 'w') as file:
        # Write Folder contents
        file.write(listToString(glob.glob('./*')))
        print(listToString(glob.glob('./*')))

        # Word Counts
        wordCountLimerick = countWords('./Limerick-1.txt')
        wordCountIF = countWords('./IF.txt')
        
        # Three Largest Word Counts in IF
        n = 3
        largest_pairs = get_n_largest_pairs(wordCountIF, n)
        print(f"The {n} key-value pairs with the largest values:")
        for key, value in largest_pairs:
            file.write(f"{key}: {value}")
            print(f"{key}: {value}")

        # Write Word Count
        file.write("WORD COUNT LIMERICK: " + str(wordCountLimerick))
        file.write("WORD COUNT IF: " + str(wordCountIF))

        # Find IP Address
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        
        # Write IP Address
        file.write("Your Computer Name is:" + hostname)
        file.write("Your Computer IP Address is:" + IPAddr)
        print("Your Computer Name is:" + hostname)
        print("Your Computer IP Address is:" + IPAddr)


        file.close()


except Exception as e:
    print("An Error Occured: ", e)



# print(wordCount)




# Example usage:
# my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30, 'e': 15}




