
import math
from . import constants


# Check for 
# How many People should be allowed,
# In Which City
# In Which Company
# For How long

def area_of_city():
    """Area of city and How many people it can handle at a time"""
    area = 1
    return area

def number_of_people_working_in_city():
    number = 1
    return number

def minimum_distance_to_be_maintained():
    """Distance in meters"""
    return constants.MIN_DISTANCE_TO_BE_MAINTAINED_FROM_EACH_OTHER

#def how_much_can_be_handled(area_of_the_place):
#    """
#    Actual Algo to calculate 
#    How many people can be allowed 
#    to be out at 1 point in time
#    """
#    first_number = area_of_city/minimum_distance_to_be_maintained()
#    if first_number < 1:
#        handle = 1
#    else:
#        handle = math.ceil(handle)
#        handle = pow(handle, handle)
#    return handle

def how_many_can_be_handled(area):
    """
    area: area of any place/company etc in SquareMeters
    minimum_distance_to_be_maintained in Meters
    """
    # Since area is in SquareMeters, 
    # We will first find the SquareRoot of it
    sqrt_of_area = math.sqrt(area)
    # Getting the 
    #number_of_points = area/minimum_distance_to_be_maintained()
    # Getting the Quotient
    number_of_points = sqrt_of_area//minimum_distance_to_be_maintained()
    # If its exactly half or Greater than Half
    # Then, the NumberOfPoints will be 2 points at each of the distance + 1 point at the origin
    # And, NumberOfPeople is  SquareTheValueOf(NumberOfPoints)
    if number_of_points == 2 or number_of_points > 2:
        number_of_points += 1
        #allowed = pow(number_of_points, number_of_points)
    # If division greater than half_of_area, so division less than 2
    # Then, NumberOfPoints will Most Probably 1 + 1 At Origin
    # NumberOfPeople is SquareTheValueOf(NumberOfPoints)
    elif number_of_points < 2: 
        number_of_points = 2

    handle = pow(number_of_points, 2)
    return handle

def check_for_previous_people_not_given_chance_allow_them():
    not_given_chance_yet_so_allow_them_now = 1
    return not_given_chance_yet_so_allow_them_now


