#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math                   #importing the math module 


# In[2]:


def mySum (sumNum):             # aid for creating this function obtained from: 
                                #'''https://www.educative.io/edpresso/how-to-compute-the-sum-of-a-list-in-python''' 
                                #accessed 10/4/21
    """
    Function for adding up the components of a list.

    Parameters
    ----------
    sumNum: <list>
        A list of numbers in numerical or string format. The function converts them into integers before calculating.
   
    Returns
    -------
    <int>
        Summed up values
        
    Type
    ----
    function
    """
    
    # this code adds each value in the list to a placeholder with a value
    # of zero. It returns the final value as a sum of all members
    
    N_sum = 0                           
    for i in sumNum:
        N_sum = N_sum + int(i)   
    
    return N_sum



    


# In[3]:


def myMean (meanNum):
    
    """
    Function for calculating the average of all components in a list. myMean function required in namespace.

    Parameters
    ----------
    meanNum: <list>
        A list of numbers in numerical or string format. The function converts them into integers before calculating.
   
    Returns
    -------
    <int>
        Mean of values
        
    Type
    ----
    function
    """
    #  this function finds the mean using all values in the u=input list
    # mySum function needs to be stored in the namespace before this is used
    
    N_mean = len(meanNum)
    mean = mySum(meanNum)/N_mean

    return mean 


# In[4]:


def myMax(maxNum):              # aid obtained from: '''https://www.delftstack.com/howto/python/python-max-value-in-list/''' accessed 10/4/21
    
    """
    Function to calculate the maximum value out of a list.

    Parameters
    ----------
    sumNum: <list>
        A list of values in numerical or string format. The function converts them into integers before calculating.
        Values must contain non-negative numbers.
   
    Returns
    -------
    <int>
        Maximum value in the list 
        
    Type
    ----
    function
    """
    #this function starts from a maximum value of zero and iterates through 
    # the input list to find a number higher than the current value.
    #if ONLY negative numbers are present, the default output is zero.
    a = 0
    for i in maxNum:
        if int(i) >= int(a):
            a = i 
    return a


# In[5]:


def myStd (stdNum): 
    
    """
    Function to calculate the standard deviation using all values in a list. 
    Requires myMean function and math module import.

    Parameters
    ----------
    sumNum: <list>
        A list of values in numerical or string format. The function converts them into integers before calculating.
   
    Returns
    -------
    <int>
        Standard deviation of the values
        
    Type
    ----
    function
    """
    
    degFree = len(stdNum) - 1        # degree of freedom (n-1) value
    residual = []                    # empty list to append deviation of each value to 
    stdMean = myMean(stdNum)
    
    for i in stdNum:
        r = i - stdMean
        residual.append(r**2)
    
    stddev = math.sqrt(1/degFree * mySum(residual))
    
    return stddev


# In[6]:


def readUNpopData (path_UN = './WPP2019_INTHOUSAND.txt'):

    """
    Function that reads in a text population file and returns a list of lists containing population values.
    The header and first column of the file are striped and returned in a list as global variables 'header' and 'countryList'

    Parameters
    ----------
    path_UN: <.txt>
        Has a default file, but it can be switched out for a compatible '.txt' file. 
        
   
    Returns
    -------
    <list>
        Lis of list of population data values in string format
        
    Type
    ----
    function
    """
    try:
    
        file_UN = open( path_UN, 'r')         # open
        print('\n Please wait while the file opens')
    except IOError:
        print('\n Unfortunately, the file could not be read or opened.')
    finally:
        print ('The file should be open now, maybe.')
    
    population_Data = file_UN.readlines()  # read all lines 
    file_UN.close                         # close the .txt file

    populationData_strip = [i.rstrip('\n') for i in population_Data]                      # removes all newline characters at the end of strings 
    populationData_delimit = [i.split(',') for i in populationData_strip]                # delimits the strings at commas and creates a list of lists 
    populationData_strip2 = [[j.strip() for j in i] for i in populationData_delimit]     # removes white space surrounding all elements in the 2nd level list (list in list)
    
    populationData_replace = [[j.replace(' ','') for j in i[1:]] for i in populationData_strip2]    # aid obtained from: 
                                                                                                    # https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/ accessed 10/4/21
                                                                                                    # removes whitespace between numbers in 2nd level list
                                                                                                    # also removes the first column containing regional and country data
    
    population_Data = populationData_replace[1:]         # removes first index (header list) and creates new object list for debugging purposes
    
    global header                                       # assigning header and 
    global countryList                                  # countryList to the global namespace. Future functions and code reference them                             
    global populationData
    
    header = populationData_strip2[0][1:]                      # header is the year list without region (not needed here)
    countryList = [i[0] for i in populationData_strip2[1:]]    # countryList is the list ou countrys without the header  
    populationData  = population_Data

    return populationData                               # list of list containing all population data with matching indeces to header and countryList




