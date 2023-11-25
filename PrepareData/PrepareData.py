import argparse


def prepareData(input_file_path, output_file_path):
    # Liste für die extrahierten Sätze
    holo_sentences = []

    # Öffne die vorhandene Datei und lese die Sätze nach "Holo:" aus
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        is_holo_section = False
        for line in input_file:
            line = line.strip()
            if line.startswith('Holo: '):
                is_holo_section = True
                holo_sentences.append(line[5:])
            elif is_holo_section and line == '':
                is_holo_section = False
            elif not line.startswith('Holo: '):
                is_holo_section = False
            elif is_holo_section:
                holo_sentences.append(line)

    # Schreibe die extrahierten Sätze nach "Holo:" in die neue Datei
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for sentence in holo_sentences:
            output_file.write(sentence + '\n')

    print("Done")


# noinspection PyInterpreter
if __name__ == '__main__':
    # # # # # # # # # # # # # # INPUT PARSER # # # # # # # # # # # # # #
    parser = argparse.ArgumentParser(description='Prepare Data')
    parser.add_argument('-i', '--inputPath', dest='inputPath', required=True, help='inputPath')
    parser.add_argument('-o', '--outputPath', dest='outputPath', required=True, help='outputPath')
    args = parser.parse_args()

    # read params
    input_file_path = args.inputPath
    output_file_path = args.outputPath

    prepareData(input_file_path, output_file_path)
