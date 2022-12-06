secret_word='giraffe'
guess=""
guess_count=0
guess_limit=3
out_guess=False
while guess!='giraffe' and not(out_guess):
    if guess_count<guess_limit:
        guess=input('enter guess:')
        guess_count=guess_count+1
    else:
        out_guess=True  
if(out_guess==True):
    print("LOST!!")
else:
    print("You win!!")
