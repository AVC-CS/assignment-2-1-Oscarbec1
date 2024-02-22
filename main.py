def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    Number_of_Males = int(input("Enter the number of males:"))                            
    Number_of_Females = int(input("Enter the number of females:"))
    #print (f' Some message \total {f_perc: .2f}')
    #print (f' Some message \total {m_perc: .2m}')
    total = (Number_of_Males) + (Number_of_Females)
    m_perc = Number_of_Males / total * 100
    f_perc = Number_of_Females / total *100
    print (m_perc)
    print (f_perc)
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