# In[8]:
def main():
    """
        Main level function that calculates population staistics. Can be imported as a module to access certain functions. 

        Parameters
        ----------
        None

        Returns
        -------
        <Str>
            Strings containing relevant results. 

        Type
        ----
        function, module 
        """
    readUNpopData()
    
    # code that obtains input to answer question 5
    while True:

        try: 
            countrySearch = input (' \n Which country do you want to know about?')
            countrySearch = countryList[countryList.index(countrySearch)]
            break
        except:
            print ('Please check your input. That country could not be found.')

    print ('Your entry has been succesfully recorded')


    # In[9]:

              # run the function to generate global instances of some variables and assign data to variable

    
    def yearPop (year):
    
        """
        Function that lists the populations of all country for the input year. 

        Parameters
        ----------
        year: <numeric>
            Year in format XXXX

        Returns
        -------
        <list>
            List of populations for the given year

        Type
        ----
        function
        """
        index_year = header.index(str(year))                       # finds the index of the input year
        Population_year = [i[index_year] for i in populationData]  # lists all populations that have the same index as the given year based on the year header
        return Population_year

    
    #Ans 1

    pop_2020 = 1000 * mySum(yearPop(2020)) # finding the population for that year and multiplying by 1000 to get the actual value

    print(f'\n 1 -- The estimated total world population in 2020 is {pop_2020:,}!')


    # In[10]:


    # Ans 2

    # total world population for the given years 
    pop2050 = 1000 * mySum(yearPop(2050))
    pop2100 = 1000 * mySum(yearPop(2100))

    print (f'\n 2 -- The total world population in 2050 and 2100 is {pop2050:,} and {pop2100:,} respectively.') 
    # https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators


    # In[11]:



    def sumPercentage (year1, year2):   # year 2 should be after year 1  

        """
        Function that calculates the percentage change in total world population between two different years. 

        Parameters
        ----------
        year1: <numeric>
            Year in format XXXX
        year2: <numeric>
            Year in format XXXX

        Returns
        -------
        <float>
            Calculated percentage

        Type
        ----
        function
        """
        # formula calculates percentage based on year 1, so that should be the initial year desired
        return 100 * (mySum(yearPop(year2)) - mySum(yearPop(year1)))/mySum(yearPop(year1))


    # In[12]:


    # Ans 3
    # percentage change in world population between two defined years 
    perc2020_2050 = sumPercentage (2020, 2050)
    perc2020_2100 = sumPercentage (2020, 2100)

    print('\n 3 -- The percentage change in population between: ')
    print('2020 and 2050 is {:.2f}%.'.format(perc2020_2050))
    print('2020 and 2100 is {:.2f}%.'.format(perc2020_2100))


    # In[13]:


    # Ans 4

    #  10 years from now is 2030
    index_2030 = header.index(str(2030))                           # finding index for 2030 -- this should work for populationData and countryList
    countryPop2030 = [i[index_2030] for i in populationData]       # creates list of country population in 2030

    cP2030 = countryPop2030[:] #copy of countryPop2030             # creates copy of 2030 population list for mutation purposes 

    firstMax = countryList[(countryPop2030.index(myMax(cP2030)))]  # finding max population in 2030 
    cP2030.remove(myMax(cP2030))                                   # removing the first max value

    secondMax = countryList[(countryPop2030.index(myMax(cP2030)))] # finding next max population which should be second max
    cP2030.remove(myMax(cP2030))                                   # removing the second max value

    thirdMax = countryList[(countryPop2030.index(myMax(cP2030)))]  # finding third max value

    # all indexing is done against the original list, so removal of the max value doesn't affect this

    print('\n 4 -- The list of three countries with the largest population in 2030, from first to third are:')
    print('{}, {} and {}.'.format(firstMax, secondMax, thirdMax))


    # In[14]:


    # Ans 5 
    def countryPop (country, year):

        """
        Function that finds the population of a given country at a given year. 

        Parameters
        ----------
        country: <string>
            Country in string format with the appropriate name
        year: <numeric>
            Year in format XXXX

        Returns
        -------
        <string>
            Desired year in string format 

        Type
        ----
        function
        """

        index_country = countryList.index(country)         # Finds index of the input country
        index_year = header.index(str(year))               # finds index of the input year in the header list 

        return populationData [index_country][index_year]

    # all values multiplied by 1000 to convert into correct values 
    user_2020 = 1000* int(countryPop(countrySearch,2020))
    user_2050 = 1000* int(countryPop(countrySearch, 2050))
    user_2100 = 1000* int(countryPop(countrySearch, 2100))

    print ('\n 5 -- You entered {}.'.format(countrySearch))
    # print ('This country has a population of {} in the year 2020, {} in 2050 and {} in 2100.'.format(user_2020, user_2050, user_2100))
    print (f'This country has a population of {user_2020:,} in the year 2020, {user_2050:,} in 2050 and {user_2100:,} in 2100.')


    # In[15]:


    def popPercentage (pop1, pop2):

        """
        Function that calculates the percentage change in total world population between two different years. 

        Parameters
        ----------
        year1: <numeric>
            Year in format XXXX
        year2: <numeric>
            Year in format XXXX

        Returns
        -------
        <float>
            Calculated percentage

        Type
        ----
        function
        """

        return 100 * (int(pop2) - int(pop1))/int(pop1)


    # In[16]:


    # Ans 6

    #

    countries = ['United States of America', 'China', 'India', 'Nigeria', 'Egypt', 'Brazil', 'Australia', 'France', 'Turkey' ]
    currentPopulation = [countryPop(i,2020) for i in countries]
    futurePopulation = [countryPop(i,2100) for i in countries]


    percentIncrease = [popPercentage (i,j) for i,j in zip(currentPopulation, futurePopulation)] 
    # aid obtained from: https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel  accessed on 10/5/21
    Ans6 = [[i,j,k] for i,j,k in zip (countries, currentPopulation, percentIncrease)]

    print('\n 6 -- Below is a list of countries, their current population, and their projected percentage increase by 2100:\n')

    for i in Ans6:
        print(f'{i[0]} -> {1000*int(i[1]):,} -> {i[2]:.2f}%')


    # In[17]:


    # Ans 7
    allcurrentPopulation = [countryPop(i,2020) for i in countryList]   # current population list of all countries 
    allfuturePopulation = [countryPop(i,2100) for i in countryList]    # future population list of all countries 

    allpercentIncrease = [popPercentage (i,j) for i,j in zip(allcurrentPopulation, allfuturePopulation)]   # percentage increase for each country

    maxIncrease2100 = myMax(allpercentIncrease)                        # maximum percentage increase across countries

    maxIncreaseCountry = countryList[allpercentIncrease.index(maxIncrease2100)]        # country corresponding to the maximum percentage increase

    print (f' \n 7 -- The country with the fastest expected percentage growth until 2100, relative to'        f' their population in 2020 is {maxIncreaseCountry} with a {maxIncrease2100:.2f}% increase!')


    # In[18]:


    # Ans 8

    # API = allpercentIncrease
    meanAPI = myMean (allpercentIncrease)     # mean of the percentage increase across all countries 

    stddevAPI = myStd (allpercentIncrease)    # standard deviation of the percentage increase across all countries 

    print ('\n 8 -- The mean and standard deviation for percentage growth rates for all countries from today until 2100 are {:.2f}% and {:.2f}%, respectively.'.format(meanAPI, stddevAPI)) 


    # In[19]:


    # Ans 9 

    # What is the estimated percentage growth for Ghana in the year 2100? 

    ghanaPop2020 = countryPop('Ghana', 2020)
    ghanaPop2100 = countryPop('Ghana', 2100)

    ghanaGrowth = popPercentage (ghanaPop2020, ghanaPop2100)


    print ('\n 9 -- What is the estimated percentage growth for Ghana from 2020 to 2100?')
    print(' The expected percentage growth for Ghana in 2100 is {:.2f}%. \n' .format(ghanaGrowth) )


if __name__ == '__main__':
    main()
    
    # In[20]:


    # Acknowledgements/ References

    # Google
    # Stackoverflow
    # I had discussions with Rose McGroarty and Ben Eppinger. Ideas and opinions were exchanged, and results were compared, but no code was shared to my knowledge.

