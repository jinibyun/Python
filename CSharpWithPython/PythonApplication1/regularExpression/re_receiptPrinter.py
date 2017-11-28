import re
sentences ="""    
            Datametrex Demo             

        OCTOBER 16, 2017   11:56        
      SALE #POS-3165     S/P-STAFF      
----------------------------------------
DTCODE000031 CAMEL                      
              1.00 @ 12.99         12.99
DTCODE000022 COCA COLA CLASSIC          
              1.00 @ 0.99           0.99

                   SUBTOTAL        13.98
 SALE        13.98
                  PAID CASH        13.98
----------------------------------------
         Thank you for shopping         
.
.
.
d0
"""
strs = sentences.splitlines()

for sentence in strs: 
    if(len(sentence) > 0):
        print(sentence.strip())


"""
0. predefined data 
1. exclude
    1-1. Company name or product name: 
        eg. 
            DataMetrex
    1-2. Date : 
        eg. 
            OCTOBER 16, 2017   11:56
    1-3. Same pattern line: 
        eg. 
            SALE #POS-3165     S/P-STAFF
            -----------------
            Thank you
    1-4. Less than certain length
        eg. 
            less than 10, 11...

2. split item, summary
     
"""








exp = "[a-z]+"
p = re.compile(exp)
m = p.match('CrowHello')
print(m)

