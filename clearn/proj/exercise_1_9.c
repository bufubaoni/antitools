char * copy_printf(char * s){
    char * t;
    bool is_blank = false;
    for(;*s != '\0';s++)
    {
        if (is_blank && *s = ' ')
        {
            is_blank = true;
            *t = *s;
            t ++;
        }
        else
        {
            *t = *s;
            t ++;
            is_blank = false;
        }
    }
    return t;
}

