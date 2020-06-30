// atoi.cc -- change string to integer
#include <iostream>
#include <string>
#include <cctype>
using std::string;

int main()
{
    string str("42");
    long result = 0;
    int indicator = 1;

    int n = str.find_first_not_of(' ');
    if (isalpha(str[n]))
        return 0;
    if (str[n] == '-') {
        indicator =  -1;
        ++n;
    } else if (str[n] == '+') {
        indicator = 1;
        ++n;
    }

    for (n; n != str.size(); ++n) {
        if (isdigit(str[n])) {
            result = result * 10 + str[n];
            if (result*indicator >= INT32_MAX)
                return INT32_MAX;
            if (result*indicator <= INT32_MIN)
                return INT32_MIN;
        } else {
            std::cout << result * indicator;
            return result * indicator;
        }
    }    
}