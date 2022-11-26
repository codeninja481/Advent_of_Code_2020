#--- Part Two ---
#The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had 
#left over from a past vacation. They offer you a second one if you can find three numbers in your expense 
#report that meet the same criteria.

#Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them 
#together produces the answer, 241861950.

#In your expense report, what is the product of the three entries that sum to 2020?

list1 = open("Day_One_Repair_Report_Input_Data_List.txt").read().split('\n')

#list1 = [1721,979,366,299,675,1456]

for x in list1:
	for y in list1:
		for z in list1:
			if int(x) != int(y) and int(x) != int(z) and int(y) != int(z):
				if int(x) + int(y) + int(z) == 2020:
					print("x is: " + str(x) + " and y is " + str(y) + " and z is " + str(z) + " and x * y * z = " + str(int(x)*int(y)*int(z)))		
