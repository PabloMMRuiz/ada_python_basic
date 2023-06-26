def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
print(list_sum([1,3,5,7,9]))    

#Self check page 120
"""
How many recursive calls are made when computing the sum of the list [2, 4, 6, 8, 10]?
1. 6
2. 5
3. 4
4. 3

There are 4 calls made
"""

"""
Suppose you are going to write a recursive function to calculate the factorial of a number.
fact(n) returns n * n-1 * n-2 * . . . Where the factorial of zero is defined to be 1. What would
be the most appropriate base case?
1. n == 0
2. n == 1
3. n >= 0
4. n <= 1

n =< 0. This is the factorial of an Integer.
n ==1 would break with n=0 case
n == 0 wqould work as well, but require an extra unnecesary call
n>=0 would stop at first call as all f<ctorial numbers are positive integers.
"""

def recursive_factorial(n:int)->int:
    if n<0:
        raise ValueError("Negative integers not deffined for factorial")
    if n <=1:
        return 1
    else:
        return n*recursive_factorial(n-1)
    
print(recursive_factorial(5))


def integer_to_base_string(n:int, base:int, lookup_string = "0123456789ABCDEF")->str: 
    """Returns the string representation of a decimal number in the given base
    base must be consistent with lookup_string
    """
    if base >len(lookup_string):
        raise ValueError("Base tooo big for given conversion")
    if n < base:
        return lookup_string[n]
    else:
        return integer_to_base_string(n//base, base) + lookup_string[n%base]
    
print(integer_to_base_string(29468, 16))

#Self cehck page 122
#Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.

def string_inversion_recursive(rev_string:str)->str:
    if len(rev_string) ==1:
        return rev_string
    else:
        return string_inversion_recursive(rev_string[1:]) + rev_string[0]
    
print(string_inversion_recursive("Hola me llamo Pablo"))


def palindrome_checker_recursive(test_str:str)->bool:
    if len(test_str) == 1:
        return True
    else:
        return (test_str[0]==test_str[-1]) and palindrome_checker_recursive(test_str[1:len(test_str)-1])
print(palindrome_checker_recursive("aibohphobia")) #aibohphobia is the fear of palindromes


import math
import turtle
import random #Cursed import location eh
"""my_turtle = turtle.Turtle()
my_win = turtle.Screen()
def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)
#draw_spiral(my_turtle, 100)
#my_win.exitonclick()"""

#Modified following self check on page 130
def tree(branch_len, thickness, colour, top_sub, min_sub, t: turtle): #Top and ,im sub are a personal modification so we have more leaves and green branches:
    #Each call substracts a bit less from the branch_len. It is ensured to reach 0. Too lazy to screen for erroes, you should make sure top>min
    t.pensize(thickness)
    t.pencolor(colour)
    if branch_len > 5 and thickness >=0:
        t.forward(branch_len)
        right_turn = random.randrange(15,30)
        left_turn = random.randrange(15,30)
        t.right(right_turn)
        tree(branch_len - random.randrange(min_sub,top_sub),thickness-2,"green" if thickness<8 else "brown",top_sub-1, min_sub-1, t)
        t.left(right_turn+left_turn)
        tree(branch_len - random.randrange(min_sub,top_sub),thickness-2,"green" if thickness<8 else "brown",top_sub-1, min_sub-1, t)
        t.up()
        t.right(left_turn) #This undoes the turn so it can go backwards
        t.backward(branch_len)
        t.down()
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(120)
    t.down()
    t.color("green")
    tree(100,16, "brown",20,10, t)
    my_win.exitonclick()
#main()
def draw_triangle(points, color, my_turtle:turtle.Turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0],points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, my_turtle):
    color_map = ['black', 'red', 'white', 'black', 'red', 'white', 'black']
    draw_triangle(points, color_map[degree], my_turtle) #This draws the outer triangle
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree-1, my_turtle)
        sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree-1, my_turtle)
        sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree-1, my_turtle)
def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(my_points, 4, my_turtle)
    my_win.exitonclick()
#main()
#Tower of Hanoi

def move_disk(fp,tp, height):
    print("moving disk of size",height,"from",fp,"to",tp)
def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole, height) #This also takes care of the base case!
        move_tower(height - 1, with_pole, to_pole, from_pole)

move_tower(3, "A", "C", "B")


#Programming excercises

#Write a recursive function to reverse a list

def list_reverse_recursive(l:list)->list:
    if len(l) <=1:
        return l #Base case
    else:
        temp = list_reverse_recursive(l[1:]) #Recursive call and progress towards base case
        temp.append(l[0])
        return  temp
print(list_reverse_recursive([1,2,3,4,5,6,7,8,9]))


def get_random_point_along_line(p1, p2):
    x_coord = p1[0] + random.random()*(p2[0]-p1[0])
    y_coord = (p2[1]-p1[1])/(p2[0]-p1[0]) * (x_coord - p1[0]) + p1[1] #This is the ecuation of the line defined by p1, p2 applied to a point between them
    return (x_coord, y_coord)
def fractal_mountain(points, degree, t): #Maybe?
    draw_triangle(points, "white",t)
    if degree > 0:
        p1, p2, p3 = get_random_point_along_line(points[0], points[1]), get_random_point_along_line(points[1], points[2]), get_random_point_along_line(points[2], points[0])
        fractal_mountain([points[0], p1, p3], degree-1, t)
        fractal_mountain([points[1], p1, p2], degree-1, t)
        fractal_mountain([points[2], p2, p3], degree-1, t)
        fractal_mountain([p1,p2,p3], degree-1, t)
        

def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-150, -50], [0, 200], [150, -50]]
    fractal_mountain(my_points, 4, my_turtle)
    my_win.exitonclick()
    #God knows what will come out of this

#main()

def perpendicular_distance(p1, p2, p3): #This is auxiliary for the next function. We use three points in order to have a heigth growth proportional to the length of the side.
    #This is used to make the mountain grow only outwards:
    if p1[1] > p3[1]:
        x_coord = p2[0]+ random.random()*(math.sqrt((p3[1]-p1[1])**2 + (p3[0]-p1[0])**2))/2.75
    else:
        x_coord = p2[0]- random.random()*(math.sqrt((p3[1]-p1[1])**2 + (p3[0]-p1[0])**2))/2.75
    if p3[1] - p1[1] != 0:
        y_coord = -1/((p3[1]-p1[1])/(p3[0]-p1[0])) * (x_coord - p2[0]) + p2[1]
    else:
        y_coord = p1[1] + random.random()*(p3[0]-p1[0])/3
    return(x_coord, y_coord)

def fractal_growing_mountain(points, degree, t, side=None): #Padre nuestro que estas en el cielo
    center_point = get_random_point_along_line(points[0], points[1])
    perturbated_point = perpendicular_distance(points[0], center_point, points[1])
    """if points[0][0]>perturbated_point[0] or points[1][0] < perturbated_point[0]:
        return"""
    draw_triangle([points[0], points[1], perturbated_point], "white", t)
    if degree > 0:
        fractal_growing_mountain([points[0], perturbated_point], degree-1, t)
        fractal_growing_mountain([perturbated_point, points[1]], degree-1, t)

def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-150, -50],[150, -50]]
    fractal_growing_mountain(my_points, 4, my_turtle)
    my_win.exitonclick()
    #Well I mean it's not that bad... sometimes
#main()

def fibonacci_recursive(n):
    if n<=2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
print(fibonacci_recursive(8))