# Problem 1: Reverse Sentence
def reverse_sentence(sentence):
    sentence = sentence.split(" ")
    sentence.reverse()  # res = sentence[::-1]
    return " ".join(sentence)


sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))


# Problem 2: Goldilocks Number
def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    mx = max(nums)
    mi = min(nums)
    for n in nums:
        if n != mx and n != mi:
            return n
    return -1

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))