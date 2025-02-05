import json

def load_json(file_path):
    # JSON 파일을 불러오는 함수
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def evaluate_answers(data):
    # 정답 여부를 평가하는 함수
    correct_count = 0
    results = [{'question': item['question'], 'correct_answer': item['correct_answer'], 'generated_answer': item['generated_answer'], 'is_correct': None} for item in data]
    current_index = 0

    while current_index < len(data):
        item = results[current_index]
        print(f"\nQuestion {current_index + 1}: {item['question']}")
        print(f"Correct Answer: {item['correct_answer']}")
        print(f"Generated Answer: {item['generated_answer']}")

        # Correct Answer와 Generated Answer가 동일하면 자동으로 정답 처리
        if item['correct_answer'].strip() == item['generated_answer'].strip():
            print("The generated answer matches the correct answer. Automatically marking as correct.")
            item['is_correct'] = True
            correct_count += 1
            current_index += 1
            continue  # 다음 문제로 넘어감

        if item['is_correct'] is not None:
            print(f"Previous Answer: {'Correct' if item['is_correct'] else 'Incorrect'}")

        # 사용자가 T, F 또는 B 입력
        while True:
            user_input = input("Is this correct? (T for True, F for False, B to go back): ").strip().upper()
            if user_input == 'T':
                if item['is_correct'] is None:  # 처음 입력 시 정답 개수를 증가
                    correct_count += 1
                elif item['is_correct'] == False:  # 이전에 오답이었다면 정답으로 수정
                    correct_count += 1
                item['is_correct'] = True
                break
            elif user_input == 'F':
                if item['is_correct'] is None:  # 처음 입력 시 오답을 처리
                    pass  # correct_count 변화 없음
                elif item['is_correct'] == True:  # 이전에 정답이었다면 오답으로 수정
                    correct_count -= 1
                item['is_correct'] = False
                break
            elif user_input == 'B':
                if current_index > 0:
                    current_index -= 1
                else:
                    print("This is the first question, cannot go back.")
                break
            else:
                print("Please enter 'T' for True, 'F' for False, or 'B' to go back.")
        
        if user_input != 'B':  # 'B'를 누르지 않은 경우 다음으로 이동
            current_index += 1

    return results, correct_count

def save_results(results, output_path):
    # 결과를 JSON 파일로 저장하는 함수
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print(f"Results saved to {output_path}")

def calculate_accuracy(correct_count, total):
    # 정답률을 계산하는 함수
    accuracy = (correct_count / total) * 100
    return accuracy

def main():
    # 메인 함수
    file_path ="/home/choi/Git/RAG_con_doc/langchain/768_First_results.json"
    output_path = "/home/choi/Git/RAG_con_doc/langchain/768_First_results_Human.json"

    data = load_json(file_path)
    total_questions = len(data)

    # 답변 평가
    results, correct_count = evaluate_answers(data)

    # 정답률 계산
    accuracy = calculate_accuracy(correct_count, total_questions)
    print(f"\nEvaluation completed!")
    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {correct_count}")
    print(f"Accuracy: {accuracy:.2f}%")

    # 결과 저장
    save_results(results, output_path)

if __name__ == "__main__":
    main()
