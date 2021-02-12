import camelot

def find_camelot_tables(input_filepath):
    tables=camelot.read_pdf(input_filepath)
    print(tables)
    if (len(tables)):
        tables_list=[]
        # tables.export('output.csv', f='csv', compress='True')
        for table in tables:
            # table.to_csv('output.csv')
            # print(table.df)
            print("Digital PDF, Camelot detection done")
            tables_list.append(table.df)    
        return (tables_list)
    else:
        print("PDF with digital text, but no easily identified tables")
        return 1
