
# Will define stations pulled from API and loop through this section.

from DataFetch import*
from Stations import*


ftp_path_dly_all = '/pub/data/ghcn/daily/all/'

def connect_to_ftp():
    """
    Get FTP server and file details
    """
    ftp_path_root = 'ftp.ncdc.noaa.gov'
    # Access NOAA FTP server
    ftp = FTP(ftp_path_root)
    message = ftp.login()  # No credentials needed
    # print(message)
    return ftp

def get_flags(s):
    """
    Get flags, replacing empty flags with '_' for clarity (' S ' becomes '_S_')
    """
    m_flag = s.read(1)
    m_flag = m_flag if m_flag.strip() else '_'
    q_flag = s.read(1)
    q_flag = q_flag if q_flag.strip() else '_'
    s_flag = s.read(1)
    s_flag = s_flag if s_flag.strip() else '_'
    return [m_flag + q_flag + s_flag]

def create_dataframe(element, dict_element):
    """
    Make dataframes out of the dicts, make the indices date strings (YYYY-MM-DD)
    """
    # element = element.upper()
    df_element = pd.DataFrame(dict_element)
    # print df_element

    # Separate dfs' pass this point containing data for full record.
    # Need to filter out unwanted data to ensure final output is complete.

    # Add dates (YYYY-MM-DD) as index on df. Pad days with zeros to two places
    df_element.index = df_element['YEAR'] + '-' + df_element['MONTH'] + '-' + df_element['DAY'].str.zfill(2)
    df_element.index.name = 'DATE'
    # Arrange columns so ID, YEAR, MONTH, DAY are at front. Leaving them in for plotting later - https://stackoverflow.com/a/31396042
    for col in ['DAY', 'MONTH', 'YEAR', 'ID']:
        df_element = move_col_to_front(col, df_element)
    # Convert numerical values to float
    df_element.loc[:,element] = df_element.loc[:,element].astype(float)
    # print df_element
    return df_element
    
def move_col_to_front(element, df):
    element = element.upper()
    cols = df.columns.tolist()
    cols.insert(0, cols.pop(cols.index(element)))
    df = df.reindex(columns=cols)
    return df

def dly_to_csv(ftp, station_id):    
    ftp_filename = station_id + '.dly'
    
    # Write .dly file to stream using StringIO using FTP command 'RETR'
    s = io.BytesIO()
    ftp.retrlines('RETR ' + ftp_path_dly_all + ftp_filename, s.write)
    s.seek(0)
    
    # Write .dly file to dir to preserve original # FIXME make optional?
    with open(os.path.join(output_dir, ftp_filename), 'wb+') as f:
        ftp.retrbinary('RETR ' + ftp_path_dly_all + ftp_filename, f.write)
    
    # Move to first char in file
    s.seek(0)
    # File params
    num_chars_line = 269
    num_chars_metadata = 21

    element_list = ['PRCP', 'SNOW', 'SNWD', 'TMAX', 'TMIN']
    
    '''
    Read through entire StringIO stream (the .dly file) and collect the data
    '''
    all_dicts = {}
    element_flag = {}
    prev_year = '0000'
    i = 0
    while True:
        i += 1
        
        '''
        Read metadata for each line (one month of data for a particular element per line)
        '''
        id_station = s.read(11)
        year = s.read(4)
        month = s.read(2)
        day = 0
        element = s.read(4)
        
        # If this is blank then we've reached EOF and should exit loop
        if not element:
            break
        
        '''
        Print status
        '''
        if year != prev_year:
            # print('Year {} | Line {}'.format(year, i))
            prev_year = year
        
        '''
        Loop through each day in rest of row, break if current position is end of row
        '''
        while s.tell() % num_chars_line != 0:
            day += 1
            # Fill in contents of each dict depending on element type in current row
            if day == 1:
                try:
                    first_hit = element_flag[element]
                except:
                    element_flag[element] = 1
                    all_dicts[element] = {}
                    all_dicts[element]['ID'] = []
                    all_dicts[element]['YEAR'] = []
                    all_dicts[element]['MONTH'] = []
                    all_dicts[element]['DAY'] = []
                    all_dicts[element][element.upper()] = []
                    all_dicts[element][element.upper() + '_FLAGS'] = []
                
            value = s.read(5)
            flags = get_flags(s)
            if value == '-9999':
                continue
            all_dicts[element]['ID'] += [station_id] 
            all_dicts[element]['YEAR'] += [year]
            all_dicts[element]['MONTH'] += [month]
            all_dicts[element]['DAY'] += [str(day)]
            all_dicts[element][element.upper()] += [value]
            all_dicts[element][element.upper() + '_FLAGS'] += flags
            
    '''
    Create dataframes from dict
    '''

    #* NOTE: all_dicts are values
    # print all_dicts

    #* NOTE: all_dicts.keys() are all element types
    # print all_dicts.keys()

    all_dfs = {}
    for element in list(all_dicts.keys()):
        all_dfs[element] = create_dataframe(element, all_dicts[element])

    # print all_dfs
    #* NOTE: Data is still shown here
    
    '''
    Combine all element dataframes into one dataframe, indexed on date. 
    '''
    # pd.concat automagically aligns values to matching indices, therefore the data is date aligned!
    list_dfs = []
    for df in list(all_dfs.keys()):
        list_dfs += [all_dfs[df]]
    df_all = pd.concat(list_dfs, axis=1, sort='True')
    # df_all.index.name = 'DATE'
    
    # print df_all
    '''
    Remove duplicated/broken columns and rows
    '''
    # https://stackoverflow.com/a/40435354
    df_all = df_all.loc[:,~df_all.columns.duplicated()]

    '''
    Output to CSV, convert everything to strings first
    '''
    # NOTE: To open the CSV in Excel, go through the CSV import wizard, otherwise it will come out broken
    df_out = df_all.astype(str)
    df_out.to_csv(os.path.join(output_dir, station_id + '.csv'))
    print('\nOutput CSV saved to: {}'.format(os.path.join(output_dir, station_id + '.csv')))
    
'''
Main
'''

inFile = open('Retrieve_Files/output/Stations.csv', 'r')
theCsvData = csv.reader(inFile) #this creates a special object that the csv library knows how to access
allData=[]

#This takes the information read from the cvs and creates an index from it
for aRow in theCsvData:
  allData.append(aRow[:])

# Write list for station ids
stations = []
# Split dataset id and station id, keep station id ([-1])
for aRow in allData:
    temp = str(aRow[-4])
    new = temp.split(':', 1)[-1]
    stations.append(new)


for aRow in stations:
    station_id=aRow
    print station_id
    ftp = connect_to_ftp()
    dly_to_csv(ftp, station_id)
    ftp.quit()

# inFile = open('output/USC00323117.csv', 'r')
# theCsvData = csv.reader(inFile) #this creates a special object that the csv library knows how to access
# allData=[]

# for aRow in theCsvData:   #This takes the information read from the cvs and creates an index from it
#   allData.append(aRow[:])
# print len(allData)