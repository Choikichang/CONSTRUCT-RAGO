import pandas as pd

def renumber_id_column(input_tsv, output_tsv):
    # TSV 파일 읽기
    df = pd.read_csv(input_tsv, sep='\t')

    # id 컬럼을 순차적으로 다시 넘버링
    df['id'] = range(1, len(df) + 1)
    df['id'] = df['id'].apply(lambda x: f"{x:04d}")

    # 수정된 데이터를 새로운 TSV 파일로 저장
    df.to_csv(output_tsv, sep='\t', index=False)

if __name__ == "__main__":
    input_tsv = "/data/data/Korea_construction_standard/sibang/Con_STS.tsv"  # 입력 TSV 파일 경로
    output_tsv = "/data/data/Korea_construction_standard/sibang/Con_STS_mod.tsv"  # 출력 TSV 파일 경로
    renumber_id_column(input_tsv, output_tsv)
    print(f"TSV file with renumbered IDs created: {output_tsv}")
