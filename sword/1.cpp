# include <iostream>

using std::cin, std::cout, std::endl;

class CMyString
{
    public:
        // constructor
        CMyString(char *pData = NULL);
        // copy constructor
        CMyString(const CMyString &str);
        // destructor
        ~CMyString(void);

    private:
        char * m_pData;
};

// Reload assign operator -- method 1
CMystring &CMyString::operator = (const CMyString &str) {
    if (this == &str)
        return *this;

    delete []m_pData;
    m_pData = NULL;
    m_pData = new char[strlen(str.m_pData) + 1];
    strcpy(m_pData, str.m_pData);

    return *this;
}

// more advanced
// taking care of the possible error arised by
// limited memory (which will make m_pData a NULL ptr)
CMyString &CMyString::operator = (const CMyString &str) {
    if (this != &str) {
        CMyString strTemp(str);

        char *pTemp = strTemp.m_pData;
        strTemp.m_pData = m_pData;
        m_pData = pTemp;
    }

    return *this;
}
