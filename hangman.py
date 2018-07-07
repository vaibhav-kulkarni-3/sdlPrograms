import random

wordlist = ['apple', 'banana' , 'carrot' , 'tomato']
hangman_pic = ('x--------------------------------x',
	       'x--------------------------------x\n \
	       		|\n\
	       		|\n\
	       		|',
	       	'x--------------------------------x\n \
	       		|\n\
	       		|\n\
	       		|\n\
	       		0',
	       		
	       	'x--------------------------------x\n \
	       		|\n\
	       		|\n\
	       		|\n\
	       		0\n\
	       	       /|\ ',	
	       	'x--------------------------------x\n \
	       		|\n\
	       		|\n\
	       		|\n\
	       		0\n\
	       	       /|\n\
	       	        /\ ',
	       	 )
	       	 
def guess(word):
 	guess_letter = input("enter the alphabet ").lower()
 	if guess_letter in word :
 		return 1,guess_letter
 	else :
 		return 0 ,guess_letter
 		
 		
def playHangman():
	print("----------------------------")
	print("so lets start guessing ! ")
	ans =""
	hang = 0
	word = random.choice(wordlist)
	print(word)
	for i in range(0 , len(word)):
		test,guess_letter = guess(word)
		if test:
			print(" you guess it right \n")
			for i in range(0 , len(word)):
				if guess_letter == word[i] or word[i] in word:
					#print(" "+guess_letter+ " ")
					ans.join(word[i])
				else:
					print(" ")
					ans.join(" ")
			ans = ans						
		else:
			print(hangman_pic[hang]+"\n \n")
			hang = hang + 1
			if hang == len(hangman_pic)+1:
				print("game over, better luck nect time \n")
				break
 			
 			
def main():
	playHangman()
 	
 	
 
main()					
 					
	       	 
	       	 
	       	       	       
	       		
	       			
