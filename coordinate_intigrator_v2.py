# A program to integrate lattitude & longitude data in the description of fasta file
# Arafat

# V 0.1 6 April 2015 for WSSV dataset
# V 0.2 12 April 2015 for FMDV dataset


from Bio import SeqIO

def extract_coordinates(fileName):
    '''Input:
            - fileName: name of the tab-delimited file which contians country and its coordinates
       Output:
            - A dictionary of tuples {country:(lattitude, longitude)]'''
    fileIn = open(fileName)
    raw = fileIn.read().split('\n')
    fileIn.close()
    return {i.split('\t')[0]:i.split('\t')[1:] for i in raw if len(i.split('\t')[0]) != 0}


def extract_info(fileName):
    '''Input:
            - fileName: name of csv file
        Output:
            - A dictionary of tuples {genbankID: (isolation_date, isolation_place, lattitude, longitude)}        
    '''
    fileIn = open(fileName)
    raw = fileIn.read().split('\n')
    fileIn.close()
    return {i.split(',')[0]:i.split(',')[1:] for i in raw if len(i) != 0}
    



def write_fasta_description(fileName, coords):
    '''Input:
            - fileName: name of the fasta file
            - coords: name of countries and their coordinates data
       This function update description of fasta file with coordinate information
    '''
    recordsList = []
    for record in SeqIO.parse(fileName, 'fasta'):
        signal = 0
        for acc in coords.keys():
            if acc in record.description:
                record.description += '~'+coords[acc][0]+'~' + coords[acc][1] + ',' + coords[acc][2] + '_' + coords[acc][3] + '_' + coords[acc][4]
                record.id = ''
                
                signal = 1
                recordsList.append(record)
                break
        if signal == 0:
            print record.id, 'ID not found!'
    output_handle = open('coordinate_description_output.fas', 'w')
    SeqIO.write(recordsList, output_handle, 'fasta')
    pass




if __name__ == '__main__':
    coords = extract_info('seq_description.csv')
    fileName = 'Indian_subcontinent_truncated.fas'
    write_fasta_description(fileName, coords)
    
    

        

    
            

    
    
    
                
