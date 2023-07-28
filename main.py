print('This is a tool which can recognize whether the number is a palindrome number.')
num = input('Please enter a number: ')

class Solution:
	def isPalindrome(self, x):
		list_num = list(x)
		print('Is the number is a palindrome number:', list_num == list_num[::-1])

result = Solution()
result.isPalindrome(num)