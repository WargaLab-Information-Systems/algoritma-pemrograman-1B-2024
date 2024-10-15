buyerName = str(input("Who the heck your name?: "))
buyerAge = int(input("How old are you?: "))
buyerMemberCardCheck = str(input("Do you have a member card? (yes/no): "))
buyerTotalRecipe = int(input("How much is your bill?: Rp "))
discount = 0

if buyerAge < 18:
    print("Your age is not enough")
    exit()

if buyerMemberCardCheck == "yes":
    discount = 15
else:
    print("salesDiscountAlert: u must become a member to get 15% discount")
    
if buyerTotalRecipe > 500000:
    discount += 10
else:
    print(f"salesDiscountAlert: Spend more than 500,000 to receive 10% discount")


discountAfter = buyerTotalRecipe - (buyerTotalRecipe * discount / 100)

print(f"===========================================")
print(f"===== DRINK BAR DISCOUNT RECIPE ===========") 
print(f"===== Buyer Name          : {buyerName} =========")
print(f"===== Discount you get    : {discount}% ===========")
print(f"===== Price before diskon : {buyerTotalRecipe} ========")
print(f"===== Price after diskon  : {discountAfter} =====")
print(f"===========================================")