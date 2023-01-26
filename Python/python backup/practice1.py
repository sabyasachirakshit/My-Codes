print("Want to see when you will 100 be years old?")
print("Enter your age in 2020 or enter your year of birth")
year=2020
age=int(input())
if age >=0 and age<=100:
     var1=year-age
     var2=var1+100
     print("You will be 100 years old in",var2)
elif age>=1921 and age<=2020:
    var3=age+100
    print("You will be 100 years old in",var3)
elif  age<=1921:
    print("Yor seem to be the oldest person alive")
elif age>=2020:
    print("Yor are not yet born")
print("Do you want know your age in a specific year\n if yes Press y, if no press n")
var4=input()
if var4=="y":
    print("Enter the specific year")
    var5=int(input())
    if age >=0 and age<=100:
        var1 = year - age
        if var5 >= year:
            var6=var5-var1
            print("You will be",var6,"years old")
        elif var5 <= year and var5>=var1:
            var6=var5-var1
            print("You was",var6,"years old")
        elif var5<=var1:
            print("Yor were not yet born")
    elif age >= 1921 and age <= 2020:
        if var5 >= year:
            var6 = var5 - age
            print("You will be", var6, "years old")
        elif var5 <= year and var5 >=age:
                var6 = var5 - age
                print("You was", var6, "years old")
        elif var5 <= age:
                print("Yor were not yet born")
