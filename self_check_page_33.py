"""
Function that genetrates a random 27 character string, then compares it to 'methinks it is like a weasel' and returns a score based on how many
characters match

Then improve upon the program in the self check by keeping letters that are correct
and only modifying one character in the best string so far
"""
import random

def infinite_moneys(match, iters):
    score = 0
    res = ""
    for i in range(iters):
        trying_string = "".join(random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '], k=len(match)))
        temp_score = 0
        for index, char in enumerate(trying_string):
            if char == match[index]:
                temp_score +=1
        if temp_score > score:
            score = temp_score
            res = trying_string
    return(score, res)


def infinite_moneys_hill_climbing(match, iters):
    score = 0
    res = "_"*len(match)
    incorrect = list(range(len(match)))
    for i in range(iters):
        trying_string = "".join(random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '?', '!'], k=len(incorrect)))
        for index, char in zip(incorrect, trying_string):
            if char == match[index]:
                score +=1
                incorrect.remove(index)
                res = res[0:index] + char + res[index+1:]
                if score >= len(match):
                    print(res,"     ", i, score)
                    return
        print(res,"     ", i, score)
    print([match[i] for i in incorrect])
    return(score, res)

if __name__ == "__main__":
    max_score = 0
    n_iter = 0
    """while True:
        score, res = infinite_moneys("methinks it is like a weasel", 1000)
        n_iter+=1000
        print(score, res)
        max_score = max(score, max_score)
        print("________%d_____________%d" %(max_score, n_iter) )
        """
    
    infinite_moneys_hill_climbing("odit incidunt necessitatibus maiores neque consequuntur quia ipsam. aut quo atque dolores voluptatibus libero laboriosam sed eveniet. beatae id consequatur et. natus quia nisi eaque. eos at nostrum alias iure vel ullam eius beatae.", 10000)
