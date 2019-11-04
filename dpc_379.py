# https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/

print('What is your annual income(no commas):')
x = int(input())
tax = 0
if 10000 < x <= 30000:
    tax = (x - 10000) * 0.1
if 30000 < x <= 100000:
    tax = 20000 * 0.1
    tax += (x - 30000) * 0.25
if x > 100000:
    tax = 20000 * 0.1
    tax += 70000 * 0.25
    tax += (x - 100000) * 0.4
print(f"You owe {tax} in taxes, wow!")
