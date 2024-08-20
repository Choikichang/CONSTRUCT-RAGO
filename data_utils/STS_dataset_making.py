import os
import re
import glob

def extract_terms_and_definitions(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    terms_and_definitions = []
    extracting = False
    current_term = ''
    current_definition = ''
    
    for line in lines:
        line = line.strip()
        if "용어의 정의" in line:
            extracting = True
            continue
        if extracting:
            if re.match(r'\d', line):
                break
            if ':' in line:
                if current_term and not re.search(r'\d', current_definition):
                    terms_and_definitions.append((current_term, current_definition))
                parts = line.split(':', 1)
                if len(parts) == 2:
                    current_term, current_definition = parts
                    current_term = current_term.strip()
                    current_definition = current_definition.strip()
            else:
                current_definition += ' ' + line
    
    if current_term and current_definition and not re.search(r'\d', current_definition):
        terms_and_definitions.append((current_term, current_definition))
    
    return terms_and_definitions

def create_tsv(all_terms_and_definitions, output_tsv):
    header = "genre\tfilename\tyear\tid\tscore\tsentence1\tsentence2\n"
    with open(output_tsv, 'w', encoding='utf-8') as f:
        f.write(header)
        idx = 1
        for filename, terms_and_definitions in all_terms_and_definitions:
            for term, definition in terms_and_definitions:
                id_str = f"{idx:04d}"
                row = f"Con-captions\tConst\t2024\t{id_str}\t5.000\t{term}\t{definition}\n"
                f.write(row)
                idx += 1

def process_folder(input_folder, all_terms_and_definitions):
    for txt_file in glob.glob(os.path.join(input_folder, "*.txt")):
        terms_and_definitions = extract_terms_and_definitions(txt_file)
        all_terms_and_definitions.append((txt_file, terms_and_definitions))

def main(input_folders, output_tsv):
    all_terms_and_definitions = []
    for folder in input_folders:
        process_folder(folder, all_terms_and_definitions)
    create_tsv(all_terms_and_definitions, output_tsv)
    print(f"TSV file created: {output_tsv}")
if __name__ == "__main__":
    input_folders = [
        "/data/data/Korea_construction_standard/sibang",
        "/data/data/Korea_construction_standard/design",
    ]  # 여러 TXT 파일 폴더 경로 리스트
    output_tsv = "/data/data//Korea_construction_standard/sibang/Con_STS2.tsv"  # 출력 TSV 파일 경로
    main(input_folders, output_tsv)